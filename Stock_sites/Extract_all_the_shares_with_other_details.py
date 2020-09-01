from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
w = wd.Chrome('G:\chromedriver.exe')

url = 'https://www.dextools.io/app/uniswap/pool-explorer'
w.get(url)

try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(w, 5).until(element_present)
    WebDriverWait(w, 5).untill(w.execute_script('return jQuery.active')==0)
    WebDriverWait(w, 5).untill(w.execute_script('return document.readyState')==0)
except TimeoutException:
    pass
   
time.sleep(5)

try:
    a = w.find_elements_by_xpath("//div[@class='alert mb-0 ng-tns-c46-2 ng-star-inserted']")
    if(len(a)==0):
        raise Exception("N")
    else:
        print(a[0].text)

except:
        w.find_element_by_xpath("//*[@class = 'ng-tns-c46-2']").click()
        try:
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(w, 5).until(element_present)
            WebDriverWait(w, 5).untill(w.execute_script('return jQuery.active')==0)
            WebDriverWait(w, 5).untill(w.execute_script('return document.readyState')=='complete')
        except TimeoutException:
            pass
        print("Please enter the number of choice : ")
        print("============================================")
        print("1. ADD")
        print("2. REMOVE")
        print("3. NEW")
        print("============================================")
        user_input_1 = int(input("=>  : ").strip(" "))
        if(user_input_1 == 1):
            equity = []
            try:
                element_present = EC.presence_of_element_located((By.ID, 'table'))
                WebDriverWait(w, 5).until(element_present)
                WebDriverWait(w, 5).untill(w.execute_script('return jQuery.active')==0)
                WebDriverWait(w, 5).untill(w.execute_script('return document.readyState')=='complete')
            except TimeoutException:
                pass
            w.find_element_by_xpath("//*[@class = 'ng-tns-c46-2'and @value = 'ADD']").click()
            w.find_elements_by_xpath("//*[@class='ng-tns-c46-6 ng-trigger ng-trigger-newToken ng-star-inserted']/tbody")
            t = w.find_elements_by_xpath("//table[@class='table mb-0 ng-tns-c46-2']/tbody/tr")
            
            print("============================================")
            for i in range(len(t)):
                tr = w.find_elements_by_xpath("//table[@class='table mb-0 ng-tns-c46-2']/tbody/tr["+str(i+1)+"]/td")
                if(len(tr)==0):
                    pass;
                else:
                    print(str(i+1) +" : "+ tr[0].text+" \t " +tr[1].text+" \t"+tr[4].text+"\t"+tr[5].text)
                    equity.append(tr[0].text)
                if(i>48):
                    break;
            print("============================================") 
            equity.sort()
            p = equity[0]
            count = 0 ;
            for i in range(len(equity)):
                if(p != equity[i]):
                    print(p +"  "+ str(count) +" "+ "pools added")
                    count =1;
                    p=equity[i]
                else:
                    count+=1
                if(i==len(equity)-1):
                    print(equity[len(equity)-1] +" "+ str(count)+" pools added")

        elif(user_input_1 == 2):
            equity = []
            try:
                element_present = EC.presence_of_element_located((By.ID, 'table'))
                WebDriverWait(w, 5).until(element_present)
                WebDriverWait(w, 5).untill(w.execute_script('return jQuery.active')==0)
                WebDriverWait(w, 5).untill(w.execute_script('return document.readyState')=='complete')
            except TimeoutException:
                pass
            w.find_element_by_xpath("//*[@class = 'ng-tns-c46-2'and @value = 'REMOVE']").click()
            w.find_elements_by_xpath("//*[@class='ng-tns-c46-6 ng-trigger ng-trigger-newToken ng-star-inserted']/tbody")
            t = w.find_elements_by_xpath("//table[@class='table mb-0 ng-tns-c46-2']/tbody/tr")
            time.sleep(3)
            print("============================================")
            for i in range(len(t)):
                tr = w.find_elements_by_xpath("//table[@class='table mb-0 ng-tns-c46-2']/tbody/tr["+str(i+1)+"]/td")
                if(len(tr)==0):
                    pass;
                else:
                    print(str(i+1) +" : "+ tr[0].text+" \t " +tr[1].text+" \t"+tr[4].text+"\t"+tr[5].text)
                    equity.append(tr[0].text)
                if(i>48):
                    break;
            print("============================================") 
            equity.sort()
            p = equity[0]
            count = 0 ;
            for i in range(len(equity)):
                if(p != equity[i]):
                    print(p +"  "+ str(count) +" "+ "pools removed")
                    count =1;
                    p=equity[i]
                else:
                    count+=1
                if(i==len(equity)-1):
                    print(equity[len(equity)-1] +" "+ str(count)+" pools removed")
        elif(user_input_1 == 3):
            equity = []
            try:
                element_present = EC.presence_of_element_located((By.ID, 'table'))
                WebDriverWait(w, 5).until(element_present)
                WebDriverWait(w, 5).untill(w.execute_script('return jQuery.active')==0)
                WebDriverWait(w, 5).untill(w.execute_script('return document.readyState')=='complete')
            except TimeoutException:
                pass
            w.find_element_by_xpath("//*[@class = 'ng-tns-c46-2'and @value = 'NEW']").click()
            w.find_elements_by_xpath("//*[@class='ng-tns-c46-6 ng-trigger ng-trigger-newToken ng-star-inserted']/tbody")
            t = w.find_elements_by_xpath("//table[@class='table mb-0 ng-tns-c46-2']/tbody/tr")
            time.sleep(3)
            print("============================================")
            for i in range(len(t)):
                tr = w.find_elements_by_xpath("//table[@class='table mb-0 ng-tns-c46-2']/tbody/tr["+str(i+1)+"]/td")
                if(len(tr)==0):
                    pass;
                else:
                    print(str(i+1) +" : "+ tr[0].text+" \t " +tr[1].text+" \t"+tr[4].text+"\t"+tr[5].text)
                    equity.append(tr[0].text)
                if(i>48):
                    break;
            print("============================================") 
            if(len(equity)>0):
                equity.sort()
                p = equity[0]
                count = 0 ;
                for i in range(len(equity)):
                    if(p != equity[i]):
                        print(p +"  "+ str(count) +" "+ "pools are New")
                        count =1;
                        p=equity[i]
                    else:
                        count+=1
                    if(i==len(equity)-1):
                        print(equity[len(equity)-1] +" "+ str(count)+" pools are New")
        else:
            print("Please enter valid input")

w.close()

        

            
            

    
