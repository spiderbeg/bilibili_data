# -*- coding: utf-8 -*-
# 播放数排名前一万，--热评信息
import pymongo
import requests
import time
import random

def get_ready(ch='video_detail',dbname='blbl'):
    '''数据库调用'''
    global mycol, myclient, mypl
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    mycol = mydb[ch]
    mypl = mydb['bl_hotcomment']
get_ready()
cid = mycol.find({}) 
rank = {}
for a in cid:
    rank[a['data']['aid']] = a['data']['stat']['view']
ranks = sorted(rank.items(), key=lambda item:item[1], reverse=True) # 播放量排序 

headers = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
for i,j in enumerate(ranks[:10000]):
    if i >= 0:
        print('视频', i, j[0], j[1], end='')
        url = 'https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=' + str(j[0])
        r = requests.get(url, headers=headers)
        time.sleep(1)
        r = r.json()
        if r['message'] == '禁止评论':
            print('禁止评论')
            continue
        else:
            if r['data']['hots'] == None:
                print('没有热评')
                continue
            for co in r['data']['hots']: # 一个页面中的评论
                mypl.insert_one(dict(co))
        print('ok')