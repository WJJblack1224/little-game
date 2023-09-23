import tkinter as tk
import random
import tkinter.messagebox

wiN = tk.Tk()
wiN.title("密碼燈大挑戰!")
wiN.geometry("800x550+350+150")
wiN.configure(bg='black')

anSwer=random.sample(range(10),4)

a=0
num1=tk.StringVar()
num1.set(a)

b=0
num2=tk.StringVar()
num2.set(b)

c=0
num3=tk.StringVar()
num3.set(c)

d=0
num4=tk.StringVar()
num4.set(d)

fQ=1

def _add1():
    global a
    a=a+1
    num1.set(a)
    if a>9:
        a=0
        num1.set(a)
    
def _add2():
    global b
    b=b+1
    num2.set(b)
    if b>9:
        b=0
        num2.set(b)    

def _add3():
    global c
    c=c+1
    num3.set(c)
    if c>9:
        c=0
        num3.set(c)
        
def _add4():
    global d
    d=d+1
    num4.set(d)
    if d>9:
        d=0
        num4.set(d)   

def _reduce1():
    global a
    a=a-1
    num1.set(a)
    if a<0:
        a=9
        num1.set(a)

def _reduce2():
    global b
    b=b-1
    num2.set(b)
    if b<0:
        b=9
        num2.set(b)

def _reduce3():
    global c
    c=c-1
    num3.set(c)
    if c<0:
        c=9
        num3.set(c)

def _reduce4():
    global d
    d=d-1
    num4.set(d)
    if d<0:
        d=9
        num4.set(d)

def _guess():
    if a == anSwer[0]:
        lbL1["bg"]="#00FA9A"
    elif a == anSwer[1] or a == anSwer[2] or  a == anSwer[3]:
        lbL1["bg"]="#FFCC00"
    else:
        lbL1["bg"]="#FF0000"
        
        
    if b == anSwer[1]:
        lbL2["bg"]="#00FA9A"
    elif b == anSwer[0] or b == anSwer[2] or  b == anSwer[3]:
        lbL2["bg"]="#FFCC00"
    else:
        lbL2["bg"]="#FF0000"
        
        
    if c == anSwer[2]:
        lbL3["bg"]="#00FA9A"
    elif c == anSwer[0] or c == anSwer[1] or  c == anSwer[3]:
        lbL3["bg"]="#FFCC00"
    else:
        lbL3["bg"]="#FF0000"
        
    if d == anSwer[3]:
        lbL4["bg"]="#00FA9A"
    elif d == anSwer[0] or d == anSwer[1] or  d == anSwer[2]:
        lbL4["bg"]="#FFCC00"
    else:
        lbL4["bg"]="#FF0000"
    
    
    if a == anSwer[0] and b == anSwer[1] and c == anSwer[2] and d == anSwer[3]:
        global fQ
        tk.messagebox.showinfo("恭喜!","解鎖成功!\n"+"本回合共猜"+str(fQ)+"次")
        fQ=1
    else:
        fQ=fQ+1
        
        
        
        
        
        
        
        
def _reset():
    global a,b,c,d,num1,num2,num3,num4,anSwer
    anSwer=random.sample(range(10),4)
    a=b=c=d=0
    num1.set(a)
    num2.set(b)
    num3.set(c)
    num4.set(d)
    lbL1["bg"]="white"
    lbL2["bg"]="white"
    lbL3["bg"]="white"
    lbL4["bg"]="white"
    
def _close():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎?")
    if qQ:
        wiN.destroy()

def _question():
    wiN1=tk.Toplevel(wiN)
    wiN1.title("規則說明")
    wiN1.geometry("700x180+200+100")
    btN1 = tk.Button(wiN1, text="密碼燈的背後是一組相異的4個數字，玩家可藉由點擊[+] 、[ - ]按鈕對欄位的數字進行加減\n\n當點擊[解鎖!]按鈕後，若該欄位的數字與密碼燈後的數字相同便會亮起綠燈\n\n若該欄數字不符合，但與其他欄位的燈後數字相同則會亮起黃燈，都不符合則會亮起紅燈\n\n當4個數字都猜中，亮起4個綠燈時便解鎖成功!", font=("Arial", 10), width=3000, height=12, command=wiN1.destroy)
    btN1.pack() 


frame1 = tk.Frame(wiN, pady=16, padx=16, bg='#f90') 
frame1.place(x=150,y=20)
label1 = tk.Label(frame1, text='密', font=("Arial", 12,"bold"),width=6,height=2,bg="black",fg="white") 
label1.pack()

frame2 = tk.Frame(wiN, pady=16, padx=16, bg='#09c') 
frame2.place(x=250,y=20)
label2 = tk.Label(frame2, text='碼', font=("Arial", 12,"bold"),width=6,height=2,bg="black",fg="white") 
label2.pack()

frame3 = tk.Frame(wiN, pady=16, padx=16, bg="#FF0000") 
frame3.place(x=350,y=20)
label3 = tk.Label(frame3, text='紅', font=("Arial", 12,"bold"),width=6,height=2,bg="black",fg="white") 
label3.pack()

frame4 = tk.Frame(wiN, pady=16, padx=16, bg="#FFCC00") 
frame4.place(x=450,y=20)
label4 = tk.Label(frame4, text='綠', font=("Arial", 12,"bold"),width=6,height=2,bg="black",fg="white") 
label4.pack()

frame5 = tk.Frame(wiN, pady=16, padx=16, bg="#00FA9A") 
frame5.place(x=550,y=20)
label5 = tk.Label(frame5, text='燈', font=("Arial", 12,"bold"),width=6,height=2,bg="black",fg="white") 
label5.pack()


lbL1 = tk.Label(wiN,textvariable=num1,fg="black",bg="white", font=("Arial", 14), width=10, height=4)
lbL1.place(x=120,y=150)
lbL2 = tk.Label(wiN,textvariable=num2,fg="black",bg="white", font=("Arial", 14), width=10, height=4)
lbL2.place(x=270,y=150)
lbL3 = tk.Label(wiN,textvariable=num3,fg="black",bg="white", font=("Arial", 14), width=10, height=4)
lbL3.place(x=420,y=150)
lbL4 = tk.Label(wiN,textvariable=num4,fg="black",bg="white", font=("Arial", 14), width=10, height=4)
lbL4.place(x=570,y=150)


btN1 = tk.Button(wiN, text="+", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_add1)
btN2 = tk.Button(wiN, text="+", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_add2)
btN3 = tk.Button(wiN, text="+", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_add3)
btN4 = tk.Button(wiN, text="+", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_add4)
btN5 = tk.Button(wiN, text="-", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_reduce1)
btN6 = tk.Button(wiN, text="-", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_reduce2)
btN7 = tk.Button(wiN, text="-", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_reduce3)
btN8 = tk.Button(wiN, text="-", font=("Arial", 13), width=10, height=1,bg="#C0C0C0",command=_reduce4)
btNA = tk.Button(wiN, text="解鎖!", font=("Arial", 14,"bold"), width=8, height=3,bg="#00FA9A",fg="white",command=_guess)
btNR = tk.Button(wiN, text="重設",  font=("Arial", 14,"bold"), width=8, height=3,bg="#FFCC00",fg="white",command=_reset)
btNC = tk.Button(wiN, text="離開",  font=("Arial", 14,"bold"), width=8, height=3,bg="#FF0000",fg="white",command=_close)
btNQ = tk.Button(wiN, text="?",  font=("Arial", 11,"bold"), width=4, height=2,bg="#1E90FF",fg="white",command=_question)


btN1.place(x=130,y=265)
btN2.place(x=280,y=265)
btN3.place(x=430,y=265)
btN4.place(x=580,y=265)
btN5.place(x=130,y=305)
btN6.place(x=280,y=305)
btN7.place(x=430,y=305)
btN8.place(x=580,y=305)
btNA.place(x=180,y=415)
btNR.place(x=350,y=415)
btNC.place(x=520,y=415)
btNQ.place(x=730,y=30)


wiN.resizable(width=False, height=False)
wiN.mainloop()