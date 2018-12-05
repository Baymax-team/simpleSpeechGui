from tkinter import *
from time import *

class App:
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Speech Test")
        self.root.geometry("300x200") #200x110
        self.root.resizable(0, 0)

        self.botLabel = Label(text="Bot").place(x = 45,y = 40)
        self.userLabel = Label(text="User").place(x = 35,y = 75)
        self.timeDisp = Label(text=" ")
        self.timeDisp.place(x=100,y=150)

        self.botResponse = Entry()
        self.botResponse.place(x = 100,y = 40)    
        self.userResponse = Entry()
        self.userResponse.place(x = 100,y = 75)
        self.recordBtn = Button(text="Start Recording",command=self.startRecord)
        self.recordBtn.place(x = 120,y = 120)        

        self.btnCount = 0        
        self.root.mainloop()

    def timer(self): 
        self.timeDisp.configure(text="")
        self.recordBtn.configure(state=DISABLED)
        self.nowTime = strftime("%S")
        self.diff = int(self.nowTime) - int(self.startTime)
        if self.diff < 10 :
            self.timeDisp.configure(text="Recording ... " + str(self.diff+1))
            self.root.after(1000,self.timer)
        else:
            self.btnCount += 1
            self.root.after(100,self.endRecord)
                    
    def startRecord(self):        
        self.startTime = strftime("%S")
        self.diff = 0
        if self.btnCount == 0:            
            self.timeDisp.configure(text="Recording ...")            
            self.timer()
        else:            
            self.timeDisp.configure(text="Wait..")
            self.btnCount = 0                    
            self.root.after(3000,self.startRecord)

    def endRecord(self):        
        self.recordBtn.configure(state=NORMAL)                
        self.timeDisp.configure(text="Finish Recording")                
                    
a = App()