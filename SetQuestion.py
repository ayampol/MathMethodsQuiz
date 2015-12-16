from Tkinter import *
from string import Template
import math
import random

class SetQuestion(object):
    
    def __init__(self, q_questions,q_A,q_B,q_C):
        self.q_questions = q_questions
	self.q_A = set(q_A)
	self.q_B = set(q_B)
	self.q_C = set(q_C)
        self.chosen_type = random.randint(0, (len(self.q_questions)))
	self.q_answer = [set.intersection(self.q_A,self.q_B), set.difference(self.q_B,self.q_A), set.union(self.q_A,self.q_B), set.intersection(self.q_B,self.q_C), set.difference(self.q_B,self.q_C), set.union(self.q_B,self.q_C), set.union(self.q_A,self.q_B,self.q_C), len(self.q_C)]

    def get_question(self):
        QUESTION = [(self._generate_question()),
                    (self._generate_answer(),'correct'),
		    (self._generate_wrong_answers()),
                    ('wrong answer','no'),
                    ('wrong answer','bad'),
                    ('wrong answer','wrong')]
        return QUESTION
        
    def _generate_question(self):
	self.q_chosen_question = self.q_questions[self.chosen_type] +"\n A= " + str(list(self.q_A)) + "\n B=" + str(list(self.q_B)) + "\n C=" + str(list(self.q_C)) + " \n"
        return self.q_chosen_question
        
    def _generate_answer(self):
	self.answer = self.q_answer[self.chosen_type]
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
	return self.wronganswer1, self.wronganswer2, self.wronganswer3

# Normal, inverse, converse, contrapositive
questions = ["What is the intersection of sets A and B?", "What is the difference between B and A?", "What is the Union of sets A and B?", "What is the intersection of sets B and C", "What is the difference between B and C?", "What is the Union of sets B and C?", "What is the Union of A, B, and C?", "What is the cardinality of set C?"]

q_A = [88,'Cat',20,5,4,'Dog',6,99,'Elephant',81,10]
q_B = [88,'TV',1,3,87,'Giraffe',11,'Car','Elephant','Wizard']
q_C = [2,'Cat',20,3,4,'Pants','Key','Car','Elephant','Wizard', 'Aadvark']

SetQuestion = SetQuestion(questions,q_A,q_B,q_C)
print SetQuestion._generate_question()
print SetQuestion._generate_answer()
