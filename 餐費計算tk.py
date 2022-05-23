import tkinter as tk

def do_it():
    price = en.get()
    if price.replace('.','').isdigit()==True:
        price = float(price)
        tip = price*0.1
        price+=tip
        tax = price*0.05
        total=price+tax
        lb1.config(text='服務費:'+str(tip))
        lb2.config(text='營業稅:'+str(tax))
        lb3.config(text='總金額:'+str(total))
    else:
        t='請輸入「數字」'
        t+='!'
        lb.config(text=t)


#定義主視窗
win=tk.Tk()

#視窗屬性設定區
win.title('餐費計算小程式')
win.geometry('300x250')
win.resizable(False,False)
win.iconbitmap('haski.ico')
win.config(bg='#A3D8F8')
#win.attributes('-alpha',0.8)
win.attributes('-topmost',True)

#定義按鈕物件
#img=tk.PhotoImage(text='按按鈕開始計算總餐費')
btn=tk.Button(text='按按鈕開始計算總餐費')
btn.config(bg='#0C2D50',fg='#F8F9F9',command=do_it)
btn.grid(column=0,row=0,columnspan=3,pady=5)


#定義標籤物件
lb=tk.Label(text='請輸入餐費')
lb.config(bg='#0C2D50',fg='#F8F9F9')
lb.grid(column=0,row=1,pady=5)

#定義輸入框物件
en=tk.Entry()
en.grid(column=1,row=1,columnspan=2,pady=5)

#定義標籤物件(呈現計算結果)
lb1=tk.Label(text='服務費：')
lb1.config(bg='#0C2D50',fg='#F8F9F9')
lb1.grid(column=0,row=2,pady=5)
lb2=tk.Label(text='營業稅：')
lb2.config(bg='#0C2D50',fg='#F8F9F9')
lb2.grid(column=1,row=2,pady=5)
lb3=tk.Label(text='總金額：')
lb3.config(bg='#0C2D50',fg='#F8F9F9')
lb3.grid(column=2,row=2,pady=5)

win.mainloop()

