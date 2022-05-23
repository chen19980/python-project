from bs4 import BeautifulSoup
import requests
import tkinter as tk


win = tk.Tk()
win.title('The weather')
win.geometry('300x250')
win.resizable(False,False)
win.config(bg='#A3D8F8')


def do_it():
    res = requests.get("https://tw.news.yahoo.com/weather/")
    soup = BeautifulSoup(res.text)
    t=soup.find_all('span',class_="Va(t)")[0].string+soup.find_all('span',class_="Va(t)")[1].string
    lb.config(text='氣溫：'+t)


btn=tk.Button()
btn.config(text='天氣',bg='#54CEB7',fg='#000000',command=do_it)
btn.grid(column=0,row=0,columnspan=3,pady=5,padx=15,ipady=10)

lb = tk.Label()
lb=tk.Label(text='氣溫')
lb.config(bg='#0C2D50',fg='#F8F9F9')
lb.grid(column=8,row=0,pady=5,padx=5,ipadx=60,ipady=5)


res = requests.get("https://tw.news.yahoo.com/weather/")
soup = BeautifulSoup(res.text)

win.mainloop()