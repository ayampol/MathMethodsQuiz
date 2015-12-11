from Tkinter import *
from string import Template
import math
import random

class PermutationQuestion(object):
    
    def __init__(self, q_answer, q_questions):
        self.q_answer = q_answer
        self.q_questions = q_questions
        self.chosen_type = random.randint(0, (len(self.q_questions)))
	self.chosen_var_n = random.randint(6,9)
	self.chosen_var_r = random.randint(0,6)
        
    def _generate_question(self):
	self.q_chosen_question = self.q_questions[self.chosen_type]
	self.q_chosen_question = self.q_chosen_question.replace('%n', self.chosen_var_n)
	self.q_chosen_question = self.q_chosen_question.replace('%r', self.chosen_var_r)
        return self.q_chosen_question
        
    def _generate_answer(self):
	self.answer = self.q_answer[self.chosen_type] ;
	self.answer= self.answer.replace('$n1', self.chosen_var_n)
	self.answer= self.answer.replace('$n2', self.chosen_var_n)
	self.answer= self.answer.replace('$r1', self.chosen_var_r)
	self.answer= self.answer.replace('$r2', self.chosen_var_r)
	return self.answer
        return 0;

    def _generate_wrong_answers(self):
	i = 0
	for i in range(1, len(self.q_answer)):
		self.wronganswer1 = self.q_answer[i];
			if (self.wronganswer1 != self.answer):
				break
	for i in range(1, len(self.q_answer)):
		self.wronganswer2 = self.q_answer[i];
			if ((self.wronganswer2 != self.answer) && (self.wronganswer2 != self.wronganswer1)):
				break
	for i in range(1, len(self.q_answer)):
		self.wronganswer3 = self.q_answer[i];
			if ((self.wronganswer3 != self.answer) && ((self.wronganswer3 != self.wronganswer1) && (self.wronganswer3 != self.wronganswer2)):
				break
	return self.wronganswer1, self.wronganswer2, self.wronganswer3

# Normal, inverse, converse, contrapositive
questions = {""}

nouns = ["Duck", "Cat","Dog","Elephant", "Pidgeon", "Mouse", "Lion", "Person", "Bearcat", "Horse", "Pig", "Scorpion", "Ant", "Jaguar", "Giraffe"]
adjectives = ["Red","Sunny","Tepid","Green","Angry","Cautious","Raining", "Skying", "Jumping", "Hiking", "Swimming", "Racing"]
types = {1:"inverse", 2: "converse", 3:"contrapositive"}

logic_question = LogicQuestion(nouns,adjectives,types,forms)
print logic_question._generate_question()
print logic_question._generate_answer()
