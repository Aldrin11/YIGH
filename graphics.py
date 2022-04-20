import matplotlib.pyplot as plt
import csv
import pandas as pd
import dateutil
import numpy as np
import re
from datetime import datetime
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

###############################################################
#   High-Level Objectives:
    #### 1. create word cloud to show most used words in tweets
    #### 2. create positive vs negative sentiment pie chart
    #### 3. create linear regression to showcase the relationship between sentiment and subjectivity
###############################################################
#   Process:
    #### 0. data gathering : use web crawler api to fetch twitter data
    #### 1. clean & process data : remove (@mentions, https links, prepositions)
    #### 2. create functions for sentiment and subjectivity
    #### 3. create functions drawing word cloud
    #### 4. create function for graphing pie chart
    #### 5. create function for graphing linear regression
    #### 6. review code for style and refactoring
##############################################################################################################################

# Read CSV and Initialize DataFrame
df = pd.read_csv("manila.csv",header = None)

tweets_list = df[10].tolist() # transforms text_column into a list

### function for cleaning singular tweets
def clean (text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # removes @mentions.
    text = re.sub(r'https?:\/\/\S+', '', text) # removes hyperlinks
    text = re.sub(r'sa', '', text)  # removes most common Filipino prepositions
    text = re.sub(r'ng', '', text)  # removes most common Filipino prepositions
    text = re.sub(r'mga', '', text) # removes most common Filipino prepositions
    text = re.sub(r'na', '', text)  # removes most common Filipino prepositions
    text = re.sub(r'ang', '', text) # removes most common Filipino prepositions
    text = re.sub(r'at', '', text)  # removes most common English prepositions
    text = re.sub(r'it', '', text)  # removes most common English prepositions
    text = re.sub(r'a', '', text)   # removes most common English prepositions
    text = re.sub(r'an', '', text)  # removes most common English prepositions
    return text

### function for cleaning entire text list
def clean_list (list):
    for i in range(0,(len(list))):
        list[i] = clean(list[i])
    return list

tweets_list = clean_list(tweets_list)  # apply cleaning function
# with open('manila.csv','w') as f:
#     write = csv.writer(f)
#     write.writerow(tweets_list)

############################################################ Sentiment Analysis ################################################################################
### 1. sentiment(aka polarity) function. Uses textblob api
def subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

### 2. polarity function. Uses textblob api
def polarity(text):
    return TextBlob(text).sentiment.polarity

### 3. list to subjectivity vector function. transforms list of text into list of subjectivity values
def create_subj_vector(list):
    subj = []
    for i in range(0,(len(list))):
        subj.append(subjectivity(list[i]))
    return subj

####. list to polarity vector function.  transforms list of text into list of polarity values
def create_pol_vector(list):
    pol = []
    for i in range(0,(len(list))):
        pol.append(polarity(list[i]))
    return pol

#### list to dataframe function. transforms list into a dataframe
def create_sentiment_df(list):
    pol = create_pol_vector(list)
    subj = create_subj_vector(list)
    df = {'Text':list, 'Polarity':pol,'Subjectivity':subj}
    df = pd.DataFrame(df)
    return df

df = create_sentiment_df(tweets_list) # create df

#################################################################### VISUALIZATIONS #################################################################################
### 1. wordList to wordcloud
def create_cloud(list):
    text = ' '.join(list) # joins words with whiteSpace as delimiter.
    cloud = WordCloud(width = 3000, height = 2000,random_state = 1, colormap='Set2', collocations=False, background_color = 'black',min_font_size = 10).generate(text)
    plt.imshow(cloud,interpolation='bilinear')
    plt.title("Word Cloud Showing Top Mentioned Words in Tweets Mentioning Covid in the Philippines",fontsize = 15,wrap = True)
    plt.axis('off')
    plt.tight_layout(pad = 0) 
    plt.show()

### add count values for df. this function is used by create_pie(df)
def binary_sentiment(df):
    df['P'] = 0
    df['S'] = 0
    df['Count'] = 1
    for i in range(0,len(df['Text'])):
        if (df['Polarity'][i] < 0):
            df['P'][i] = 'nP'
        else:
            df['P'][i] = 'P'
        if (df['Subjectivity'][i] < 0.5):
            df['S'][i] = 'nS'
        else:
            df['S'][i] = 'S'
    new_df = pd.DataFrame({'P': df['P'], 'S': df['S'], 'Count': df['Count']})
    return new_df

### generate pie chart graphics
def create_pie(df):
    z = binary_sentiment(df) # summarizes frequency
    x = z.groupby(['P']).sum() # group data 
    fig = plt.figure()  # setup fig canvas
    ax1 = fig.add_subplot(211) # first frame
    z.groupby(['P']).sum().plot(y = 'Count', kind = 'pie', ax = ax1, shadow = True, autopct = '%.0f%%', labels = ['Negative Sentiment','Positive Sentiment'], explode = (0,0.2),radius = 0.7, colors = ['#ff9999','#66b3ff'])
    plt.legend(loc = 'lower left')
    plt.title("Share of Negative and Positive Sentiment Tweets Mentioning Covid (in Manila)",fontsize = 12,wrap = True, loc = 'center')
    plt.ylabel("")
    ax2 = fig.add_subplot(212) # second frame
    z.groupby(['S']).sum().plot(y = 'Count', kind = 'pie', ax = ax2, shadow = True, autopct = '%.0f%%', labels = ['Subjective','Objective'], explode = (0,0.2), radius = 0.7, colors = ['#99ff99','#ffcc99'])
    plt.legend(loc = 'lower right')
    plt.title("Share of Subjective and Objective Tweets Mentioning Covid (in Manila)", fontsize = 12, wrap = True, loc = 'center')
    plt.ylabel("")
    plt.show()

### generate regression line in a scatter plot
def create_regression(df):
    # plotting the actual points as scatter plot
    x = df['Subjectivity']
    y = df['Polarity']
    plt.scatter(x, y, color = "m",
               marker = "o", s = 20)

    m, b = np.polyfit(x, y, 1) # uses numpy for best-fit
    plt.plot(x, m*x + b) # plot line
    plt.title("Linear Regression Showing the Relationship Between Subjectivity and Sentiment of Tweets")
    plt.text(0.05, 0.6, 'y = ' + '{:.3f}'.format(b) + ' + {:.3f}'.format(m) + 'x', size=14)
    plt.xlabel("Subjectivity", size=14)
    plt.ylabel("Sentiment", size=14)
    plt.show()

############################################################## Graphing Commands #############################################################################
# uncomment lines below to produce graphics
# create_pie(df)
# create_cloud(tweets_list)
# create_regression(df)

