# -*- coding: utf-8 -*-
# 1w 以上 video 数据抓取 
# 包括：标签、播放量、收藏数、评论数、弹幕数、视频时长、up 主 id

import requests
import time
import pymongo
import random
def get_ready(ch='video_info',dbname='blbl'):
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

bilibili = [('145', '欧美电影'), ('86', '特摄'), ('37', '人文-历史'), ('178', '科学-探索-自然'), ('179', '军事'), ('180', '社会-美食-旅行'), ('147', '华语电影'), ('157', '美妆'), ('158', '服饰'), ('164', '健身'), ('159', 'T台'), ('192', '风尚标'), ('166', '广告'), ('71', '综艺'), ('137', '明星'), ('131', 'Korea相关'), ('182', '影视杂谈'), ('183', '影视剪辑'), ('85', '短片'), ('184', '预告-资讯'), ('162', '绘画'), ('163', '运动'), ('174', '其他'), ('22', '鬼畜调教'), ('26', '音MAD'), ('126', '人力VOCALVID'), ('127', '教程演示'), ('76', '美食圈'), ('75', '动物圈'), ('161', '手工'), ('21', '日常'), ('96', '星海'), ('98', '机械'), ('176', '汽车'), ('95', '手机平板'), ('189', '电脑装机'), ('190', '摄影摄像'), ('191', '影音智能'), ('138', '搞笑'), ('65', '网络游戏'), ('173', '桌游棋牌'), ('121', 'GMV'), ('136', '音游'), ('19', 'Mugen'), ('124', '趣味科普人文'), ('122', '野生技术协会'), ('39', '演讲-公开课'), ('171', '电子竞技'), ('172', '手机游戏'), ('17', '单机游戏'), ('27', '综合'), ('33', '连载动画'), ('32', '完结动画'), ('51', '资讯'), ('152', '官方延伸'), ('153', '国产动画'), ('168', '国产原创相关'), ('169', '布袋戏'), ('195', '动态漫-广播剧'), ('170', '资讯'), ('28', '原创音乐'), ('31', '翻唱'), ('30', 'VOCALVID-UTAU'), ('194', '电音'), ('59', '演奏'), ('193', 'MV'), ('29', '音乐现场'), ('130', '音乐综合'), ('20', '宅舞'), ('154', '三次元舞蹈'), ('156', '舞蹈教程'), ('47', '短片-手书-配音'), ('25', 'MMD-3D'), ('24', 'MAD-AMV'),('146', '日本电影'), ('83', '其他国家'), ('185', '国产剧'), ('187', '海外剧')]

get_ready() # 数据库调用

for rid in bilibili: # 分类
    print(rid, end='')
    paras = ['time_from=20190101&time_to=20190131', 'time_from=20190201&time_to=20190228','time_from=20190301&time_to=20190331', 'time_from=20190401&time_to=20190430', 'time_from=20190501&time_to=20190524']
#     if rid[0] == '157': # 出错继续 月份控制
#         paras = ['time_from=20190501&time_to=20190524']
    for para in paras: # 参数
        page = 1
#         if rid[0] == '157' and para == 'time_from=20190501&time_to=20190524': # 出错继续 页数控制
#             page = 31
        status = True
        while status: # 页数
            url = 'https://s.search.bilibili.com/cate/search?&main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1&cate_id=' + rid[0] + '&page=' + str(page) + '&pagesize=50&jsonp=jsonp&' + para
            r = requests.get(url, headers=headers)
            print('url:', url)
            assert r.status_code == 200 # 判断状态
            results = r.json() # json格式
            if len(results['result']) == 0: # 没有满足条件的结果
                status = False
                break
            for result in results['result']:
                # if page == 1 and rid[0] == '145':
                #     print(result)
                result2 = {} # 初始化字典
                if result['rank_score'] > 10000: # 播放量设置
                    print(result['rank_score'], end='')
                    if mycol.find_one({'id': result['id']}): # 用 video id 判断，不然数据会重复
                        print('exist',end='')
                    else:
                        result2 = dict(result)
                        result2['section'] = rid
                        print(result2)
                        mycol.insert_one(result2)
                        print('ok！',end='')
                else:
                    print('不满足判断条件，插入失败')
                    status = False
                    break
            page += 1