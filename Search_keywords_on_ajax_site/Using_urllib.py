from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
import requests
import xlsxwriter
key = "alcohol"
url1="https://www.babycenter.com/search/momanswers.htm?q="+str(key)
r = urlopen(url1)
soup = bf(r,'lxml')
a = soup.find(id ="solrSearchResults")
a = int(a.find("h1").get_text().split(" ")[0])
links = []
if(a-1/10 == 0 ):
    for i in range(a):
        links.append("https://community.babycenter.com/"+soup.find(id ="searchResultTitleLink-"+str(i+1))['href'])
        print("https://community.babycenter.com/"+soup.find(id ="searchResultTitleLink-"+str(i+1))['href'])
else:
    for i in range(10):
        links.append("https://community.
        babycenter.com/"+soup.find(id ="searchResultTitleLink-"+str(i+1))['href'])
    for i in range(1,a//10):
        url = "https://www.babycenter.com/search/momanswers.htm?startIndex="+str(i)+"0&q="+str(key)
        r = urlopen(url)
        soup = bf(r,'lxml')
        for j in range(10):
            links.append("https://community.babycenter.com/"+soup.find(id ="searchResultTitleLink-"+str(j+1))['href'])
if(not a//10==0 and not a%10==0 ):
    url = "https://www.babycenter.com/search/momanswers.htm?startIndex="+str(a//10)+"0&q="+str(key)
    r = urlopen(url)
    soup = bf(r,'lxml')
    for j in range(a%10):
        links.append("https://community.babycenter.com/"+soup.find(id ="searchResultTitleLink-"+str(j+1))['href'])
        print("https://community.babycenter.com/"+soup.find(id ="searchResultTitleLink-"+str(j+1))['href'])
wx = xlsxwriter.Workbook("G:/Free Lancer/Alcohol_final.xlsx")
wx1= wx.add_worksheet()
num =1
max = 0
wx1.write(0,0,"Keyword search term")
wx1.write(0,1,"Title of post")
wx1.write(0,2,"Question")
wx1.write(0,3,"ScreenName")
wx1.write(0,4,"Date Asked/ Posted for original question")
wx1.write(0,5,"Mom  Answers number Of answer")
wx1.write(1,0,key)
for i in links:
    r = urlopen(i)
    soup = bf(r,'lxml')
    c = soup.find(class_ ="mainQuestion")
    wx1.write(num,1,c.find(class_ = 'h1Container withBookmark').find('h1').get_text().strip("\n"))
    wx1.write(num,2,c.find(class_ ='spacer bodyText').get_text().strip("\n"))

    wx1.write(num,3,c.find(class_ ='screenName').get_text().strip("\n"))
    wx1.write(num,4,c.find(class_ ='details').get_text().strip("\n"))
    wx1.write(num,5,soup.find(class_ ='fakeH2').get_text().strip("\n"))
    no_of_answer = soup.find(class_ ='fakeH2').get_text().strip("\n")
    n = int(no_of_answer.split(" ")[2].strip("(").strip(")"))
    if(max<n):
        max = n
    num1 = 6
    code = 0;
    if(n<=10):
        for i in range(n):
            answers = soup.find_all(class_ = 'maItem answerSection')
            wx1.write(num,num1,answers[0].find(class_ = 'spacer bodyText answerBody').get_text().replace('\n',' ').strip(" "))
            num1=num1+1
            wx1.write(num,num1,answers[0].find(class_ = 'screenName').get_text().replace('\n',' ').strip(" "))
            num1 = num1 +1
            wx1.write(num,num1,answers[0].find(class_ = 'details').get_text().replace('\n',' ').strip(" "))
            num1 = num1 +1
            h = answers[0].find(class_ = 'verticalCenterCell helpfulCount').get_text().replace('\n',' ').strip(" ")
            if(h == 'Was this helpful?'):
                h = '0 found this helpful'
            wx1.write(num,num1,h)
            num1 = num1 +1
    else:
        for i in range(10):
            answers = soup.find_all(class_ = 'maItem answerSection')
            wx1.write(num,num1,answers[0].find(class_ = 'spacer bodyText answerBody').get_text().replace('\n',' ').strip(" "))
            num1=num1+1
            wx1.write(num,num1,answers[0].find(class_ = 'screenName').get_text().replace('\n',' ').strip(" "))
            num1 = num1 +1
            wx1.write(num,num1,answers[0].find(class_ = 'details').get_text().replace('\n',' ').strip(" "))
            num1 = num1 +1
            h = answers[0].find(class_ = 'verticalCenterCell helpfulCount').get_text().replace('\n',' ').strip(" ")
            if(h == 'Was this helpful?'):
                h = '0 found this helpful'
            wx1.write(num,num1,h)
            num1 = num1 +1
            code = answers[0].find(class_ = "floatRight reportDataContainer")['data-report-question-id']
        for i in range(2,(n//10)+1):
            url = "https://www.babycenter.com/ws/ajax/v1/momanswers/question/"+str(code)+"?page="+str(i)
            r1 = requests.get(url)
            r = r1.json()
            for i in range(10):
                wx1.write(num,num1,r['answersPage']['content'][i]['answer'].replace("&#39;",","))
                num1=num1+1
                wx1.write(num,num1,r['answersPage']['content'][i]['screenName'])
                num1 = num1 +1
                wx1.write(num,num1,r['answersPage']['content'][i]['prettyCreateDate'])
                num1 = num1 +1
                wx1.write(num,num1,str(r['answersPage']['content'][i]['usefulCount'])+" found this useful")
                num1 = num1 +1
        url = "https://www.babycenter.com/ws/ajax/v1/momanswers/question/"+str(code)+"?page="+str((n//10)+1)
        r1 = requests.get(url)
        r = r1.json()
        for i in range(n%10):
                wx1.write(num,num1,r['answersPage']['content'][i]['answer'].replace("&#39;",","))
                num1=num1+1
                wx1.write(num,num1,r['answersPage']['content'][i]['screenName'])
                num1 = num1 +1
                wx1.write(num,num1,r['answersPage']['content'][i]['prettyCreateDate'])
                num1 = num1 +1
                wx1.write(num,num1,str(r['answersPage']['content'][i]['usefulCount'])+" found this useful")
                num1 = num1 +1
            
    num = num +1
num2 = 6
for i in range(max):
    wx1.write(0,num2,"Answer "+ str(i+1) + "(sometimes called Best Answer)")
    num2 = num2+1
    wx1.write(0,num2,"Answer "+ str(i+1) + "Screen name")
    num2 = num2+1
    wx1.write(0,num2,"Answer "+ str(i+1) + "Date answered")
    num2 = num2+1
    wx1.write(0,num2,"Number who found Answer "+ str(i+1) + "helpful (thumbs up)")
    num2 = num2+1
wx.close()
    
    
    
    
