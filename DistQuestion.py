#from Tkinter import *
import math
import random

class DistQuestion(object):
    def __init__(self, q_answer, q_questions):
        self.q_answer = q_answer
        self.q_questions = q_questions
        self.chosen_type = random.randint(1, (len(self.q_questions)))
	self.chosen_var_n = random.randint(5,9)
	self.chosen_var_r = random.randint(1,5)
	self.chosen_var_rchar= chr(self.chosen_var_r +48)
	self.chosen_var_nchar= chr(self.chosen_var_n +48)
	
    def get_question(self):
        self._generate_question()
        self._generate_answer()
        self._generate_wrong_answers()
        
        QUESTION = [(self.q_chosen_question),
                    (self.answer,'correct'),
                    (self.wronganswer1,'no'),
                    (self.wronganswer2,'bad'),
                    (self.wronganswer2,'wrong')]

        return QUESTION
        
    def _generate_question(self):
        self.chosen_type = random.randint(1, (len(self.q_questions)))
	self.q_chosen_question = self.q_questions[self.chosen_type]
	self.q_chosen_question= self.q_chosen_question.replace('$n1', self.chosen_var_nchar)
	self.q_chosen_question= self.q_chosen_question.replace('$n2', self.chosen_var_nchar)
	self.q_chosen_question= self.q_chosen_question.replace('$r1', self.chosen_var_rchar)
        return self.q_chosen_question
        
    def _generate_answer(self):
	self.answer = self.q_answer[self.chosen_type]
	self.interim1 = int(math.ceil((self.chosen_var_n / self.chosen_var_r)))
	self.answer= self.answer.replace('$n1', self.chosen_var_nchar)
	self.answer= self.answer.replace('$n2', self.chosen_var_nchar)
	self.answer= self.answer.replace('$r1', self.chosen_var_rchar)
	if self.chosen_type == 1 :
		self.answer= self.answer.replace('$n1', (chr(self.interim1+48)))
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
                if type(getattr(self,i)) != int:
                    x = getattr(self,i)
                    setattr(self, i, x.replace('$n1',self.chosen_var_nchar).replace('$n1',self.chosen_var_nchar).replace('$r2',self.chosen_var_rchar)) 
	
	return self.wronganswer1, self.wronganswer2, self.wronganswer3

# Normal, inverse, converse, contrapositive
questions = {1:"If there is $n1 video game players interested in playing a game, where there are only $r1 consoles, at least how many players must share a console?", 2: " How many ways can yo deal 5 cards to each of 2 players from a standard deck of 52 cards?", 3:"What is the minimum amount of people that must be in a room before you can guarantee at least 2 of them have the same favorite day of the week?", 4: "How many functions exist from a set of $r1 elements to a set with $n1 elements?", 5: "How many onto functions exist from a set of $r1 elements to a set of $n1 elements?", 6: "How many funtions from a set of $r1 elements to a set of $n1 elements are invertible?"}

answer = {1:"$n1",2:"C(52,5)*C(47,5)",3:"8",4:"($n1)^$r1",5:"S($r1,$n1)*$n2!",6:"$r1!",7:"$r1"}
#
dist_quest = DistQuestion(answer, questions)
#print DistributionQuestion._generate_question()
#print DistributionQuestion._generate_answer()
print dist_quest.get_question()
print dist_quest.get_question()
print dist_quest.get_question()