#!/usr/bin/env python
# -*- coding: utf-8 -*-

'ClassifyCorpusUsingEmotionalDictionary'

__author__ = 'Frank Fu'

import numpy as np
import re
import jieba.posseg
import logging

#Load user dictionary to increse segmentation accuracy
jieba.load_userdict('/usr/local/lib/python2.7/dist-packages/jieba/dict.txt')
logging.basicConfig(level=logging.INFO)

def getTextData(filePath):
    lines = file(filePath).readlines()
    lines = ''.join(lines).decode('utf8').split('\n')
    noSamelines = list(set(lines)) #del same line, change data entry order
    noSamelines.sort(key=lines.index) #keep original data entry order
    lines = [line.replace(' ','') for line in lines if line.replace(' ', '')] #del empty line and spaces
    return lines

pathPrefix = 'BasicEmotionDict/'

logging.info('Begin to retrieve data from files to variables in memory')
logging.info('......')

# Load sentiment dictionary
poswords = getTextData(pathPrefix + 'poswords')
negwords = getTextData(pathPrefix + 'negwords')
neuralwords = getTextData(pathPrefix + 'neuralwords')

# Load adverbs of degree dictionary
mostdict = getTextData(pathPrefix + 'most.txt')
verydict = getTextData(pathPrefix + 'very.txt')
moredict = getTextData(pathPrefix + 'more.txt')
ishdict = getTextData(pathPrefix + 'ish.txt')
insufficientdict = getTextData(pathPrefix + 'insufficiently.txt')
inversedict = getTextData(pathPrefix + 'inverse.txt')

# Load dataList
# dataList = getTextData('sina_user_weibos_1386599408.csv')
dataList = getTextData('weibotest.csv')
logging.info('Finishing retrieving data from files to variables in memory')


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
    outputNeuralwords = open(pathPrefix + 'neuralwords', 'a')
    for word in wordList:
        # print word.encode('utf-8')
        # count basic sentiment word

        if word in poswords or word in negwords:
            baseScore = 1
            # print sentimentWordIndex, wordIndex
            for degreeWord in wordList[sentimentWordIndex:wordIndex]:
                baseScore = considerSentimentLevel(degreeWord, baseScore)
            if word in poswords:  #consider many degree adv words by baseScore
                if baseScore < 0:
                    negScore -= baseScore
                elif baseScore > 0:  
                    posScore += baseScore
            elif word in negwords:
                if baseScore < 0:
                    posScore -= baseScore
                elif baseScore > 0:  
                    negScore += baseScore

        elif word == "！".decode('utf8') or word == "!".decode('utf8'):
            if posScore > negScore:
                posScore += 2 
            elif posScore < negScore:
                negScore += 2

        elif word not in neuralwords:
            outputNeuralwords.write('\n' + word.encode('utf-8'))
        wordIndex += 1
        # print posScore, negScore
    outputNeuralwords.close()

    return [posScore, negScore]

def getAllSentencesScore(data):
    sentences = getSentences(data)
    score = []
    for sentence in sentences:
        # print sentence.encode('utf-8')
        score.append(getSingleSentenceScore(sentence))
    return score

def statisticalProcess(scoreList):
    newScoreList = []
    logging.info('Begin statisticalProcess')
    logging.info('......')
    for score in scoreList:
        score_array = np.array(score)
        Pos = np.sum(score_array[:,0])
        Neg = np.sum(score_array[:,1])
        AvgPos = np.mean(score_array[:,0])
        AvgNeg = np.mean(score_array[:,1])
        StdPos = np.std(score_array[:,0])
        StdNeg = np.std(score_array[:,1])
        newScoreList.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    logging.info('Finish statisticalProcess')
    return newScoreList

def getScore(dataList):
    scoreList = []
    logging.info('Begin to getAllSentencesScore')
    logging.info('......')
    for data in dataList:
        data = re.sub(r"[a-zA-Z0-9_:/\'\"]", " ", data)  #delete words containing char and digit
        scoreList.append(getAllSentencesScore(data))
    logging.info('Finish getAllSentencesScore')

    return statisticalProcess(scoreList)

def writeScoreIntoFile(scoreList, filePath):
    outputFile = open(filePath,'w')
    logging.info('Begin to write data into ' + filePath)
    for score in scoreList:
        outputFile.write('%4s %4s %16s %16s %16s %16s \n' % (str(score[0]),str(score[1]), str(score[2]), str(score[3]), str(score[4]), str(score[5])))
    outputFile.close()
    logging.info('......')
    logging.info('Finish writing data into ' + filePath)


def getScoreFile(dataList, filePath):
    score = getScore(dataList)
    writeScoreIntoFile(score, filePath)

if __name__ == '__main__':
    logging.info('Main function begin!')
    logging.info('-----------------------------')
    getScoreFile(dataList, 'score.txt')
    logging.info('-----------------------------')
    logging.info('Main function ended!')