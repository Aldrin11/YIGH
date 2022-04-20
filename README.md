# YIGH

Objectives
========================================================================
To demonstrate competence with data analysis in various technologies 
Python
Stata
APIs: Twint, TextBlob, matplotlib, WordCloud
Data Manipulation: regex, data structures, data cleaning
Git/Github: version control
To showcase ability to learn quickly with learning new technologies

Technologies Used
========================================================================
Web Scrape Twitter using Python and Twint API
Initial Data Cleaning with Stata
Data Wrangling with Python using numpy and pandas packages
Text Analysis with Python using TextBlob API
Data Visualization with Python using matplotlib, WordCloud packages

Summary of Work 
========================================================================
Web Scrape Twitter using Python and Twint API (2hrs)
Learned the fundamentals of webscraping and API integration 
Scraped 1000 tweet data points geotagged in Manila that mentions “covid” with Twint API. 

Initial Data Cleaning with Stata (0.5 hr)
Removed all other data columns aside from unique_id and Text from raw data
Removed data rows with missing values or inconsistent data types 

Data Wrangling with Python using numpy and pandas packages (2hrs)
Decided against pursuing the project in Stata because of limitations in functional integration with Python and Twint
Removed prepositions, @mentions, and hyperlink from text in data
Created filter functions that structured data for visualization

Text Analysis with Python (2hrs)
Learned the fundamentals of Natural Language Processing, and Sentiment Analysis
Learned about common APIs for Sentiment Analysis which included TextBlob.
Integrated TextBlob API and created textual analysis functions 

Data Visualization (1hr)
Learned about optimal graphic styling and implemented design optimizations

Data Visualizations
========================================================================
Graphic highlights how most recent tweets that mention “covid” are both mostly Negative and Objective. Used TextBlob, which is an opensource API from MIT, for the textual sentiment analysis. A limitation of this analysis is that most tweets in the Philippines combine both English and Filipino, which makes it hard for the API to detect the overall language and apply proper analysis.

Word Cloud graphic that shows most used words among the most recent tweets that mentions “covid” in Manila. Words like “DOH”, “cse” (colloquial abbreviation for “blame” in Filipino), “vccine” , “Tguig” stand out as they highlight the very common use of colloquial abbreviations that are likely to escape the detection of text sentiment analysis.

Conclusion
========================================================================
Overwhelming majority of most recent tweets in Manila that mention covid show negative sentiment and objectivity according to the Natural Language Processing Algorithm of TextBlob
This analysis is limited by (1) presence of Filipino words in tweets (2) presence of colloquial abbreviations and language that likely distort the sentiment analysis.

Reflection
========================================================================
While I encountered some hiccups along the way, this mini-project was incredibly fascinating and enjoyable. I loved learning about sentiment analysis and web scraping techniques that I was able to implement in my program. I also thoroughly enjoyed sharpening my data cleaning and analysis skills by managing over 1,000 data entries that were noisy and messy.

Despite the heavy focus on quantitative data analysis, projects like these excite me because I love breaking down complex problems into smaller pieces. Finding new ways to optimize  my code, or make my dataframes more efficient is something that I find incredibly rewarding especially when I get to work on visualizing the results of my analysis as well. 


Documentation
========================================================================
My github page contains all the files needed to recreate this project. 
crawl.py : web crawler that saves data into manila.csv
visualizations.py : program that implements text sentiment analysis, data wrangling, and visualizations
manila.csv : csv file that contains output after initial data cleaning with Stata


