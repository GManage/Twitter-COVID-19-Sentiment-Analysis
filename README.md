# Twitter COVID-19 Sentiment Analysis
    Members: Christopher Bach | Khalid Hamid Fallous | Jay Hirpara | Jing Tang | Graham Thomas | David Wetherhold

  
## Project Overview
This project seeks to identify any correlation between ∆ daily inoculation rates and ∆ twitter sentiment surrounding COVID-19. The reason why this topic was selected is because it is a very relevant topic in today's world causing a global pandemic crisis.
      
  - Data Sources: [Twitter](https://www.trackmyhashtag.com/blog/free-twitter-datasets/) | [CDC](https://covid.cdc.gov/covid-data-tracker/#datatracker-home)

## Analysis Methods
    Integrated Database  
Extract csv datasets from data sources (referenced above), transforming and cleaning them with Python, and loading the datasets using Amazon Web Services and PostgreSQL (server/database). This allows us to establish connection with our model, and store static data for use during the project.
- Constructed as an Amazon RDS instance: 
    - Connection Parameter: (covidsentiment.cqciwtn1qpki.us-east-2.rds.amazonaws.com)
    - Accessed with a password upon request
<p>
  
Further transformations:
  - [Entity Relationship Diagram](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/9ab668f1fcd96a28bcabaf22c940531f12dbc8ed/02.Database/UpdatedDBStructure.png)
  - [Tables](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/9ab668f1fcd96a28bcabaf22c940531f12dbc8ed/02.Database/02.CreateTables.ipynb)
  - [Joins/Strings](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/9ab668f1fcd96a28bcabaf22c940531f12dbc8ed/02.Database/12.LoadCSVtoDB.ipynb)
 <p>
   
    Machine Learning Model

Next, implementing a natural language processing algorithm allows us to gather our [sentiment analysis](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/702f821038f6f4596ff8908df69acc57ed5bbd80/03.Machine_Learning/Sentiment_Analysis_MNBclassifier_D2.ipynb)
- Machine Learning Libraries: nltk, sklearn 
- Description of preliminary data preprocessing
1. Load historical twitter covid vaccine data from kaggle. 
2. Clean tweets with clean_tweet function(regex), tokenize and get ready for text classification. Also, clean up function for removing hashtags, URL's, mentions, and retweets.
3. Apply Textblob.sentiment.polarity and Textblob.sentiment.subjectivity, ready for sentiment analysis. 
4. Apply analyze_sentiment function on tweet texts to label texts with sentiment range from -1 (negative) to 1(positve). 
5. Plot top 10 words from postivie and negative-resulted words. 

- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
1. Import CountVectorizerfrom sklearn.feature_extraction.text. CountVectorizer is a tool provided by the scikit-learn library in Python. It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text. The value of each cell is nothing but the count of the word in that particular text sample.
2. Fit sentiment texts features with vectorizer, and target sentiment column. 

- Description of how data was split into training and testing sets
Splitting into training and testing set so as to evaluate the classifier. The aim is to get an industry standard sample split of 80% train and 20% test.
     
- Explanation of model choice, including limitations and benefits
1. Naive Bayes classifier is a collection of many algorithms where all the algorithms share one common principle, and that is each feature being classified is not related to any other feature. The algorithm is based on the Bayes theorem and predicts the tag of a text such as a piece of email or newspaper article. It calculates the probability of each tag for a given sample and then gives the tag with the highest probability as output.
The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification).Multinomial Naive Bayes algorithm is a probabilistic learning method that is mostly used in Natural Language Processing (NLP). 
2. Multinomial Naive Bayes classification algorithm tends to be a baseline solution for sentiment analysis task. The basic idea of Naive Bayes technique is to find the probabilities of classes assigned to texts by using the joint probabilities of words and classes.
3. Naive Bayes algorithm is only used for textual data classification and cannot be used to predict numeric values. The result of naive bayes model provide statistical sense by predicting how often that certain words with the sentimental labels appear, which does not necessarily indicate the factual attitudes/sentiments towards covid vaccine, and it does not work with regression because it is not numerical data. One of the benefits of Naive Bayes is that if its assumption of the independence of features holds true, it can perform better than other models and requires much less training data. 

- Changes of model choice from segment 2 to segment 3
1. Vader Analysis: VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. VADER not only tells about the Positivity and Negativity score but also tells us about how positive or negative a sentiment is.
5. Solution to limitations: We discovered the most common words appeared in our twitter dataset are associated with covid vaccines because we retrieved the data with covid vaccine as search terms. Textblob Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float which lies in the range of [0,1]. We are trying to process text classification with another function to get more accurate sentiment labels on the tweet texts. 
<p>
  
    Dashboard
  [COVID-19 DASHBOARD](https://public.tableau.com/app/profile/jay.s.hirpara/viz/COVID-19Dashboard_16313779892960/COVID-19Dashboard?publish=yes)
- A blueprint for the dashboard is created and includes all of the following:
- Storyboard on Google Slide(s)
- Description of the tool(s) that will be used to create final dashboard
- Description of interactive element(s)
<p>
  
 [Presentation](https://docs.google.com/presentation/d/1mDPH7XcgGB0oe8LvYLOQ0zkui6xMUB3WQaB8qf4a__4/edit?usp=sharing)
- Selected topic
- Why we selected our topic
- Description of our source of data
- Questions we hope to answer with the data
- Description of the data exploration phase of the project
- Description of the analysis phase of the project

## Challenges and Limitations
    Problems
- Some members ran into issues with gaining Academic Twitter accounts to be able to access the Twitter API.
- After gaining access to tweets our original goal of using the location of tweets was not possible due to most tweets not having geotag data
- The Twitter API was very limited to the amount of data we could pull
- Group ran into a machine learning natural language paradox, where we noticed an issue within our sentiment analysis. When analyzing tweets for Covid-19 Vaccination sentiment 
(pro/anti-vaccine) when running into a tweet such as “I hate anti-vaxxers”, this would return a negative sentiment when this person is actually pro-vaccine.
- Using academic accounts only allows access back to 7 days of tweets. We could not get twitter's full archive search without having a twitter scholar account. 
<p>
    
    Solutions
- Members had to submit extra information to the Twitter developers platform to qualify for academic research accounts
- Due to lack of geodata, the team decided to switch to using twitter sentiment over time, rather than region
- The group decided to use a Kaggle Dataset, which provided us with tweets from December 21, 2020. 
