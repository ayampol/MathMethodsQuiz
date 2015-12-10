#!/usr/bin/python

from Tkinter import *

top = Tk()
top.title('Math Methods Project by Jose and Alena')

frame = Frame(top)
frame.pack()

########	MAIN WINDOW INTERFACE	 ########

# The frame that will determine the size of the window
mainframe = Frame(top, width=500, height=300)
mainframe.pack(side=TOP)
#mainframe.pack_propagate(0) Uncomment if auto-fit not desired


# Project Banner 
bannerframe = Frame(mainframe,bd=7, width=500, height=100, relief= RAISED, bg="blue")
bannerframe.pack(side = TOP)

img1= PhotoImage(file="images/header1.gif")
img2= PhotoImage(file="images/header2.gif")
img3= PhotoImage(file="images/header3.gif")
toptext = Label(bannerframe, image= img1, justify= CENTER)
toptext2 = Label(bannerframe, image= img2, justify= CENTER)
toptext3 = Label(bannerframe, image= img3, justify= CENTER)
toptext.pack()
toptext2.pack()
toptext3.pack()

#INFO BUTTON
infoframe = Frame(mainframe, bd=2)
infoframe.pack(side = TOP)

option1_button = Button(infoframe, text = "Info", fg="red")
option1_button.pack( side= TOP)
	
#QUIZ BUTTON
quizframe = Frame(mainframe, bd=2)
quizframe.pack(side = TOP)

quizbutton = Button (quizframe, text = "Quiz Yourself")
quizbutton.pack(side = TOP)

#GAME BUTTON
gameframe = Frame(mainframe, bd=2)
gameframe.pack(side = TOP)

gamebutton = Button (gameframe, text = "Play a game")
gamebutton.pack(side = TOP)

#End information
info_main_frame = Frame(mainframe, bd=2)
info_main_frame.pack(side = TOP)

endtext= StringVar()
endtext.set("This project was built using Python for our EECE 507: \n Mathematical Methods for Computer Engineers class. The code \n was designed and written by Alena Yampolskaya and Jose Duque \n for consideration by Professor Linke Guo")

toptext1 =  Label(info_main_frame, relief=GROOVE, bg= "#90DCF5", textvariable=endtext, justify= CENTER)
toptext1.pack()

#textframe = Frame(mainframe, width=450, height= 30)
#textframe.grid(row=0, column=1)

top.mainloop()
