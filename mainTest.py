#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test file'

__author__ = 'Frank Fu'

import main

# "皇明太阳能股份有限公司火热招商进行中我公司为扩大在枣阳市的市场网络覆盖，先在枣阳市里招直销总代理一名，各个乡镇，办事处等招分销商各一家。我们皇明公司无论行业发展方向，还是产品的质量售后服http://t.cn/agtlL0"
def getTextDataTest():
	dataList = main.getTextData('sina_user_weibos_1386599408.csv')
	print dataList[0].encode('utf-8')

def getDataListSql():
	# SELECT `text` FROM `sina_user_weibos_1386599408` WHERE text not like '%转发%' and text not like '%微博客户%' and text not like '%@%' and id > 1 and id < 5000 and text not like '%#%' 
	pass

# 今天终于和交行脱离关系了
# 你们的服务态度值得肯定
# 但是没法儿
# 我这个人就是不待见罗嗦和繁琐
# PS:销卡的时候还倒贴了9块4毛6的卡费
# 存款都存成负数了
# 惭愧
# 多亏这是张借记卡
# 信用卡还了得
# 
# 音响到底怎么了
# 应该给个交代吧
def getSentencesTest():
	# data = '今天终于和交行脱离关系了。你们的服务态度值得肯定，但是没法儿，我这个人就是不待见罗嗦和繁琐。PS:销卡的时候还倒贴了9块4毛6的卡费，存款都存成负数了，惭愧。多亏这是张借记卡，信用卡还了得。'
	data = '# 音响到底怎么了？应该给个交代吧？'
	for sentence in main.getSentences(data.decode('utf-8')):
		print sentence.encode('utf-8')

# 操作
# 也
# 非常
# 流畅
# ！
def getWordListTest():
	data = '操作也非常流畅！'
	for word in main.getWordList(data):
		print word.encode('utf-8')
# 4.0
# -1
def considerSentimentLevelTest():
	datalist = ['非常', '不']
   	dlist = []
   	for data in datalist:
   		dlist.append(data.decode('utf-8'))
   	for word in dlist:
   		print main.considerSentimentLevel(word, 1)

# for w in wordList[wordIndex::-1]:
#     if w in posdict:
#         posScore += 2
#         break
#     elif w in negdict:
#         negScore += 2
#         break
def getSingleSentenceScoreTest():
	data = '非常不流畅！!'
	print main.getSingleSentenceScore(data)

# [[1, 0], [2, 0], [0, 1], [-1, 1], [0, 1.0], [0, 1], [0, 1], [1, 0], [0, 0]]
def getAllSentencesScoreTest():
	# data = '今天终于和交行脱离关系了。你们的服务态度值得肯定，但是没法儿，我这个人就是不待见罗嗦和繁琐。PS:销卡的时候还倒贴了9块4毛6的卡费，存款都存成负数了，惭愧。多亏这是张借记卡，信用卡还了得。'
	data = '今天是怎么了…先是新疆爆炸，然后宜宾自焚，然后上海飞乌市航班因威胁信息迫降…然后兰州火车站发现炸弹…随后泰国军方宣布控制政府…现在是朝鲜向韩军巡逻舰开炮……[晕]'
	print main.getAllSentencesScore(data.decode('utf-8'))

#[[3.0, 5.0, 0.33333333333333331, 0.55555555555555558, 0.81649658092772603, 0.4969039949999533]]
def statisticalProcessTest():
	print main.statisticalProcess([[[1, 0], [2, 0], [0, 1], [-1, 1], [0, 1.0], [0, 1], [0, 1], [1, 0], [0, 0]]])

#[[3.0, 5.0, 0.75, 1.25, 0.4330127018922193, 1.6393596310755001], [9.0, 5.0, 1.0, 0.55555555555555558, 2.5385910352879693, 0.4969039949999533], [0, 0, 0.0, 0.0, 0.0, 0.0]]
def getScoreTest():
	datalist = ['这手机的画面极好，操作也比较流畅。不过拍照真的太烂了！系统也不好。',
    '今天终于和交行脱离关系了。你们的服务态度值得肯定!!!但是没法儿，  ,,    我这个人就是不待见罗嗦和繁琐。PS:销卡的时候还倒贴了9块4毛6的卡费，存款都存成负数了，惭愧。多亏这是张借记卡，信用卡还了得..。',
    '我来到北京清华大学']
   	dlist = []
   	for data in datalist:
   		dlist.append(data.decode('utf-8')) 
	print main.getScore(dlist)

def writeScoreIntoFileTest():
	scoreList = [[3.0, 5.0, 0.75, 1.25, 0.4330127018922193, 1.6393596310755001], [9.0, 5.0, 1.0, 0.55555555555555558, 2.5385910352879693, 0.4969039949999533], [0, 0, 0.0, 0.0, 0.0, 0.0]]
	main.writeScoreIntoFile(scoreList, 'test.txt')

def getScoreFileTest():
	datalist = ['这手机的画面极好，操作也比较流畅。不过拍照真的太烂了！系统也不好。',
    '今天终于和交行脱离关系了。你们的服务态度值得肯定!!!但是没法儿，  ,,    我这个人就是不待见罗嗦和繁琐。PS:销卡的时候还倒贴了9块4毛6的卡费，存款都存成负数了，惭愧。多亏这是张借记卡，信用卡还了得..。',
    '我来到北京清华大学']
   	dlist = []
   	for data in datalist:
   		dlist.append(data.decode('utf-8'))
   	main.getScoreFile(dlist, 'score.txt')

def mTest():
	# Load dataList
	dataList = main.getTextData('datalist.txt')
	print main.getScore(dataList)


# getTextDataTest()
# getSentencesTest()
# getWordListTest()
# considerSentimentLevelTest()
# getSingleSentenceScoreTest()
getAllSentencesScoreTest()
# statisticalProcessTest()
# getScoreTest()
# writeScoreIntoFileTest()
# getScoreFileTest()
# mTest()