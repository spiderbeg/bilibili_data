# -*- coding: utf-8 -*-
# 视频播放数大于50w的作者数据抓取

import requests
import time
import pymongo
import random
def get_ready(ch='video_info',dbname='blbl'):
    '''数据库调用'''
    global mycol, myclient,mya
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    mycol = mydb[ch]
    mya = mydb['author']
get_ready()
results = mycol.find({}) # video_info 中读取数据
headers = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
bb = []
for i,v in enumerate(results):
    if i >= 0:
        if v['play'] == '--':
            continue
        if v['mid'] not in bb and int(v['play']) > 500000:
            bb.append(v['mid']) # 不重复的列表,去重作者
            print('顺序是：',i,'id是',v['mid'],end='')
            urlu = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(v['mid']) 
            r1 = requests.get(urlu, headers=headers) # 作者信息
            r12 = r1.json()

            urlu2 = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(v['mid'])
            r2 = requests.get(urlu2, headers=headers) # following 关注，follower，粉丝
            r22 = r2.json()

            urlu3 = 'https://api.bilibili.com/x/space/upstat?mid=' + str(v['mid'])
            r3 = requests.get(urlu3, headers=headers) # archive 播放数，article 阅读数 
            r32 = r3.json()

            dic = dict(dict(r12['data']), **dict(r22['data']), **dict(r32['data'])) # 字典合并
            if mya.find_one({'mid': dic['mid']}): # 
                print('exist',end='')
            else:
                mya.insert_one(dic) # 插入数据库表 author
                print('ok！',end='')