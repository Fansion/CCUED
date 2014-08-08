#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test file'

__author__ = 'Frank Fu'

import main,re

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

	# "无论是视觉、嗅觉还是味觉都超给力的---非著名青岩猪脚，第一口咬下去就已经决定了你会爱上这满足的感觉"
	# 活动不是天天有 双十一 花甲 猪脚 大大优惠 最后三天了 11月11号下午两点恢复原价 加微信fwlx20080808 接受预留 [酷]
	# 喝奶茶 吃花甲的赶脚 你试过没有[嘻嘻]
	# 如果曾经有一个人为了你而等待，不管是三年还是三个月，请不要那样轻率地选择拒绝。这世间的缘分并不像空气那样廉价，再平凡不过的相遇与相识。在亲情以外，没有谁人能够轻易而又不求回报地为一个人付出一段寂寞的等待。即使没有欣喜的结果，也一度温暖过冷若冰霜的心灵。 [互粉]亲爱的朋友送给你们!
	# 错过了，就真的没有机会了！ 我在:http://t.cn/zHDiXgk
	#  要过年了，祝愿天下有情人，互爱互谅，莫为了一时的追求，放弃掉曾经的沧海誓言。爱了就深爱，人都不是完美的。祝福天下恋人幸福！
	#  我还没真正的穿过一次情侣装,我还没和我喜欢的人游过泳,我还没和我喜欢的人做饭,我还没和我喜欢的过情人节,我还没和我喜欢的人撒过娇,我还没和我喜欢的人看日出日落,我还没和我喜欢的人坐旋转木马,我还没和我喜欢的人看电影,我还没和我喜欢的人坐过摩天轮.我青春在哪里,是死了吗?
	#  平时发个QQ信息，从来没有回音。结婚的时候，瞬间成了中国好闺蜜，“谁不来你可千万得来啊……”谄媚的笑声外加这句假的要死台词让人心寒。十年前，我们单纯，我们傻，我们二，我们无话不谈；十年后，我们渐行渐远，有时觉得心里很憋屈，人到底是怎么了，再深的情谊终抵不过时间，这就是成长的代价。
	#  And not talk to suit together derived; And not for, can together; And not able to together will be together forever; And not always together will be happy. 并不是聊得来，就适合在一起；并不是适合，就能够在一起；并不是能够在一起就会永远在一起；也并不是永远在一起了就会幸福的。
	#  其实真的没必要去争执那些不属于你的东西 总会有一天属于你的都会回到你身边 时间会告诉我们 什么才是你值得去拼了命付出拼了命抓紧的东西 总要学会放手那些留不住的 或许当你释怀了放下了 你会发现 真正最美好的事物会到来 所以 亲爱的你 请别总是对自己过不去
	#  总算有一个人不带骂的！部分支持！
	#  总以为 我原本期望的朋友 爱人 感情可以持续很久不会变 但有些东西是自然而然连你自己都不知道变了 那么渺小经不住考验 其实也没必要太在意这些不是吗 接触的人多了 时间久了 什么通通都会变不是吗 我觉的那个能陪我到最后的你 不管怎么样 我会用心对你 爱人也好朋友也罢
	#  手牌无上限[威武]
	#  王立军事件，真不是想象中那么简单，是中央政治斗争的产物，可怜了这么多无知的民众！
	# sen = '总以为 我原本期望的朋友 爱人 感情可以持续很久不会变 但有些东西是自然而然连你自己都不知道变了 那么渺小经不住考验 其实也没必要太在意这些不是吗 接触的人多了 时间久了 什么通通都会变不是吗 我觉的那个能陪我到最后的你 不管怎么样 我会用心对你 爱人也好朋友也罢'
	# sen = re.sub(r"[a-zA-Z0-9_:/\'\"]", "", sen)
	# print main.getAllSentencesScore(sen.decode('utf-8'))
	# l = []
	# l.append(main.getAllSentencesScore(sen.decode('utf-8')))
	# print main.statisticalProcess(l)

	print main.getAllSentencesScore(data.decode('utf-8'))

#[[3.0, 5.0, 0.33333333333333331, 0.55555555555555558, 0.81649658092772603, 0.4969039949999533]]
def statisticalProcessTest():
	print main.statisticalProcess([[[1, 0], [2, 0], [0, 1], [-1, 1], [0, 1.0], [0, 1], [0, 1], [1, 0], [0, 0]]])

#[[3.0, 5.0, 0.75, 1.25, 0.4330127018922193, 1.6393596310755001], [9.0, 5.0, 1.0, 0.55555555555555558, 2.5385910352879693, 0.4969039949999533], [0, 0, 0.0, 0.0, 0.0, 0.0]]
def getScoreTest():
	datalist = ['这手机的画面极好，操作也比较流畅。不过拍照真的太烂了！系统也不好。',
    '今天终于和交行脱离关系了。你们的服务态度值得肯定!!!但是没法儿，  ,,    我这个人就是不待见罗嗦和繁琐。PS:销卡的时候还倒贴了9块4毛6的卡费，存款都存成负数了，惭愧。多亏这是张借记卡，信用卡还了得..。',
    '我来到北京清华大学',"abddef"]
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
# getAllSentencesScoreTest()
# statisticalProcessTest()
getScoreTest()
# writeScoreIntoFileTest()
# getScoreFileTest()
# mTest()