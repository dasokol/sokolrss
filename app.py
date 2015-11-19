from flask import Flask
from flask import render_template, request
from dataParser import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def loadPage():
    weather = getWeather()
    title = weather[0]
    description = weather[1]

    sports = getSports()
    #date = getSports[0]

    news = getNews()

    history = getHistory()


    '''
    f = open('index.html', 'r')
    return f.read()
    '''
    html = '''
    <!DOCTYPE html>
    <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title>RSS Feed</title>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <link rel="icon" type="image/png" href="https://cdn2.iconfinder.com/data/icons/web2/Icons/Feed_512x512.png">
        </head>
        <body>
            <h1>Hello, David</h1>
            <h3>%s:</h3>
            <p>%s</p>
            <h3>Tigers</h3>
            <a href="%s">%s</a>
            <h3>Red Wings</h3>
            <a href="%s">%s</a>
            <h3>Lions</h3>
            <a href="%s">%s</a>
            <h3>Pistons</h3>
            <a href="%s">%s</a>
            <h3>NPR News</h3>
            <a href="%s">%s</a>
            <p>%s</p><br>
            <a href="%s">%s</a>
            <p>%s</p><br>
            <a href="%s">%s</a>
            <p>%s</p><br>
            <a href="%s">%s</a>
            <p>%s</p><br>
            <a href="%s">%s</a>
            <p>%s</p>
            <h3>On this day in history:</h3>
            <a href="%s">%s</p><br>
        </body>
    </html>
    ''' %(title, description, sports[0], sports[1], sports[2], sports[3], sports[4], sports[5], sports[6], sports[7],
          news[0], news[1], news[2], news[3], news[4], news[5], news[6], news[7], news[8], news[9], news[10], news[11],
          news[12], news[13], news[14], history[0], history[1])
    return html
