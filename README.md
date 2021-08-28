# Machine Learning Branch
Group Project: Module 20 


Members:
Jay Hirpara
Jing Tang
Graham Thomas (Square)
David Wetherfield
Christopher Bach
Khalid Hamid Fallous

Overview



Project Goal:

This project aims to collect some data and perform sentiment analysis surrounding trending topics related to covid-19 and covid-19 vaccines. We will perform the ETL using python and a SQL database, and also come up with some machine learning algorithms to predict trending topics and hashtags related to the virus and it's vaccines.  The project will bring some meaningful discussions over whether getting vaccinated stands in the way of individual personal liberty, including but not limited to the topic of employers requirment to have staff vaccinated.



## Machine Learning Approach:

We use and compare various different methods for sentiment analysis on tweets (a binary classification problem). The training dataset is expected to be a csv file of type tweet_id,sentiment,tweet where the tweet_id is a unique integer identifying the tweet, sentiment is either 1 (positive) or 0 (negative), and tweet is the tweet enclosed in "". Similarly, the test dataset is a csv file of type tweet_id,tweet.


### Logistic Regression:
Logistic regression is a classification algorithm, used when the value of the target variable is categorical in nature. Logistic regression is most commonly used when the data in question has binary output, so when it belongs to one class or another, or is either a 0 or 1.



Resources:
1. https://www.youtube.com/watch?v=4UI9qZw7DXg
2. 
