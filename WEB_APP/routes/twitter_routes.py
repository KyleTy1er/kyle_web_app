# web_app/routes/twiiter_routes.py

from flask import Blueprint, jsonify
from web_app.services.twitter_service import api_client
from web_app.models import User, Tweet, db

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name=None):
    api = api_client()
    user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count= 150, exclude_replies=True, include_rts=False)


    breakpoint()
    #store in the database
    db_user = User.query.get(twitter_user.id or User(id=twitter_user.id))

    return jsonify({"user": user._json, "tweets_count": len(statuses)})
