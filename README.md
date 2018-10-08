# 豆瓣电影爬虫

使用Scrapy框架的豆瓣爬虫



## 项目介绍

[豆瓣选影视页面](https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1)分别筛选地区为中国大陆、香港、台湾（可更换为其他地区），构造Ajax请求，获取电影id，再通过id构造电影链接，解析页面后获得电影详细数据，如名称、年份、导演、主演、类型等。具体可见我的博文：[爬虫实战（一）——利用scrapy爬取豆瓣华语电影](https://yeungsk.github.io/2018/10/08/%E7%88%AC%E8%99%AB%E5%AE%9E%E6%88%98(%E4%B8%80)%E5%88%A9%E7%94%A8scrapy%E7%88%AC%E5%8F%96%E8%B1%86%E7%93%A3%E5%8D%8E%E8%AF%AD%E7%94%B5%E5%BD%B1/)。



## 安装

### 安装Python

至少Python3.5以上

### 安装Redis和Mongo

安装好之后将Redis和Mongo服务开启

### 安装依赖

```
pip3 install -r requirements.txt
```



## 运行

### 配置代理池

```bash
cd proxypool
```

进入proxypool目录，修改settings.py文件

PASSWORD为Redis密码，如果为空，则设置为None

目前默认的代理为免费代理，如需添加代理，请在crawler.py的Crawler下添加以crawl_开头的函数。

### 打开代理池和API

```bash
cd proxypool
python3 run.py
```

### 运行scrapy

```
cd douban
python3 run.py
```



## 获取结果

电影数据存储在MongoDB中名为douban数据库的film表中，数据结果如下：

```json
{
    "_id" : ObjectId("5bb96351fd21815bdbe90124"),
    "id" : "24719063",
    "title" : "烈日灼心",
    "year" : "2015",
    "region" : [ "中国大陆"],
    "language" : [ "汉语普通话"],
    "director" : [ "曹保平"],
    "type" : [ "剧情", "悬疑", "犯罪"],
    "actor" : [ "邓超", "段奕宏", "郭涛", "王珞丹", "吕颂贤", "高虎", "白柳汐", "杜志国"],
    "date" : [ "2015-08-27(中国大陆)", "2015-06-15(上海电影节)"],
    "runtime" : [ "139分钟"],
    "rate" : "7.9",
    "rating_num" : "290209"
}
```

