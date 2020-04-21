

# web_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Tweetz, parse_records, db
tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    # ]
    tweet_records = Tweetz.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    # ]
    tweet_records = Tweetz.query.all()
    print(tweet_records)
    return render_template("tweets.html", message="Here's some tweets", tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    # INSERT INTO books ...
    new_tweet = Tweetz(text=request.form["text"])
    print(new_tweet)
    db.session.add(new_tweet)
    db.session.commit()
        # return jsonify({
    #     "message": "User Created Successfully ()",
    #     "book": dict(request.form)
    # })
    flash(f"TWEET: '{new_tweet.text}' created successfully!", "success")
    return redirect(f"/tweets")