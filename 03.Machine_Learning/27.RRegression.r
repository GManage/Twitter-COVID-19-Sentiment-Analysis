
library(dplyr)
path = "C:\\OneDrive\\Desktop\\Assignments\\COVID19\\"

#file = "agg_sentiment_w3classifiers_olddata.csv"
file = "agg_sentiment_w3classifiers_olddata_wNLTK.csv"

filepath = paste(path , file, sep="")

classifiers <- read.csv(filepath,check.names=F,stringsAsFactors = F)

file = "vaccinationbydate.csv"
filepath = paste(path , file, sep="")

administered <- read.csv(filepath,check.names=F,stringsAsFactors = F)

tweetdata <- merge (classifiers, administered, by="normalized_date")

Administered <- tweetdata$Administered
textblob_agg_sentiment <- tweetdata$textblob_agg_sentiment
nltk_agg_sentiment <- tweetdata$nltk_agg_sentiment
vader_agg_sentiment <-  tweetdata$Vader_agg_sentiment
vader_agg_sentiment


fit <- lm(Administered ~ textblob_agg_sentiment + nltk_agg_sentiment + vader_agg_sentiment, date = tweetdata)
fit <- lm(Administered ~ nltk_agg_sentiment, date = tweetdata)

summary(fit)

