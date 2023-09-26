from flask import Flask, render_template

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/top5")
def fave():
    artists = ["Lizzo", "Billie Eilish", "The Weeknd", "Post Malone", "SZA"]
    return render_template("fave5.html", artists=artists)