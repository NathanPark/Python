'''
naver Blog Search Collect
author: Park Jung-Hwan in Sejong Univ. the master's course std.
make date: 2017-03-27
using IPython Notebook
'''

from urllib.parse import quote
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd
import time

class CollectBlog:
    def __init__(self, indexing, pageNum):
        self.index = quote(indexing.encode('utf-8'))
        self.pageNum = int(pageNum)
        
    def blogCollect(self):
        html_title=[]
        html_contents=[]
        html_author=[]
        html_date=[]
        
        for i in range(0,self.pageNum):
            time.sleep(10)
            url="http://section.blog.naver.com/sub/SearchBlog.nhn?type=post&option.keyword=%s"%(self.index) +\
                "&term=&option.startDate=&option.endDate=&option.page.currentPage=%d&option.orderBy=sim"%(self.pageNum)

            data=urllib.request.urlopen(url)
            content = data.read().decode(data.headers.get_content_charset())

            soup = BeautifulSoup(content, 'html.parser')
            html_list=soup.find('ul', class_ = 'list_type_1 search_list')

            for j in range(0,10):
                html_date.append(html_list.findAll('span', attrs={'class':'date'})[j].text)

            for i in range(0,len(html_list.findAll('a',attrs={'target':'_blank'}))):
                if(divmod(i,5)[1]==0):
                    html_title.append(html_list.findAll('a',attrs={'target':'_blank'})[i].text)
                elif(divmod(i,5)[1]==4):
                    html_contents.append(html_list.findAll('a',attrs={'target':'_blank'})[i].text)
                elif(divmod(i,5)[1]==1):
                    html_author.append(html_list.findAll('a',attrs={'target':'_blank'})[i].text)

        blog_Collect=pd.DataFrame()
        blog_Collect['Date']=html_date
        blog_Collect['title']=html_title
        blog_Collect['content']=html_contents
        blog_Collect['author']=html_author
        
        #return type is dataframe 
        return blog_Collect
    
'''
검색 문구 입력
IPython을 사용하였을 때를 예시로 함
'''
indexing=input("검색문구 입력: ")

'''
블로그 중 포스트 페이지 번호를 입력 
번호는 0번부터 시작이므로 최종번호까지만 입력하면 됨
'''
pageNum=input("블로그 검색 번호 입력: ")

collect_class=CollectBlog(indexing, pageNum)
collect_class.blogCollect()