from .xclient import client
from common.log import logger


import pandas as pd
import tweepy


def post_tweet(text):
    try:
        response = client.create_tweet(text=text)
        print(f"推文发布成功！推文 ID: {response.data['id']}")
        return response.data
    except tweepy.TweepyException as e:
        print(f"发布推文失败: {e}")
        return None

# This Tweet was Tweeted using Tweepy and Twitter API v2!
def create_tweet(text: str):
    # Create Tweet

    # The app and the corresponding credentials must have the Write permission

    # Check the App permissions section of the Settings tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps

    # Make sure to reauthorize your app / regenerate your access token and secret
    # after setting the Write permission

    # Example 1: Create a regular Tweet
    response = client.create_tweet(
        text=text
    )
    logger.info(f"[x_tweet] text={text}")
    logger.info(f"[x_tweet] response={response}")

    print(f"https://twitter.com/user/status/{response.data['id']}")

    # Example 2: Create a Tweet in a Community
    # Note: The authenticated user must be a member of the Community
    # response = client.create_tweet(
    #     text="This Tweet was posted in a Community using Tweepy and Twitter API v2!",
    #     community_id="INSERT_COMMUNITY_ID_HERE"
    # )
    # print(f"https://twitter.com/user/status/{response.data['id']}")


def search_popular_tweets(query, max_results=100):
    tweets = client.search_recent_tweets(
        query=query,
        tweet_fields=["public_metrics", "created_at", "author_id"],
        max_results=max_results
    )
    return tweets.data


# 推荐热门推文
def recommend_tweets(tweets, top_n=5):
    # 提取推文数据
    tweet_data = []
    for tweet in tweets:
        metrics = tweet.public_metrics
        tweet_data.append({
            "id": tweet.id,
            "text": tweet.text,
            "author_id": tweet.author_id,
            "likes": metrics["like_count"],
            "retweets": metrics["retweet_count"],
            "created_at": tweet.created_at,
            "score": metrics["like_count"] + metrics["retweet_count"] * 2  # 转发权重更高
        })

    # 转换为 DataFrame 并排序
    df = pd.DataFrame(tweet_data)
    top_tweets = df.sort_values(by="score", ascending=False).head(top_n)
    return top_tweets