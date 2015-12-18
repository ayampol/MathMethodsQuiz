from Tkinter import *
from string import Template
import math
import random

class SetQuestion(object):
    
    def __init__(self, q_questions,q_A,q_B,q_C):
        self.q_questions = q_questions
	self.src_A = set(q_A)
	self.src_B = set(q_B)
	self.src_C = set(q_C)
	self.q_A = set()
	self.q_B = set()
	self.q_C = set()
        self.chosen_type = random.randint(0, (len(self.q_questions)))

    def get_question(self):
        self._generate_sets(self.q_A)
        self._generate_sets(self.q_B)
        self._generate_sets(self.q_C)
        self._generate_question()
        self._generate_answer()
        self._generate_wrong_answers()
        
        QUESTION = [(self.q_chosen_question),
                    (self.wronganswer2,'wrong'),
                    (self.wronganswer1,'no'),
                    (self.answer,'correct'),
                    (self.wronganswer2,'bad')]
                    
        return QUESTION
        
    def _generate_question(self):

	self.q_chosen_question = self.q_questions[self.chosen_type] +"\n A= " + str(list(self.q_A)) + "\n B=" + str(list(self.q_B)) + "\n C=" + str(list(self.q_C)) + " \n"
        return self.q_chosen_question
        
    def _generate_sets(self,set_to_fill):
        z = random.randint(3,10);
        #set_to_fill = set()
        for i in range(0,z):
            x = random.randint(1,3)
            if x == 1: 
                set_to_fill.add(random.choice(q_A))
            elif x == 2:
                set_to_fill.add(random.choice(q_B))
            else:
                set_to_fill.add(random.choice(q_C))
        self.q_answer = [set.intersection(self.q_A,self.q_B), set.difference(self.q_B,self.q_A), set.union(self.q_A,self.q_B), set.intersection(self.q_B,self.q_C), set.difference(self.q_B,self.q_C), set.union(self.q_B,self.q_C), set.union(self.q_A,self.q_B,self.q_C), len(self.q_C)]
        return set_to_fill

        
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
#questions = ["What is the intersection of sets A and B?", "What is the difference between B and A?", "What is the Union of sets A and B?", "What is the intersection of sets B and C", "What is the difference between B and C?", "What is the Union of sets B and C?", "What is the Union of A, B, and C?", "What is the cardinality of set C?"]
##
#q_A = range(0,50);
#q_B = open("nouns.txt").read().splitlines()
#q_C = open("adjectives.txt").read().splitlines()
#
#set_quest = SetQuestion(questions,q_A,q_B,q_C)
#set_quest._generate_sets(set_quest.q_A)
#
#print set_quest.get_question()
