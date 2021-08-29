# ETL Notes
### Extract-Transform-Load
--- 
Fist, design an Entity Relationship Diagram (ERD) as a visual aid, prior to creating Tables in PostgreSQL. (see below)

<img width="601" alt="Screen Shot 2021-08-29 at 7 06 58 AM" src="https://user-images.githubusercontent.com/82069038/131248251-f9881d74-f64b-44ff-bac6-ca4ee8693219.png">

We're tasked with priming raw data from JSON files via Twitter's API.\
Nevertheless, we'll consider the following questions before any unsupervised learning models can be applied and results analyzed. 

   -  Will I be able to easily hand off this data set to other teams?
   -  Does the data contain excess data that we don’t really need?
   -  How can I get this data to be used to create great visualizations?
--- 

Then we'll download necessary libraries prior to analysing tweets with Python and PostgreSQL
<b>

 -    tweepy: Python library for accessing the Twitter API
 -   SkLearn: popular machine learning library
 -    NLTK: Natural language processing library
 -   re: regular expression library
 -   pandas: popular data analysis library
    



