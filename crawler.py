import twint

c = twint.Config()

# c.Username = "unicef" # verified twitter handle of UNICEF PHILIPPINES
c.Search = "covid" # topic
c.Limit = 1000      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Output = "/Users/aldrin/Desktop/tweet/un.csv"     # path to csv file
c.Near = "Manila"
c.Debug = True

#c.Until = "2021-12-31"
#c.Verified = True
#c.Min_replies = 1


# Run
twint.run.Search(c)