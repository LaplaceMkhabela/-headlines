import feedparser
from flask import Flask

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
    first_article = feed["entries"][0]

    return """
                <html>
                    <body>
                        <h1>{3} Headlines</h1>
                        <h2>{0}</h2>
                        <em>{1}</em>
                        <p>{2}</p>
                        <a href="/">Read More</a>
                    </body>
                </html>
            """.format(first_article.get("title"),first_article.get("published"),first_article.get("summary"),publication)

if __name__ == "__main__":
    app.run(debug = True)