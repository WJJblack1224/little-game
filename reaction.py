import tkinter as tk,random,time

def _hit():
    showTime=random.randint(3000,5000)
    btN1["bg"]="#FF0000"
    btN1["text"]="畫面變色時點擊畫面"
    wiN.after(showTime,_chg)


def _chg():
        global startTime
        btN1["bg"]="#00FA9A"
        startTime=time.time()
        btN1["state"]=tk.NORMAL
        
    
def _reaction():
    global startTime
    endTime=time.time()
    reactionTime=endTime-startTime
    btN1["text"]="你的反應時間為:%5.3f秒"%reactionTime
    btN1["state"]=tk.DISABLED 
    
    
startTime=0  
        
wiN = tk.Tk()
wiN.title("反應速度測試")

wiN.configure(bg='aliceblue')

wiN.geometry("800x450+350+150")


btN1 = tk.Button(wiN,text="測試你的反應速度",fg="white",bg="#6495ED", font=("Arial", 25), width=41, height=9,command=_reaction,state=tk.DISABLED)
btN1.place(x=6,y=0)
btN2 = tk.Button(wiN, text="開始", font=("Arial", 12), width=10, height=2,command=_hit)
btN2.place(x=350,y=385)


wiN.resizable(width=False, height=False)
wiN.mainloop()
