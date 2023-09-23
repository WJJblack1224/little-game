import tkinter as tk
import random
import tkinter.messagebox

liTle=1
bIg=100

answeR=random.randint(2,99)

wiN = tk.Tk()



wiN.title("終極密碼")

wiN.geometry("620x500+350+150")
wiN.configure(bg='black')
a=0
num=tk.StringVar()
num.set(a)

laBel=tk.Label(wiN,textvariable=num,fg="black",bg="white", font=("Arial", 16), width=49, height=3,anchor='center')

laBel.place(x=5,y=10)
def test(e):
    global a
    if e=="delete":
        a=0
        num.set(a)
    else:
        if a!=0:
            a=f"{a}{e}"
        else:
            a=f"{e}"
        num.set(a)

def _hit1():
    global answeR
    global a
    if int(a)==answeR:
        listBox.insert("end",str(a),"-------Boom!! 遊戲結束!!")
    elif int(a) > answeR:
        global bIg,liTle
        
        bIg=a
        listBox.insert("end",str(a)+"到"+str(liTle)+"之間")
        a=0
        
    else:
       
        liTle=a
        listBox.insert("end",str(bIg)+"到"+str(a)+"之間")
        a=0
    
    
def _hit2():
    global bIg,liTle,answeR,a,num
    
    liTle=1
    bIg=100
    a=0
    num.set(a)
    answeR=random.randint(2,99)
    listBox.delete(0,"end")

def _hit3():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎?")
    if qQ:
        wiN.destroy()
        
    
        
    
    
btN1 = tk.Button(wiN, text="1", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(1))
btN2 = tk.Button(wiN, text="2", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(2))
btN3 = tk.Button(wiN, text="3", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(3))
btN4 = tk.Button(wiN, text="4", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(4))
btN5 = tk.Button(wiN, text="5", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(5))
btN6 = tk.Button(wiN, text="6", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(6))
btN7 = tk.Button(wiN, text="7", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(7))
btN8 = tk.Button(wiN, text="8", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(8))
btN9 = tk.Button(wiN, text="9", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(9))
btN0 = tk.Button(wiN, text="0", font=("Arial", 12), width=10, height=2,bg="#C0C0C0",command=lambda:test(0))
btND = tk.Button(wiN, text="清空", font=("Arial",12,'bold'), width=6, height=5,bg="#C0C0C0",fg="white",command=lambda:test("delete"))
btNA = tk.Button(wiN, text="我猜!", font=("Arial", 12), width=10, height=3,bg="#C0C0C0",fg="#0000CD",command=_hit1)
btNR = tk.Button(wiN, text="重玩", font=("Arial", 12), width=10, height=3,bg="#C0C0C0",fg="#006400",command=_hit2)
btNC = tk.Button(wiN, text="結束", font=("Arial", 12), width=10, height=3,bg="#C0C0C0",fg="#DC143C",command=_hit3)

btN1.place(x=10,y=100)
btN2.place(x=113,y=100)
btN3.place(x=216,y=100)
btN4.place(x=319,y=100)
btN5.place(x=422,y=100)
btN6.place(x=10,y=153)
btN7.place(x=113,y=153)
btN8.place(x=216,y=153)
btN9.place(x=319,y=153)
btN0.place(x=422,y=153)
btND.place(x=527,y=100)
btNA.place(x=150,y=210)
btNR.place(x=253,y=210)
btNC.place(x=356,y=210)

wiN.resizable(width=False, height=False)
sBar=tk.Scrollbar(wiN)
sBar.pack(side="right",fill="y")

listBox=tk.Listbox(wiN, font=("Arial", 20),height=6,bg="black",fg="white",yscrollcommand=sBar.set)
listBox.pack(side="bottom", fill="both")
sBar.config(command=listBox.yview)

wiN.mainloop()
