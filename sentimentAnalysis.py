from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import difflib
import twint
import nest_asyncio
import json
import pandas
# nest_asyncio.apply()

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
analysis = pipeline(task="sentiment-analysis",model=model,tokenizer=tokenizer) 


app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio = SocketIO(app)

id = 1;

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
    return Tweets_df
    
def clean(df):
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

    #TODO: Remove punctuations.
    #TODO: Convert emojis to text.
    #TODO: Remove mentions
    #TODO: Remove URLS
    #TODO: Remove Stop Words
    #TODO: Translate abbreviations
    #TODO: Expand contractions
    #TODO: Lemmatise
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
        raw = scrape(sentence)
        cleaned = clean(raw)
        s_df = sentiment(cleaned)
        score_df = s_df[s_df['score'] > 0.5]         
        return score_df['sentiment'].value_counts().to_json()
    except Exception as e:
        print(e)
    return "Error",400

# @app.route('scrapping',methods=['GET','POST'])
# def scrapping():
#     print("scrapping")


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=80, use_reloader=False)

