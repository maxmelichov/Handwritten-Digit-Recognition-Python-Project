from tkinter import *
import win32gui
from PIL import ImageGrab
import predictANN,predictCNN

class App(object):
    def __init__(self, root):
        self.x = self.y = 0
        self.root= root
        self.canvas = Canvas(root, height=200, width=200, bg="white", cursor="cross")
        self.canvas.bind('<B1-Motion>',self.addLine)
        self.canvas.place(x=0,y=0)
        self.canvas.grid(row=0, column=0, pady=2, sticky=W )
        self.button1 = Button(root, text="PredictANN", command=self.predictANN)
        self.button2 = Button(root, text="PredictCNN", command=self.predictCNN)
        self.button3= Button(root, text="Clear", font=('Helvetica bold', 10), command = self.reset,background= 'green')
        self.button4= Button(root, text="Quit", font=('Helvetica bold', 10), command = self.quit,background='red')
        self.button1.place(x=200,y=10)
        self.button2.place(x=300,y=10)
        self.button3.place(x=100,y=220)
        self.button4.place(x=10,y=220)
        self.count =0 
    # def locate_xy(self,event):
    #     global current_x,current_y
    #     current_x,current_y=event.x,event.y

    
    #  draw func
    def addLine(self,event):
        self.x = event.x
        self.y = event.y
        r=7 # width of the line
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
        
        
    # pred func
    def predictANN(self):
        HWND = self.canvas.winfo_id() 
        rect = win32gui.GetWindowRect(HWND) 
        img = ImageGrab.grab(rect)
        dig,acc = predictANN.loadimg(img)
        self.count+=1
        self.label1 =Label(text= str(dig)+', '+ str(int(acc*100))+'%'+',\nattempts:'+str(self.count),font=("Helvetica", 12))
        self.label1.place(x=210,y=50)


    def predictCNN(self):
        HWND = self.canvas.winfo_id() 
        rect = win32gui.GetWindowRect(HWND) 
        img = ImageGrab.grab(rect)
        dig,acc = predictCNN.loadimg(img)
        self.count+=1
        self.label2 =Label(text= str(dig)+', '+ str(int(acc*100))+'%'+',\nattempts:'+str(self.count),font=("Helvetica", 12))
        self.label2.place(x=310,y=50)

    # reset GUI
    def reset(self):
        self.canvas.delete('all')
        self.label1.destroy()
        self.label2.destroy()

    # quit GUI
    def quit(self):
        self.root.destroy() 

if __name__ == '__main__':
    root = Tk()
    w = 400 # width for the Tk root
    h = 250 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() 
    hs = root.winfo_screenheight() 

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Number predict")
    app = App(root)
    root.mainloop()