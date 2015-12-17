from Tkinter import *
from DistQuestion import DistQuestion
from QuizState import QuizState
from LogicQuestion import LogicQuestion

import itertools
import random
import tkMessageBox

LARGE_FONT = ("courier new", 12)

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
        
        self.check_string = [];
        self.questions_so_far = '';
        self.seq_num = 0;
        
        forms = {1:"If $noun is $adjective1 then it is $adjective2", 2: "$adjective1 implies $adjective2" , 3: "$noun is $adjective1 if it is $adjective2", 4:"If $noun is not $adjective1 then it is not $adjective2", 5: "Not $adjective1 implies not $adjective2", 6: "$noun is $adjective1 if it is $adjective2", 7:"If $noun is $adjective2 then it is $adjective1", 8:"$adjective2 implies $adjective1", 9:"$noun is $adjective2 if it is $adjective1", 10:"If $noun is not $adjective2 then it is not $adjective1", 11:"Not $adjective2 implies not $adjective1", 12:"$noun is not $adjective2 if it is not $adjective1"}
        nouns = ["Duck", "Cat","Dog","Elephant", "Pidgeon", "Mouse", "Lion", "Person", "Bearcat", "Horse", "Pig", "Scorpion", "Ant", "Jaguar", "Giraffe"]
        adjectives = ["Red","Sunny","Tepid","Green","Angry","Cautious","Raining", "Skiing", "Jumping", "Hiking", "Swimming", "Racing"]
        types = {1:"inverse", 2: "converse", 3:"contrapositive"}
        
        questions = {1:"If there is $n1 video game players interested in playing a game, where there are only $r1 consoles, at least how many players must share a console?", 2: " How many ways can yo deal 5 cards to each of 2 players from a standard deck of 52 cards?", 3:"What is the minimum amount of people that must be in a room before you can guarantee at least 2 of them have the same favorite day of the week?", 4: "How many functions exist from a set of $r1 elements to a set with $n1 elements?", 5: "How many onto functions exist from a set of $r1 elements to a set of $n1 elements?", 6: "How many funtions from a set of $r1 elements to a set of $n1 elements are invertible?"}
        answer = {1:"$n1",2:"C(52,5)*C(47,5)",3:"8",4:"($n1)^$r1",5:"S($r1,$n1)*$n2!",6:"$r1!",7:"$r1"}

        self.logic_question = LogicQuestion(nouns,adjectives,types,forms)
        self.dist_question = DistQuestion(answer,questions)        
        
        for F in (StartPage, InfoPage, QuizPage, GamePage, QuizQuestion, ResultsPage):

            frame = F(self.tainercon, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont, *arguments, **keywords):
        if cont == QuizPage:
            self.quizstate = QuizState();
            self.questions_so_far = '';
            self.seq_num = 1;
            
        elif cont == QuizQuestion:
            self.quizstate.check_answer(keywords.get('choice'),keywords.get('question'))
            self._save_question(keywords.get('question'))
            self.frames[QuizQuestion].refresh_question();
            self.check_string.append(keywords.get('choice'));
            self.seq_num = self.seq_num + 1;
            if self.seq_num < 3:
                self.frames[QuizQuestion].logic_question = self.logic_question;
            else:
                self.frames[QuizQuestion].logic_question = self.dist_question;
            
        elif cont == ResultsPage:
            tkMessageBox.showinfo("Your Results",self.quizstate.get_result())
            self.frames[ResultsPage]._update_fields(self.questions_so_far,self.quizstate.get_result())
                
        frame = self.frames[cont]
        frame.tkraise()
        
    def _save_question(self,question_blob):
        for i in question_blob:
            if i != None:
                if len(i) == 2:
                    if str(i[1]) == 'correct':
                        curr_str = '\t' + str(i[0]) + ' <== Correct'+ '\n'
                    elif 'bad' == str(i[1]):
                        curr_str = '\t| You chose ~> ' + str(i[0]) + '\n'
                    else:
                        curr_str = '\t' + str(i[0]) + '\n'
                else:
                    curr_str = str(i) + '\n'
                self.questions_so_far = self.questions_so_far + curr_str;
        print self.questions_so_far
            
        
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
        #self._generate_question()
        self.current_question = controller.logic_question.get_question();
        print self.current_question
        #Get quiz question
        question_label = Label(self, text=self.current_question[0], font=LARGE_FONT);
        question_label.pack(pady=50,padx=50);
        
        #Get quiz answers
        v = StringVar();
        v.set('cat')
        
        for x in range(1,5):
            Radiobutton(self, text=self.current_question[x][0], variable=v, value=self.current_question[x][1]).pack(side='top')
        
        quizbutton = Button(self, text="Next Question", 
                            command=lambda: controller.show_frame(QuizQuestion,choice=v.get(),question=self.current_question))
        quizbutton.pack(side = TOP)
        
        button1 =  Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM)

        button2 =  Button(self, text="Info",
                            command=lambda: controller.show_frame(InfoPage))
        button2.pack(side = BOTTOM)
        
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
        
        self.ans_vals = [[StringVar(),''] for _ in range(0,4)]
        
        self.lst = [0,1,2,3];
        self.lst = set(itertools.permutations(list(self.lst))).pop();

        for x in range(1,5):
            self.ans_vals[x-1][0].set(self.current_question[x][0]);
            self.ans_vals[x-1][1] = self.current_question[x][1];
            
        self.ans_vals = random.choice(list(itertools.permutations(list(self.ans_vals))));         
        
        for x in self.lst:
            Radiobutton(self, textvariable=self.ans_vals[x][0], variable=self.v,value=self.ans_vals[x][1]).pack(side = 'top')
            
        quizbutton = Button(self, text="Next Question", 
                            command=lambda:controller.show_frame(QuizQuestion,choice=self.v.get(),question=self.current_question))
        quizbutton.pack(side = TOP)
        
        endbutton = Button(self,text="End Quiz",
                            command=lambda:controller.show_frame(ResultsPage,endquiz='yes'))
        endbutton.pack();
        
    def refresh_question(self):
        self.current_question = self.logic_question.get_question(); 
        self.question_text.set(self.current_question[0]);
        
        self.lst = set(itertools.permutations(list(self.lst))).pop();
        
        for x in self.lst:
            self.ans_vals[x][0].set(self.current_question[x+1][0]);
            self.ans_vals[x][1] = self.current_question[x+1][1];  
        
        self.ans_vals = random.choice(list(itertools.permutations(list(self.ans_vals))));  
        
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
        
class ResultsPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.results_label_text = StringVar();
        S = Scrollbar(self)
        self.T = Text(self, height=7, width=70)
        self.result_label = Label(self,textvariable=self.results_label_text,font=LARGE_FONT)
        
        self.result_label.pack(side='right')
        self.T.pack(side='left',fill=Y)
        S.pack(side='left',fill=Y)
        
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)
        
        self.T.config(state=DISABLED)
                
        homebutton = Button(self,text='Back to Start',
                            command=lambda: controller.show_frame(StartPage))
        homebutton.pack(side='bottom');
        
    def _update_fields(self,question_summary,result):
        self.results_label_text.set(result);
        self.T.config(state=NORMAL);
        self.T.delete(1.0,END);
        self.T.insert(END,question_summary);
        self.T.config(state=DISABLED)

        
        
app = FrameWarden();
app.mainloop();      
