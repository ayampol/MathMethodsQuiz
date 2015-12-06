#This code is based on http://pythonprogramming.net/change-show-new-frame-tkinter/

from Tkinter import *

LARGE_FONT= ("Consolas", 12)

class FrameWarden(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Math Methods Project by Jose and Alena');
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, InfoPage, QuizPage, GamePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        bannerframe = Frame(self,bd=7, width=500, height=100, relief= RAISED, bg="blue")
        bannerframe.pack(side = TOP)
        
        self.img1= PhotoImage(file="images/header1.gif")
        self.img2= PhotoImage(file="images/header2.gif")
        self.img3= PhotoImage(file="images/header3.gif")
        
        toptext = Label(bannerframe, image=self.img1, justify= CENTER)
        toptext2 =  Label(bannerframe, image= self.img2, justify= CENTER)
        toptext3 =  Label(bannerframe, image= self.img3, justify= CENTER)
        toptext.pack()
        toptext2.pack()
        toptext3.pack()
        
        button =  Button(self, text="Info",
                            command=lambda: controller.show_frame(InfoPage))
        button.pack()

        button2 =  Button(self, text="Quiz Yourself",
                            command=lambda: controller.show_frame(QuizPage))
        button2.pack()

        button3 =  Button(self, text="Play A Game",
                            command=lambda: controller.show_frame(QuizPage))
        button3.pack()
         
        botinfo = StringVar();
        botinfo.set("This project was built using Python for our EECE 507: \n Mathematical Methods for Computer Engineers class. The code \n was designed and written by Alena Yampolskaya and Jose Duque \n for consideration by Professor Linke Guo")
        
        bottext = Label(self,relief=GROOVE, bg= "#90DCF5", textvariable=botinfo, justify= CENTER)
        bottext.pack(side = BOTTOM)
        
            
class InfoPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Info", fg='red',font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        
        button1 =  Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Take a quiz!",
                            command=lambda: controller.show_frame(QuizPage))
        button2.pack()


class QuizPage( Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label =  Label(self, text="Quiz questions!! \n Or page two, actually.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        quizbutton = Button(self, text="Next Question")
        quizbutton.pack(side = TOP)
        
        button1 =  Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM)

        button2 =  Button(self, text="Info",
                            command=lambda: controller.show_frame(InfoPage))
        button2.pack(side = BOTTOM)
        
class GamePage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Let's play a game.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        playbutton = Button(self,text='Next Question')
        playbutton.pack(side = TOP)
        
        backbutton = Button(self,text='Back to Start');
        backbutton.pack(side = BOTTOM)
        
app = FrameWarden();
app.mainloop();      
