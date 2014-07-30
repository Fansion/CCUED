source dict:
sentiment
- 正面评价词语（中文）.txt 中文正面评价词语  3730
- 正面情感词语（中文）.txt 中文正面情感词语	 836

- 负面评价词语（中文）.txt 中文负面评价词语  3116
- 负面情感词语（中文）.txt 中文负面情感词语	 1254

taiwan
- NTUSD_positive_simplified.txt  2810
- NTUSD_negative_simplified.txt  8276

extend emtion dict

most.txt
程度级别词语（中文）.txt  “极其|extreme / 最|most”  69

more.txt
程度级别词语（中文）.txt  “较|more” 37
add 比较

very.txt
程度级别词语（中文）.txt  “很|very” 42

ish.txt
程度级别词语（中文）.txt  “稍|-ish” 29

over.txt
程度级别词语（中文）.txt “超|over” 30

insufficiently.txt
程度级别词语（中文）.txt  “欠|insufficiently” 12


算法：

考虑多个程度词的连乘效应。
如："非常不流畅"
"流畅"属于posdict, 考虑"流畅"之前的词，"非常"取1×4=4, "不"取4*-1=-4
所以最终虽然"流畅"属于posdict,但此处归于negScore, negScore += 4

分句尾的感叹号对句子正负分值的考虑 感叹号之前 整个句子单词的分值，如果posScore > 
negScore则posScore += 2, 否则negScore += 2
