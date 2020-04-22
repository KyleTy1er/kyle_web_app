# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template

from web_app.models import User, Tweet, db
from web_app.services.twitter_service import api_client
from web_app.services.basilica_service import connection as basilica_connection

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name=None):
    
    api = api_client()
    twitter_user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("Status Count:", len(statuses))

    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()

    # STORE TWEETS:

    all_tweet_texts = [status.full_text for status in statuses]
    embeddings = list(basilica_connection.embed_sentences(all_tweet_texts, model="twitter"))
    print("Number of Embeddings:", len(embeddings))

    counter = 0
    for status in statuses:
        print(status.full_text)
        print("----")
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id
        db_tweet.full_text = status.full_text
        embedding = embeddings[counter]
        print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        counter+=1
    db.session.commit()

    return "OK"


@twitter_routes.route("/users")
def ret_users(screen_name=None):
    api = api_client()
    twitter_user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    return render_template('tu.html', db_user=db_user)
    