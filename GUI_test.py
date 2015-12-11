#This code is based on http://pythonprogramming.net/change-show-new-frame-tkinter/

from Tkinter import *
from QuizState import QuizState
from LogicQuestion import LogicQuestion

LARGE_FONT= ("Consolas", 12)

class FrameWarden(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Math Methods Project by Jose and Alena');
        
        container = Frame(self)
        self.tainercon = container;
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        forms = {1:"If $noun is $adjective1 then it is $adjective2", 2: "$adjective1 implies $adjective2" , 3: "$noun is $adjective1 if it is $adjective2", 4:"If $noun is not $adjective1 then it is not $adjective2", 5: "Not $adjective1 implies not $adjective2", 6: "$noun is $adjective1 if it is $adjective2", 7:"If $noun is $adjective2 then it is $adjective1", 8:"$adjective2 implies $adjective1", 9:"$noun is $adjective2 if it is $adjective1", 10:"If $noun is not $adjective2 then it is not $adjective1", 11:"Not $adjective2 implies not $adjective1", 12:"$noun is not $adjective2 if it is not $adjective1"}
        nouns = ["Duck", "Cat","Dog","Elephant", "Pidgeon", "Mouse", "Lion", "Person", "Bearcat", "Horse", "Pig", "Scorpion", "Ant", "Jaguar", "Giraffe"]
        adjectives = ["Red","Sunny","Tepid","Green","Angry","Cautious","Raining", "Skiing", "Jumping", "Hiking", "Swimming", "Racing"]
        types = {1:"inverse", 2: "converse", 3:"contrapositive"}

        self.logic_question = LogicQuestion(nouns,adjectives,types,forms)        
        
        for F in (StartPage, InfoPage, QuizPage, GamePage, QuizQuestion):

            frame = F(self.tainercon, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont, *arguments, **keywords):
        if cont == QuizPage:
            self.quizstate = QuizState();
            self.quizstate.check_answer(keywords.get('choice'))
        elif cont == QuizQuestion:
            self.quizstate.check_answer(keywords.get('choice'))
            self.frames[QuizQuestion].refresh_question()
        if keywords.get('endquiz') == 'yes':
            print self.quizstate.get_result();
                
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
        
        button4 = Button(self, text="Quit",
                            command=lambda: controller.destroy())
        button4.pack()
         
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
        label =  Label(self, text="Start Of Quiz", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        self.current_question = controller.logic_question.get_question();
        
        #Get quiz question
        question_label = Label(self, text=self.current_question[0], font=LARGE_FONT);
        question_label.pack(pady=50,padx=50);
        
        #Get quiz answers
        v = StringVar();
        v.set('cat')
        
        for x in range(1,5):
            Radiobutton(self, text=self.current_question[x][0], variable=v, value=self.current_question[x][1]).pack(side='top')
        
        quizbutton = Button(self, text="Next Question", 
                            command=lambda: controller.show_frame(QuizQuestion,choice=v.get()))
        quizbutton.pack(side = TOP)
        
        button1 =  Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM)

        button2 =  Button(self, text="Info",
                            command=lambda: controller.show_frame(InfoPage))
        button2.pack(side = BOTTOM)
        
    def _quiz_update(self,controller):
        quiz_state.update_question_total;
        
class QuizQuestion(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        
        self.current_question = controller.logic_question.get_question();
        self.logic_question = controller.logic_question;
        
        #Get quiz question
        self.question_text = StringVar();
        self.question_text.set(self.current_question[0]);
        
        question_label = Label(self, textvariable=self.question_text, font=LARGE_FONT);
        question_label.pack(pady=50,padx=50);
        
        #Get quiz answers
        self.v = StringVar();
        self.v.set('cat')
        
        self.answer_text = [];
        self.answer_value = [];
        
        self.right_answer = StringVar();
        self.right_value = StringVar();
        
        self.right_answer.set(self.current_question[1][0]);
        self.right_value.set(self.current_question[1][1]);
        
        #for x in range(0,4):
               # Radiobutton(self, textvariable=self.answer_text[x], variable=self.v, value=self.answer_value[x]).pack(side='top')
        Radiobutton(self, textvariable=self.right_answer, variable=self.v, value=self.right_value).pack(side='top')
            
        quizbutton = Button(self, text="Next Question", 
                            command=lambda:controller.show_frame(QuizQuestion,choice=self.v.get()))
        quizbutton.pack(side = TOP)
        
        endbutton = Button(self,text="End Quiz",
                            command=lambda:controller.show_frame(StartPage,endquiz='yes'))
        endbutton.pack();
        
    def refresh_question(self):
        self.current_question = self.logic_question.get_question(); 
        self.question_text.set(self.current_question[0]);
        
        self.right_answer.set(self.current_question[1][0]);
        self.right_value.set(self.current_question[1][1]);
        
        self.v.set('new');
        
        
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
