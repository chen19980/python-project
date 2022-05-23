import pymongo
import certifi
import tkinter as tk

from bs4 import BeautifulSoup
import requests
import time

client = pymongo.MongoClient("mongodb+srv://gift60307:zxc123456@cluster0.jgt9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())

db = client.joblist
col = db.list

win=tk.Tk()
win.title("1111職缺查詢")
win.geometry('300x300')
win.config(bg="#CDCD9A")

lb=tk.Label(text="職缺查詢")
lb.config(bg="#C6A300",fg="#4F4F4F")
lb.pack()

en=tk.Entry()
en.pack()

# res = requests.get("https://www.1111.com.tw/search/job?ks=%E5%A4%A7%E6%95%B8%E6%93%9A")
# soup = BeautifulSoup(res.text)


# page = 0
# while page<73:
#     page += 1
#     res = requests.get("https://www.1111.com.tw/search/job?ks=%E5%A4%A7%E6%95%B8%E6%93%9A&page="+str(page))
#     soup = BeautifulSoup(res.text)
#     for job in soup.find_all("div",class_="job-list-item")[0].find_all("div",class_="job_item_info") :
#         a = job.h5.text   #職位名稱
#         b = job.a["href"]    #網址
#         c = job.h6.text      #公司名稱
#         d = job.find_all("a",class_="job_item_detail_location mr-3 position-relative")[0].text    #公司地區
#         e = job.find_all("div", class_="job_item_detail_salary ml-3 font-weight-style digit_6")[0].text  #薪水
#         f = job.select("div")[2].div.div.text[0:2]

#         price = ""

#         for word in e:
#             if  word == "0" or word == "1" or word == "2" or word == "3" or word == "4" or word == "5" or word == "6" or word == "7" or word == "8" or word == "9" or word == "~" or word == "." or word == "萬" :
#                 price += word

#         low_price = ""
#         high_price = ""
#         if "~" in price :
#             low_price = price[0:price.find("~")]
#             high_price = price[price.find("~")+1:len(price)]
#         else:
#             low_price = price
#             high_price = price
 
#         if "萬" in low_price:
#             low_price = low_price[0:low_price.find("萬")]
#             low_price = float(low_price)*10000 

#         else:
#             low_price = float(low_price)

 
#         if "萬" in high_price:
#             high_price = high_price[0:high_price.find("萬")]
#             high_price = float(high_price)*10000 
        
#         else:
#             high_price = float(high_price)
#         wk = {"職位名稱":a,"網址":b,"公司名稱":c,"公司地區":d,"薪水":e,"給薪方式":f,"薪資下限":low_price,"薪資上限":high_price}
#         result = col.insert_one(wk)
#     print(f"已完成:{page}")   
#     print("--------------") 
#     time.sleep(2)


def work():
    t = en.get()
    result2 = col.find_one({"網址":t})
    x = result2["職位名稱"]
    lb2.config(text ="職位名稱: "+x,bg="#C6A300",fg="#4F4F4F")

lb2=tk.Label(text = "職位名稱")
lb2.config(bg="#C6A300",fg="#4F4F4F")
lb2.pack()

btn=tk.Button(text="開始搜尋")
btn.config(command = work)
btn.pack()
win.mainloop() 

# print(result)



