__author__ = 'david_000'
import feedparser

def getWeather():
    weatherData = feedparser.parse('https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid=12778800&format=json')
    return weatherData
    #return weatherData.entries[0].title, weatherData.entries[0].description

def getSports():
    tigersData = feedparser.parse('https://sports.yahoo.com/mlb/teams/det/rss.xml')
    redWingsData = feedparser.parse('https://sports.yahoo.com/nhl/teams/det/rss.xml')
    lionsData = feedparser.parse('https://sports.yahoo.com/nfl/teams/det/rss.xml')
    pistonsData = feedparser.parse('https://sports.yahoo.com/nba/teams/det/rss.xml')

    return tigersData.entries[0].link, tigersData.entries[0].title,\
           redWingsData.entries[0].link, redWingsData.entries[0].title,\
           lionsData.entries[0].link, lionsData.entries[0].title, \
           pistonsData.entries[0].link, pistonsData.entries[0].title


def getNews():
    newsData = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')
    return newsData.entries[0].link, newsData.entries[0].title, newsData.entries[0].description,\
           newsData.entries[1].link, newsData.entries[1].title, newsData.entries[1].description, \
           newsData.entries[2].link, newsData.entries[2].title, newsData.entries[2].description,\
           newsData.entries[3].link, newsData.entries[3].title, newsData.entries[3].description,\
           newsData.entries[4].link, newsData.entries[4].title, newsData.entries[4].description

def getHistory():
    historyData = feedparser.parse('http://www.history.com/this-day-in-history/rss')
    return historyData.feed.link, historyData.entries[0].title
