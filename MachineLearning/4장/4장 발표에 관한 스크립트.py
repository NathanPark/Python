import bayes

'''
4_1. 텍스트로 단어 벡터 만들기
myVocabList는 단어의 유니크함을 나타내기 위해 사용한다.
'''
listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
myVocabList

bayes.setOfWords2Vec(myVocabList, listOPosts[0])

bayes.setOfWords2Vec(myVocabList, listOPosts[3])

------------------------------------------------------------------------------------------------------------------------------------------------

'''
4_1_2. 훈련: 단어 벡터로 확률 계산하기
'''

from numpy import *
reload(bayes)
listOPosts, listClasses = bayes.loadDataSet()
#이전의 값들을 데이터로 불러옴

myVocabList = bayes.createVocabList(listOPosts)
#myVocabList에 있는 단어들을 갖고 하나의 리스트를 생성

trainMat[]
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))

p0V,p1V,pAb = bayes.trainNB0(trainMat,listClasses)

pAb

p0V

p1V

------------------------------------------------------------------------------------------------------------------------------------------------

'''
4_1_3. 검사: 실제 조건을 반영하기 위해 분류기 수정하기
'''
reload(bayes)
bayes.testingNB()

------------------------------------------------------------------------------------------------------------------------------------------------

'''
4_2. 예제: 스팸 이메일 분류하기
'''

# 4_2.1 텍스트 토큰 만들기
MySent='This book is the best book on Python or M.L. I have ever laid eyes upon.'
MySent.split()

import re
regEx = re.compile('\\W*')
listOfTokens = regEx.split(MySent)
listOfTokens

[tok for tok in listOfTokens if len(tok) > 0]

# 예제 email을 사용
emailText=open('Python/Script/[file].txt').read()
listofTokens = regEx.split(emailText)
listofTokens

[sent for sent in listofTokens if len(sent) > 0]

bayes.spamTest()
bayes.spamTest()

------------------------------------------------------------------------------------------------------------------------------------------------


'''
4_3. 나이브 베이즈를 사용하여 개인 광고에 포함된 지역 특색 도출하기
'''

import feedparser
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
ny['entries']
len(ny['entries'])

reload(bayes)
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')

vocabList, pSF, pNY = bayes.localWords(ny,sf)

vocabList, pSF, pNY = bayes.localWords(ny,sf)

reload(bayes)
bayes.getTopWords(ny,sf)
