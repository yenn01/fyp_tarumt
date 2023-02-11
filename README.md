# trend
![image](https://user-images.githubusercontent.com/48972583/218265911-88eaa5b1-494a-4d81-af4d-7930c01e2fbc.png)

### Social Media Topic Sentiment Analysis and Visualisation
A self-hosted web application that allows for user inputted topic sentiment analysis and visualisation of Twitter tweets. 

This project was built as the Final Year Project when pursuing the Bachelor of Computer Science (Honours) in Data Science in Tunku Abdul Rahman University of Management and Technology.

Accuracy of sentiments are achieved through the use of [RoBERTa-base model by cardiffnlp](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest).

## Front-End
The front end is built on the Svelte Framework. [tinro](https://github.com/AlexxNB/tinro) was used to handle routing between pages. Various Svelte libraries were used to enhance user experience such as [svelte-loading-spinners](https://www.npmjs.com/package/svelte-loading-spinners). For certain animations, [animejs](https://animejs.com/) was used to animate them. [ApexChart.js](https://apexcharts.com/) was used for data visualisation through charts. 

## Back-End
The back end is built on Python with the [Flask](https://flask.palletsprojects.com/en/2.2.x/) library as end-points for interaction between the web application and the back-end. Data pre-processing of tweets utilised Regex expressions, [cleantext](https://pypi.org/project/cleantext/), and [Pandas dataframes](https://pandas.pydata.org/docs/index.html).

## Tweet scrapping
The [twint library](https://github.com/twintproject/twint) is used for scrapping tweets from Twitter.

### More Pictures
![image](https://user-images.githubusercontent.com/48972583/218265921-649e6793-a998-42ec-9e7d-5dd41565291d.png)
![image](https://user-images.githubusercontent.com/48972583/218265945-0a02f019-a3e6-4c5c-a437-661ecbf5b7fa.png)
![image](https://user-images.githubusercontent.com/48972583/218265951-ce11a4ba-fc55-46bf-8bc7-f3d68b691afa.png)

## Limitations
- Lack of queue system prevents multiple concurrent users from utilising the system at the same time. [Redis](https://redis.io/) has been considered to alleviate this limitation.
