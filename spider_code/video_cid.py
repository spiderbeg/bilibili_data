# -*- coding: utf-8 -*-
# 根据之前抓取数据进行播放数排名，根据 aid 获取 video detail 信息--获取cid
import pymongo
import requests
import time
import random

def get_ready(ch='video_info',dbname='blbl'):
    '''数据库调用'''
    global mycol, myclient, mydetail
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    mycol = mydb[ch]
    mydetail = mydb['video_detail']
get_ready()

plays = mycol.find({}) # 视频信息
details = mydetail.find({}) # 视频详细信息
print( mycol.count_documents({}))
playid,detailid = {},{}
for index,d in enumerate(details): # 视频详细信息列表
    if d['data']['aid'] not in detailid:
        detailid[d['data']['aid']] = d['data']['pages'][0]['cid']
    else:
        mydetail.delete_one(d)
for i,j in enumerate(plays): # 生成id
    if j['title'] not in playid:
        playid[j['id']] = int(j['rank_score'])
    else:
        print(j)
# print(len(detailid),index)        
play2 = sorted(playid.items(), key=lambda item:item[1], reverse=True) # 视频播放数排序
headers = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
# goaway = [52808146, 41612018, 39724421, 42343350, 39761467, 41876084, 40885499, 52800820, 42719731, 52963838, 43918291, 44054574, 45788042, 50750382, 52304549, 44637609, 47875674, 42176880, 42048751, 40645915, 52980002, 53240034, 44821140, 41571291, 40371421, 50350367, 48785512, 40333177, 40354715, 52032531, 44412590, 41875851, 47874239, 52643987, 42706131, 48515618, 43247037, 43281886, 48635612, 48452254, 44910848, 49410299, 43586960, 40234429, 52190969, 50149106, 50637510, 40930325, 45574781, 39819450, 52953973, 45496726, 41994245, 47848029, 44173949, 39619591]
goaway = []
for i,play3 in enumerate(play2[:10000]):
    if i<2:
        aid = play3[0] # 视频id
        if aid not in detailid and aid not in goaway:
            url = 'https://api.bilibili.com/x/web-interface/view?aid=' + str(aid)
            r = requests.get(url, headers=headers)  # 数据抓取
            t = random.randint(1,3)
            time.sleep(t)
            r2 = r.json()
            try:
                print(r2['data']['aid'],r2['data']['pages'][0]['cid'], ' ',end='')
                mydetail.insert_one(r2)
            except:
                goaway.append(aid)
                print('page', i, r2, aid)
print(goaway)