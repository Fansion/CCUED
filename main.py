#!/usr/bin/env python
# -*- coding: utf-8 -*-

'ClassifyCorpusUsingEmotionalDictionary'

__author__ = 'Frank Fu'

import numpy as np
import re
import jieba.posseg
#Load user dictionary to increse segmentation accuracy
jieba.load_userdict('/usr/local/lib/python2.7/dist-packages/jieba/dict.txt')


def getTextData(filePath):
    lines = file(filePath).readlines()
    lines = ''.join(lines).decode('utf8').split('\n')
    noSamelines = list(set(lines)) #del same line, change data entry order
    noSamelines.sort(key=lines.index) #keep original data entry order
    lines = [line.replace(' ','') for line in lines if line.replace(' ', '')] #del empty line and spaces
    return lines

# Load sentiment dictionary
posdict = getTextData('BasicEmotionDict/posdict.txt')
# print posdict[0].encode('utf-8')
negdict = getTextData('BasicEmotionDict/negdict.txt')

# Load adverbs of degree dictionary
mostdict = getTextData('BasicEmotionDict/most.txt')
verydict = getTextData('BasicEmotionDict/very.txt')
moredict = getTextData('BasicEmotionDict/more.txt')
ishdict = getTextData('BasicEmotionDict/ish.txt')
insufficientdict = getTextData('BasicEmotionDict/insufficiently.txt')
inversedict = getTextData('BasicEmotionDict/inverse.txt')

# Load dataList
dataList = getTextData('sina_user_weibos_1386599408.csv')


def getSentences(data):
    sentences = []
    punctuationList =  ',.!?;~，。！？；～… '.decode('utf8')
    uselessPunctuationList = ',.?;~，。？；～… '.decode('utf8')
    current = 0
    begin = 0
    guardWord = ''
    for word in data:
        if word not in punctuationList:
            if current+2 < len(data):
                guardWord = data[current+2]
        else:
            if guardWord in punctuationList:
                if current+2 < len(data):
                    guardWord = data[current+2]
            else:
                sentences.append(data[begin:current+1].strip(uselessPunctuationList))
                begin = current+1
        current += 1
    if begin < len(data):
        sentences.append(data[begin:].strip(uselessPunctuationList))
    return sentences

def considerSentimentLevel(degreeWord, baseScore):
    # print 'degreeWord', degreeWord.encode('utf-8')
    # print 'in', baseScore
    if degreeWord in mostdict:
        baseScore *= 4.0
    elif degreeWord in verydict:
        baseScore *= 2.0
    elif degreeWord in moredict:
        baseScore *= 1.0
    elif degreeWord in ishdict:
        baseScore *= 0.5
    elif degreeWord in insufficientdict:
        baseScore *= 0.25
    elif degreeWord in inversedict:
        baseScore *= -1
    # print 'out', baseScore
    return baseScore

def getWordList(sentence):    
    gen = jieba.cut(sentence) #jieba.cut(sentence) returns generator, convert to list
    genList = list(gen)
    wordList = []
    for word in genList:
        wordList.append(word)
    return wordList

def getSingleSentenceScore(sentence):
    wordList = getWordList(sentence)    
    posScore = 0
    negScore = 0
    wordIndex = 0
    sentimentWordIndex = 0
    for word in wordList:
        print word.encode('utf-8')
        # count basic sentiment word

        if word in posdict or word in negdict:
            baseScore = 1
            for degreeWord in wordList[sentimentWordIndex:wordIndex]:
                baseScore = considerSentimentLevel(degreeWord, baseScore)
            if word in posdict:  #consider many degree adv words by baseScore
                if baseScore < 0:
                    negScore -= baseScore
                elif baseScore > 0:  
                    posScore += baseScore
            elif word in negdict:
                if baseScore < 0:
                    posScore -= baseScore
                elif baseScore > 0:  
                    negScore += baseScore

        elif word == "！".decode('utf8') or word == "!".decode('utf8'):
            if posScore > negScore:
                posScore += 2 
            elif posScore < negScore:
                negScore += 2
        wordIndex += 1
        print posScore, negScore

    return [posScore, negScore]


def getAllSentencesScore(data):
    sentences = getSentences(data)
    score = []
    for sentence in sentences:
        print sentence.encode('utf-8')
        score.append(getSingleSentenceScore(sentence))
    return score

def statisticalProcess(scoreList):
    newScoreList = []
    for score in scoreList:
        score_array = np.array(score)
        Pos = np.sum(score_array[:,0])
        Neg = np.sum(score_array[:,1])
        AvgPos = np.mean(score_array[:,0])
        AvgNeg = np.mean(score_array[:,1])
        StdPos = np.std(score_array[:,0])
        StdNeg = np.std(score_array[:,1])
        newScoreList.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return newScoreList

def getScore(dataList):
	scoreList = []
	for data in dataList:
		scoreList.append(getAllSentencesScore(data))

	return statisticalProcess(scoreList)

def writeScoreIntoFile(scoreList, filePath):
    outputFile = open(filePath,'w')
    for score in scoreList:
        outputFile.write('%4s %4s %16s %16s %16s %16s \n' % (str(score[0]),str(score[1]), str(score[2]), str(score[3]), str(score[4]), str(score[5])))
    outputFile.close()


def getScoreFile(dataList, filePath):
	score = getScore(dataList)
	writeScoreIntoFile(score, filePath)

if __name__ == '__main__':
	getScoreFile(dataList, 'score.txt')