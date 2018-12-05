from threading import Thread
from tkinter import *
from time import *
import pyaudio
import wave

class App:
    
    def __init__(self):        

        # Tkinter components
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

        self.startTime = strftime("%S")
        self.diff = 0
        self.idx = 0
        self.btnCount = 0        
        self.root.mainloop()            
            
    def startRecord(self):    
        self.startTime = strftime("%S")
        self.diff = 0
        if self.btnCount == 0:        
            self.timeDisp.configure(text="Recording ...")            
            print("Recording ...")
            self.recordBtn.configure(state=DISABLED)            
            self.root.after(100,self.middleware(False))
        else:            
            self.btnCount = 0
            print("Wait..")
            self.timeDisp.configure(text="Wait..")
            self.root.after(2000,self.startRecord)

    def middleware(self,finishRecord):
        if finishRecord:
            print("finish Recording")
            self.timeDisp.configure(text="finish Recording")
            self.idx += 1
            self.root.after(100,self.endRecord)
        else:
            self.root.after(100,self.record)

    def endRecord(self):
        print("{} saved".format(self.WAVE_OUTPUT_FILENAME))
        self.timeDisp.configure(text="{} saved".format(self.WAVE_OUTPUT_FILENAME))
        self.recordBtn.configure(state=NORMAL)
        self.timeDisp.configure(text="")

    def record(self):
        
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 16000
        CHUNK = 1024
        RECORD_SECONDS = 1
        self.WAVE_OUTPUT_FILENAME = "record" + str(self.idx) + ".wav"
        audio = pyaudio.PyAudio()
        print("\a")
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

        frames = []         
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)            
            frames.append(data)
            
                    
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("\a")

        
        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()        
        self.root.after(100,self.middleware(True))

a = App()