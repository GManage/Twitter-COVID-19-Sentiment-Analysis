# Twitter COVID-19 Sentiment Analysis
    Members: Christopher Bach | Khalid Hamid Fallous | Jay Hirpara | Jing Tang | Graham Thomas | David Wetherhold

**Communication Protocols**:
- Zoom: Monday/Wednesday meetings
- Slack: brainstorming, member assignment, progress/code updates, meeting arrangements
<p>
  
## Project Overview
This project seeks to identify any correlation between ∆ daily inoculation rates and ∆ twitter sentiment surrounding COVID-19. 
      
  - Data Sources: [Twitter](https://www.trackmyhashtag.com/blog/free-twitter-datasets/) | [CDC](https://covid.cdc.gov/covid-data-tracker/#datatracker-home)

## Analysis Methods
    Integrated Database  
Extract csv datasets from data sources (referenced above), transforming and cleaning them with Python, and loading the datasets using Amazon Web Services and PostgreSQL (server/database). This allows us to establish connection with our model, and store static data for use during the project. 
<p>
  
Further transformations:
  - [Entity Relationship Diagram](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/9ab668f1fcd96a28bcabaf22c940531f12dbc8ed/02.Database/UpdatedDBStructure.png)
  - [Tables](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/9ab668f1fcd96a28bcabaf22c940531f12dbc8ed/02.Database/02.CreateTables.ipynb)
  - [Joins/Strings](https://github.com/GManage/Twitter-COVID-19-Sentiment-Analysis/blob/9ab668f1fcd96a28bcabaf22c940531f12dbc8ed/02.Database/12.LoadCSVtoDB.ipynb)
 <p>
   
    Machine Learning Model
Next, implementing a natural language processing algorithm allows us to gather our sentiment analysis. 
- Description of preliminary data preprocessing
- Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
- Description of how data was split into training and testing sets
- Explanation of model choice, including limitations and benefits
<p>
  
    Dashboard
  [link to dashboard]
- A blueprint for the dashboard is created and includes all of the following:
- Storyboard on Google Slide(s)
- Description of the tool(s) that will be used to create final dashboard
- Description of interactive element(s)
<p>
  
 [Presentation](https://docs.google.com/presentation/d/1mDPH7XcgGB0oe8LvYLOQ0zkui6xMUB3WQaB8qf4a__4/edit?usp=sharing)
- Selected topic
- Reason why they selected their topic ✓ Description of their source of data
- Questions they hope to answer with the data
- Description of the data exploration phase of the project
- Description of the analysis phase of the project