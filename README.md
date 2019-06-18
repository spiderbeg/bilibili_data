# 2019年六月前哔哩哔哩视频数据分析
## 项目内容
* 抓取哔哩哔哩2016年至今视频发布数、2019年六月前哔哩哔哩**播放量1万**以上视频数据、及视频播放量超 **50w 作者信息**、以及抓取视频中播放量**前 1w** 的视频弹幕及热评。
* 使用**标签**对播放数、收藏数、评论数、弹幕数、时长分析；及对视频发布数和作者粉丝数、视频播放量；弹幕及热评分别进行绘图定量分析，如下。
  1. 哔哩哔哩全站2016至今每月各分类下视频发布数量；
  2. 播放量过 1w 视频信息抓取，包括发布时间、播放数、收藏数、时长、评论数、弹幕数；
  3. 科技类下播放量过 1w 视频各指标分析（同第2条）；
  4. 抓取到播放数超 50w 作者信息抓取，包含作者粉丝数、发布视频数量、总播放数；
  5. 播放量前 1w 视频弹幕及热评分词分析。
## 项目思路
1. 使用哔哩哔哩视频、作者信息、弹幕、热评 api 接口进行数据抓取，并使用 **MongoDB** 存储；
2. 分析哔哩哔哩全站视频发布量月变化、及作者视频播放数、粉丝数；及视频播放数、收藏数、评论数等靠前的“最热”标签。
## 运行环境
* python3.7
* Windows
* jupyter notebook
## 运行依赖包
* requests
* matplotlib
* numpy
* pymongo
* pickle
* jieba
* wordcloud
## 文件说明
### spider_code 文件夹
* 抓取的2019年六月前哔哩哔哩播放数1万以上视频信息代码;
* 抓取的2019年六月前哔哩哔哩播放数前1万视频弹幕及热评代码;
* 抓取哔哩哔哩2016年至今每月各分类视频发布数代码；
* 抓取已抓取的播放数超 50w 视频的作者信息代码；
* 抓取 video 详细信息，以便获取获得弹幕的 cid 代码。
### picture_code 文件夹
本项目需大量使用 matplotlib 绘图，因此绘图部分使用 jupyter notebook，**blblneaten.ipynb** 中包含生成 picture 文件夹中图片的所有代码。此处强烈推荐使用 jupyter notebook 进行数据分析，方便快捷；
### picture 文件夹
按照发布量、标签、作者、弹幕及热评分类放置相关的**图像**。
* Total：视频播放量分布图、视频各月发布量条形图、按时间变化折线图形、分阶段视频数与作者数之比；
* Tags：视频播放数 1w 以上及 10w 以上按标签对视频播放数、评论数、弹幕数、收藏数、时长分析的条形图；
* Author：作者粉丝数及平均播放数条形图；
* Technology：科技类下视频发布量及按标签分析图；
* Danmaku_hots: 弹幕词云及热评分词条形图;
* Analyze: 对全站及科技类视频发布从小时、星期、数量等方面分别进行对比分析;以及全站视频发布与弹幕发布时间的分析。
### pickle_file 文件夹
为方便绘图，部分数据在本项目使用序列化数据存储变量，pickle_file 文件夹放置本代码所需的序列化文件及部分 jieba 分词所需的文件。
## 一些建议
* 爬取时大部分数据为 json 格式，推荐使用 MongoDB 存储数据;
* 绘图库使用 matplotlib，官方示例<https://matplotlib.org/>；
* 对于经常使用的较大的变量可以使用 pickle 序列化。
## 部分图片展示（更多图片见 picture 文件夹）
* 哔哩哔哩2016年至今每月各分类视频发布条形图
![publish](picture/total/pub_total.png)<br>
* 哔哩哔哩2016年至今每天视频发布变化图
![publish](picture/total/send.png)<br>
* 哔哩哔哩2019年6月前视频星期发布变化图
![publish](picture/total/total_week.png)<br>
* 哔哩哔哩2019年6月前视频小时发布变化图
![publish](picture/total/hour_total.png)<br>
* 哔哩哔哩2019年6月前视频标签出现次数前100条形图
![publish](picture/tags/1_tag_counts.png)<br>
* 哔哩哔哩2019年6月前视频标签平均播放前100条形图
![publish](picture/tags/1_tag_mean.png)<br>
* 哔哩哔哩2016年至今播放数前 1w 视频弹幕词云
![publish](picture/Danmaku_hots/danmaku.png)<br>
* 哔哩哔哩2019年6月前科技类视频各月发布图
![publish](picture/technology/tech_pubcount_1.png)<br>
* 哔哩哔哩2019年6月前科技类视频星期发布变化图
![publish](picture/technology/tech_week.png)<br>
* 哔哩哔哩2019年6月前科技类视频小时发布变化图
![publish](picture/technology/tech_hour.png)<br>
