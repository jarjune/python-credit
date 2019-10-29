import requests
import re
from bs4 import BeautifulSoup

import uuid
import mysql.connector

# 线程数(暂时无用)
THREADS_NUM = 5

# 批次号
BATCH_ID = str(uuid.uuid1())

# 站点名称
SITE_NAME = '信用河北（石家庄）'

# 数据库连接
conn = mysql.connector.connect(host='192.168.30.248', user='root', password='mysql', database='py')

###############################

baseURL = 'http://www.sjzxy.gov.cn'

def getArticle(uniqueCode, moduleName, page = 1, size = 10):

    requestURL = baseURL + '/node/' + str(uniqueCode)
    if page > 1:
        requestURL += '_' + str(page)
    
    response = requests.get(requestURL)

    soup = BeautifulSoup(response.text, 'lxml')
    
    articleList = soup.select('#blog-mainbody > ul > li a')

    resultEntityList = []
    for item in articleList:
        entity = getDetail(detailURL = item.get('href'))
        entity['batch_id'] = BATCH_ID
        entity['site_name'] = SITE_NAME
        entity['site_module'] = moduleName
        resultEntityList.append(entity)

    saveArticle(resultEntityList)
    return

def getDetail(detailURL):

    requestURL = baseURL + detailURL

    response = requests.get(requestURL)

    soup = BeautifulSoup(response.text, 'lxml')
    
    body = soup.select_one('body > div.ncc.box')

    title = body.select_one('h1').text
    source = body.select_one('div.date').text

    arr = re.findall(r'\s*[^\s]*?：([^\s]*)\s*', source)
    content = body.select_one('div.nwwcon')

    summary = arr[0]
    date = arr[1]
    return {'title': title, 'summary': summary, 'publish_time': date, 'html': str(content), 'url': requestURL}

def saveArticle(resultEntityList):

    resultEntityListRemove = []

    cursor = conn.cursor()
    for item in resultEntityList:
        cursor.execute('select count(*) from article where title = %s and site_name = %s and site_module = %s', (item['title'], item['site_name'], item['site_module']))
        if cursor.fetchone()[0] == 0:
            cursor.execute('insert into article (title, summary, publish_time, html, url, site_name, site_module, batch_id) values (%s,%s,%s,%s,%s,%s,%s,%s)', (item['title'], item['summary'], item['publish_time'], item['html'], item['url'], item['site_name'], item['site_module'], item['batch_id']))
        else:
            resultEntityListRemove.append(item)
    conn.commit()
    cursor.close()
    return

# 获取多少页，第一次可以全部获取
def getFullArticle(page):
    for i in range(1, page):
        getArticle(uniqueCode = 118, moduleName = '风险提示', page = i, size = 10)
    return

getFullArticle(9)
# getArticle(uniqueCode = 118, moduleName = '风险提示', page = 1, size = 10)