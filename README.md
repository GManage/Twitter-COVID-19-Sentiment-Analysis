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





## Machine Learning Approach:

We use and compare various different methods for sentiment analysis on tweets (a multiclass classification problem). The training dataset is expected to be a csv file of type tweet_id,sentiment,tweet where the tweet_id is a unique integer identifying the tweet, sentiment is either positive , negative , or neutral and tweet is the tweet enclosed in "". Similarly, the test dataset is a csv file of type tweet_id,tweet. In addition, we will also use data set from the CDC to help compare and give a better geographical comparison.


### Logistic Regression:
Logistic regression is a classification algorithm, used when the value of the target variable is categorical in nature. Logistic regression is most commonly used when the data in question has binary output, so when it belongs to one class or another, or is either a 0 or 1.


Next, implementing a natural language processing algorithm allows us to gather our sentiment analysis

Machine Learning Libraries: nltk, sklearn
Description of preliminary data preprocessing
Load historical twitter covid vaccine data from kaggle.
Clean tweets with clean_tweet function(regex), tokenize and get ready for text classification. Also, clean up function for removing hashtags, URL's, mentions, and retweets.
Apply Textblob.sentiment.polarity and Textblob.sentiment.subjectivity, ready for sentiment analysis.
Apply analyze_sentiment function on tweet texts to label texts with sentiment range from -1 (negative) to 1(positve).
Plot top 10 words from postivie and negative-resulted words.
Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
Import CountVectorizerfrom sklearn.feature_extraction.text. CountVectorizer is a tool provided by the scikit-learn library in Python. It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text. The value of each cell is nothing but the count of the word in that particular text sample.
Fit sentiment texts features with vectorizer, and target sentiment column.
Description of how data was split into training and testing sets Splitting into training and testing set so as to evaluate the classifier. The aim is to get an industry standard sample split of 80% train and 20% test.

Explanation of model choice, including limitations and benefits

Naive Bayes classifier is a collection of many algorithms where all the algorithms share one common principle, and that is each feature being classified is not related to any other feature. The algorithm is based on the Bayes theorem and predicts the tag of a text such as a piece of email or newspaper article. It calculates the probability of each tag for a given sample and then gives the tag with the highest probability as output. The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification).Multinomial Naive Bayes algorithm is a probabilistic learning method that is mostly used in Natural Language Processing (NLP).
Multinomial Naive Bayes classification algorithm tends to be a baseline solution for sentiment analysis task. The basic idea of Naive Bayes technique is to find the probabilities of classes assigned to texts by using the joint probabilities of words and classes.
Naive Bayes algorithm is only used for textual data classification and cannot be used to predict numeric values. The result of naive bayes model provide statistical sense by predicting how often that certain words with the sentimental labels appear, which does not necessarily indicate the factual attitudes/sentiments towards covid vaccine, and it does not work with regression because it is not numerical data. One of the benefits of Naive Bayes is that if its assumption of the independence of features holds true, it can perform better than other models and requires much less training data.
Changes of model choice from segment 2 to segment 3
Vader Analysis: VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. VADER not only tells about the Positivity and Negativity score but also tells us about how positive or negative a sentiment is.
Solution to limitations: We discovered the most common words appeared in our twitter dataset are associated with covid vaccines because we retrieved the data with covid vaccine as search terms. Textblob Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float which lies in the range of [0,1]. We are trying to process text classification with another function to get more accurate sentiment labels on the tweet texts.
Changes from segement 3 to segment 4
Added sentiment "NLTK" which is a votes based combined algorithm encompassing multiple natural language processing techniques.
