# -*- coding: utf-8 -*-
# 2016-2019.5每月各分类视频发布数抓取

import requests
import time
import pymongo
import random

def get_ready(ch='video_pub',dbname='blbl'):
    '''数据库调用'''
    global mycol, myclient
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    mycol = mydb[ch]
    
headers = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
used = []

bilibili = [('121', 'GMV'), ('136', '音游'), ('19', 'Mugen'), ('124', '趣味科普人文'), ('122', '野生技术协会'), ('39', '演讲-公开课'), ('171', '电子竞技'), ('172', '手机游戏'), ('17', '单机游戏'), ('27', '综合'), ('33', '连载动画'), ('32', '完结动画'), ('51', '资讯'), ('152', '官方延伸'), ('153', '国产动画'), ('168', '国产原创相关'), ('169', '布袋戏'), ('195', '动态漫-广播剧'), ('170', '资讯'), ('28', '原创音乐'), ('31', '翻唱'), ('30', 'VOCALVID-UTAU'), ('194', '电音'), ('59', '演奏'), ('193', 'MV'), ('29', '音乐现场'), ('130', '音乐综合'), ('20', '宅舞'), ('154', '三次元舞蹈'), ('156', '舞蹈教程'), ('47', '短片-手书-配音'), ('25', 'MMD-3D'), ('24', 'MAD-AMV'),('146', '日本电影'), ('83', '其他国家'), ('185', '国产剧'), ('187', '海外剧'), ('131', 'Korea相关'), ('182', '影视杂谈'), ('183', '影视剪辑'), ('85', '短片'), ('184', '预告-资讯'), ('162', '绘画'), ('163', '运动'), ('174', '其他'), ('22', '鬼畜调教'), ('26', '音MAD'), ('126', '人力VOCALVID'), ('127', '教程演示'), ('76', '美食圈'), ('75', '动物圈'), ('161', '手工'), ('21', '日常'), ('96', '星海'), ('98', '机械'), ('176', '汽车'), ('95', '手机平板'), ('189', '电脑装机'), ('190', '摄影摄像'), ('191', '影音智能'), ('138', '搞笑'),('65', '网络游戏'), ('173', '桌游棋牌'), ('145', '欧美电影'), ('86', '特摄'), ('37', '人文-历史'), ('178', '科学-探索-自然'), ('179', '军事'), ('180', '社会-美食-旅行'), ('147', '华语电影'), ('157', '美妆'), ('158', '服饰'), ('164', '健身'), ('159', 'T台'), ('192', '风尚标'), ('166', '广告'), ('71', '综艺'), ('137', '明星')]

get_ready() # 数据库调用
s = mycol.find()

for rid in bilibili: # 分类
    print(rid, end='')
    counts = {}
    counts['rid'] = rid[0]
    counts['rname'] = rid[1]
    paras = ['time_from=20160101&time_to=20160131', 'time_from=20160201&time_to=20160228', 'time_from=20160301&time_to=20160331', 'time_from=20160401&time_to=20160430', 'time_from=20160501&time_to=20160531', 'time_from=20160601&time_to=20160630', 'time_from=20160701&time_to=20160731', 'time_from=20160801&time_to=20160831', 'time_from=20160901&time_to=20160930', 'time_from=20161001&time_to=20161031', 'time_from=20161101&time_to=20161130', 'time_from=20161201&time_to=20161231','time_from=20170101&time_to=20170131', 'time_from=20170201&time_to=20170228', 'time_from=20170301&time_to=20170331', 'time_from=20170401&time_to=20170430', 'time_from=20170501&time_to=20170531', 'time_from=20170601&time_to=20170630', 'time_from=20170701&time_to=20170731', 'time_from=20170801&time_to=20170831', 'time_from=20170901&time_to=20170930', 'time_from=20171001&time_to=20171031', 'time_from=20171101&time_to=20171130', 'time_from=20171201&time_to=20171231','time_from=20180101&time_to=20180131', 'time_from=20180201&time_to=20180228','time_from=20180301&time_to=20180331', 'time_from=20180401&time_to=20180430', 'time_from=20180501&time_to=20180531','time_from=20180601&time_to=20180630', 'time_from=20180701&time_to=20180731','time_from=20180801&time_to=20180831', 'time_from=20180901&time_to=20180930', 'time_from=20181001&time_to=20181031','time_from=20181101&time_to=20181130', 'time_from=20181201&time_to=20181231','time_from=20190101&time_to=20190131', 'time_from=20190201&time_to=20190228','time_from=20190301&time_to=20190331', 'time_from=20190401&time_to=20190430', 'time_from=20190501&time_to=20190524']
    for i,para in enumerate(paras):
        url = 'https://s.search.bilibili.com/cate/search?&main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1&cate_id=' + rid[0] + '&page=1&pagesize=50&jsonp=jsonp&' + para
        r = requests.get(url,headers=headers)
        r2 = r.json()
        counts[str(i+1)] = r2['numResults']
    if mycol.find_one({'rid': rid[0]}): # 用 video id 判断
        mycol.update_one(conuts)
        print('exist, update success',end='')
    else:
        mycol.insert_one(counts)
        print('ok！',end='')
    print(counts)