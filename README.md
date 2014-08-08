##Background

Classify corpus to do sentiment analysis using emotional dictionary in python. 

####Input:
A  tweet containing several sentences.
like: "这手机的画面极好，操作也比较流畅。不过拍照真的太烂了！系统也不好。"

####output:
 A list containing six fields(Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg) of the given tweet.
 like:[3.0, 5.0, 0.75, 1.25, 0.4330127018922193, 1.6393596310755001] 

##Files		
####sentiment dictionary source
sentiment

 - 正面评价词语（中文）.txt 中文正面评价词语  3730
 - 正面情感词语（中文）.txt 中文正面情感词语	 836
 - 负面评价词语（中文）.txt 中文负面评价词语  3116
 - 负面情感词语（中文）.txt 中文负面情感词语	 1254

taiwan

 - NTUSD_positive_simplified.txt  2810
 - NTUSD_negative_simplified.txt  8276

####BasicEmotionDict

 - most.txt
程度级别词语（中文）.txt  “极其|extreme / 最|most”  69
 - more.txt
程度级别词语（中文）.txt  “较|more” 37
add 比较
 - very.txt
程度级别词语（中文）.txt  “很|very” 42
 - ish.txt
程度级别词语（中文）.txt  “稍|-ish” 29
 - over.txt
程度级别词语（中文）.txt “超|over” 30
 - insufficiently.txt
程度级别词语（中文）.txt  “欠|insufficiently” 12


##Algorithm Improvements

 - 考虑多个程度词的连乘效应。
如："非常不流畅"
"流畅"属于posdict, 考虑"流畅"之前的词，"非常"取1×4=4, "不"取4*-1=-4
所以最终虽然"流畅"属于posdict,但此处归于negScore, negScore += 4
 - 分句尾的感叹号从该分句正负分值整体考虑，考虑感叹号之前整个分句单词的分值，如果posScore > negScore则posScore += 2, 否则negScore += 2
 - to be continued

##Notes
Refer to [Python 文本挖掘：使用情感词典进行情感分析（算法及程序设计）  ](http://rzcoding.blog.163.com/blog/static/2222810172013101844033170/) and [Azure-rong](https://github.com/Azure-rong/Review-Helpfulness-Prediction/tree/master/main/Feature%20extraction%20module/Sentiment%20features/Sentiment%20dictionary%20features)。