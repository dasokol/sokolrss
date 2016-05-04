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
	    <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>RSS Feed</title>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <link rel="icon" type="image/png" href="https://cdn2.iconfinder.com/data/icons/web2/Icons/Feed_512x512.png">
	    <script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  	        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  	        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  	        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	        ga('create', 'UA-68962940-2', 'auto'); ga('send', 'pageview');
	    </script>
	    <!-- Latest compiled and minified CSS -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	    <!-- jQuery library -->
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	    <!-- Latest compiled JavaScript -->
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
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
    ''' %(title, description[:-253], sports[0], sports[1], sports[2], sports[3], sports[4], sports[5], sports[6], sports[7],
          news[0], news[1], news[2], news[3], news[4], news[5], news[6], news[7], news[8], news[9], news[10], news[11],
          news[12], news[13], news[14], history[0], history[1])
    return html
