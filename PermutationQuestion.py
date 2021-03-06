from Tkinter import *
from string import Template
import math
import random

class PermutationQuestion(object):
    
    def __init__(self, q_answer, q_questions):
        self.q_answer = q_answer
        self.q_questions = q_questions
        self.chosen_type = random.randint(1, (len(self.q_questions)))
	self.chosen_var_n = chr(random.randint(6,9)+48)
	self.chosen_var_r = chr(random.randint(0,6)+48)

    def get_question(self):
        self._generate_answer()
        self._generate_wrong_answers()
        
        QUESTION = [(self._generate_question()),
                    (self.wronganswer1,'no'),
                    (self.wronganswer2,'bad'),
                    (self.wronganswer2,'wrong'),
                    (self.answer,'correct')]
                    
        return QUESTION
        
    def _generate_question(self):
	self.q_chosen_question = self.q_questions[self.chosen_type]
	if self.chosen_type == 2 or self.chosen_type == 7 :
		self.q_chosen_question= self.q_chosen_question.replace('$n', self.chosen_var_n)
	if self.chosen_type == 3 or self.chosen_type == 4 or self.chosen_type == 5 or self.chosen_type == 6:
		self.q_chosen_question= self.q_chosen_question.replace('$n', self.chosen_var_n)
		self.q_chosen_question= self.q_chosen_question.replace('$r', self.chosen_var_r)
        return self.q_chosen_question
        
    def _generate_answer(self):
	self.answer = self.q_answer[self.chosen_type]
	self.answer= self.answer.replace('$n', self.chosen_var_n)
	self.answer= self.answer.replace('$r', self.chosen_var_r)
	return self.answer

    def _generate_wrong_answers(self):
	i = 0
	for i in range(1, len(self.q_answer)):
		self.wronganswer1 = self.q_answer[i];
		if self.wronganswer1 != self.answer:
			break
	for i in range(1, len(self.q_answer)):
		self.wronganswer2 = self.q_answer[i];
		if self.wronganswer2 != self.answer and self.wronganswer2 != self.wronganswer1:
			break
	for i in range(1, len(self.q_answer)):
		self.wronganswer3 = self.q_answer[i];
		if self.wronganswer3 != self.answer and self.wronganswer3 != self.wronganswer1 and self.wronganswer3 != self.wronganswer2:
			break
	for i in vars(self):
            if 'wronganswer' in i:
                x = getattr(self,i)
                setattr(self, i, x.replace('$n',self.chosen_var_n[-1]).replace('$r',self.chosen_var_r[-1]))      
	
	return self.wronganswer1, self.wronganswer2, self.wronganswer3

# Normal, inverse, converse, contrapositive
questions = {1:"How many terms are in the expansion of (a+b+c+d)*(a+b+c+e)*(x,y,z)?", 2:"How many unique binary strings can be made of length $n", 3: "What is the number of ways $r students can be seated in a class with $n seats?", 4: "What is the  number of ways a bag of $n+2 donuts can be formed with $r types of donuts?", 5: "What is the number of patterns that can be formed by stacking $n wooden blocks if there are $r types of blocks?", 6: "How many ways can $n adults and $r children are to be lined up such that no 2 children are standing next to one another. In how many ways can this be done?", 7: "How many $n letter strings can be formed from the english alphabet", 8: "How many ways can the letters MISSISSIPPI be arranged?"}

answer = {1:"12",2:"2^$n",3:"C($n,$r)",4:"P($n+$r+1!,$r-1)",5:"C($n+$r-1, $r-1)",6:"P($n,$n) * P($n+1,$r)", 7: "26^$n", 8: "11! / (4!*2!*4!)"}

types = {1:"inverse", 2: "converse", 3:"contrapositive"}
#
#PermutationQuestion = PermutationQuestion(answer, questions)
#print PermutationQuestion._generate_question()
#print PermutationQuestion._generate_answer()
#print PermutationQuestion.get_question()
