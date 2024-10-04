import feedparser
from flask import Flask,render_template

app = Flask(__name__)

RSS_FEED = {
    "bbc":"http://feeds.bbci.co.uk/news/rss.xml",
    "cnn":'http://rss.cnn.com/rss/edition.rss',
    "fox": 'http://feeds.foxnews.com/foxnews/latest',
    "iol": 'http://www.iol.co.za/cmlink/1.640',
}

@app.route("/")
def index():
    return "Home"

@app.route("/<publication>")
def get_news(publication = "bbc"):
    feed = feedparser.parse(RSS_FEED[publication])
    articles = feed["entries"][0]

    return render_template("index.html",title=articles.get("title"),published=articles.get("published"),summary=articles.get("summary"))

if __name__ == "__main__":
    app.run(debug = True)