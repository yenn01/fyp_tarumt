import eventlet
eventlet.monkey_patch(thread=False)
from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO,send,emit
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from cleantext import clean
import difflib
import twint
import nest_asyncio
import json
import pandas
import re
#nest_asyncio.apply()


tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
analysis = pipeline(task="sentiment-analysis",model=model,tokenizer=tokenizer) 


app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio = SocketIO(app,async_mode = 'eventlet')

id = 1;

def rmMention(passed):
    clean = re.sub(r'@\w+', '',passed)
    return clean

#Function used to measure similarity between posts and then remove them (Prevents Bot Spam Messages)
dupe_df = None
def dedupe(df,threshold=0.85):
    dupe = df.tweet.apply(lambda row: difflib.get_close_matches(row, list(df[df.tweet!=row].tweet), cutoff = threshold))    
    df_dupes = dupe[dupe.astype(bool)]
    df_deduped = df.drop(df_dupes.index,axis=0)
    return df_deduped,df_dupes


def scrape(topic,limit=400):
    c = twint.Config()
    c.Search = topic
    c.Limit = limit
    c.Lang = "en"
    c.Pandas = True
    
    # Run
    twint.run.Search(c)
    Tweets_df = twint.storage.panda.Tweets_df
    socketio.emit("completed_scrape")
    return Tweets_df
    
def clean_process(df):
    #Get all tweets which are in English
    en_df = df.query("language == 'en'")

    #Remove duplicated tweets
    de_df, dupe_df = dedupe(en_df)

    #Subset required tweets only
    sub_df = de_df[["tweet", "nlikes","nretweets","nreplies"]]

    #Calculate and insert as new column the traction of posts.
    sub_df["traction"] = sub_df["nlikes"] * 2 + sub_df["nreplies"] * 3 + sub_df["nretweets"] * 4

    #Sort according to traction
    sort_df = sub_df.sort_values(by=["traction"], ascending=False)


    #Convert emojis to text, remove any emails, phone numbers and urls
    #sort_df["tweet"] = sort_df["tweet"].apply(clean,lower=True,no_line_breaks=True,no_urls=True,no_emails=True,no_phone_numbers=True)
    
    #Remove mentions in tweet
    sort_df["tweet"] = sort_df["tweet"].apply(rmMention)

    #TODO: Translate abbreviations
    #TODO: Expand contractions
    #TODO: Lemmatise
    socketio.emit("completed_clean")
    return sort_df

def s_analysis(tweet):
    analysed = analysis(tweet)
    return analysed[0]['label'], analysed[0]['score']

def sentiment(df):
    df["sentiment"],df["score"] = zip(*df["tweet"].apply(s_analysis))
    return df





@app.route('/')
def base():
    return send_from_directory('public','index.html')

@app.route('/<path:path>')
def home(path):
    return send_from_directory('public',path)

@app.route('/scrape',methods=['GET','POST'])
def analyse():
    try:
        
        sentence = request.args.get('text')

        if not sentence:
            return "Error",400

        #Carry out scrapping, sends completed scrape when done
        raw = scrape(sentence)
        

        #Carry out cleaning, sends completed clean when done
        cleaned = clean_process(raw)
        

        #Carry out sentiment analysis on the rows of the dataframe
        s_df = sentiment(cleaned)
        score_df = s_df[s_df['score'] > 0.5]        

        socketio.emit("high_traction",cleaned.head(4).to_json(orient="records"))

        #Return the number of counts of tweets  
        return score_df['sentiment'].value_counts().to_json()
    except Exception as e:
        print(e)
    return "Error",400

# @app.route('scrapping',methods=['GET','POST'])
# def scrapping():
#     print("scrapping")

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=80, use_reloader=False)

