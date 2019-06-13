# -*- coding: utf-8 -*-
# 播放数排名，--由cid获取弹幕信息 # 9944条
import pymongo
from bs4 import BeautifulSoup
import requests
import time
import random

def get_ready(ch='video_detail',dbname='blbl'):
    '''数据库调用'''
    global mycol, myclient, mydanmu
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    mycol = mydb[ch]
    mydanmu = mydb['b1_danmu']
get_ready()
cid = mycol.find({})
headers = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
for i,j in enumerate(cid):
    if i >= 0:
        print('次数',i,j['data']['pages'][0]['cid'],j['data']['aid'],j['data']['title'],end='')
        url = 'https://comment.bilibili.com/' + str(j['data']['pages'][0]['cid']) +'.xml'
        r = requests.get(url, headers=headers)
        time.sleep(1)
        r.encoding = 'utf8'
        soup = BeautifulSoup(r.text)
        results = soup.find_all('d')
        for result in results:
            danmu = {} # 弹幕信息
            danmu['cid'] = j['data']['pages'][0]['cid']
            danmu['aid'] = j['data']['aid']
            danmu['title'] = j['data']['title']
            danmu['content'] = result.text
            danmu['sendtime'] = result.get('p')
            mydanmu.insert_one(danmu)