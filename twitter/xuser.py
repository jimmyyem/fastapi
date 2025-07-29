from .xclient import client
from common.log import logger


import pandas as pd
import tweepy

def get_me():
    try:
        response = client.get_me()
        logger.info(f"[xuser] response={response}")
        return response.data
    except tweepy.TweepyException as e:
        print(f"获取个人信息失败: {e}")
        return None