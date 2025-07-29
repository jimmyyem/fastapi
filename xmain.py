
from twitter.xtweet import post_tweet, search_popular_tweets, recommend_tweets
from twitter.xuser import get_me

texts = """
This Tweet was Tweeted using Tweepy and Twitter API v2.
但是我还是用了这个API，希望能帮到更多人
"""

# 获取个人信息
# me = get_me()
# print(f"me={me}")
# print(me.id, me.name, me.username)

# 发推文
post_tweet(texts)

# # 示例：搜索关于“Python”的热门推文
# query = "Python -is:retweet lang:en"  # 排除转发，仅限英文
# tweets = search_popular_tweets(query, max_results=100)
# top_tweets = recommend_tweets(tweets, top_n=5)
#
# # 打印推荐结果
# for _, tweet in top_tweets.iterrows():
#     print(f"Tweet: {tweet['text']}")
#     print(f"Likes: {tweet['likes']}, Retweets: {tweet['retweets']}, Score: {tweet['score']}")
#     print("---")