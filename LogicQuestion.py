from Tkinter import *
from string import Template
import math
import random

class LogicQuestion(object):
    
    def __init__(self, nouns, adjectives, q_types, q_forms):
        self.adjectives = adjectives
        self.nouns = nouns
        self.q_types = q_types
        self.q_forms = q_forms
        self.chosen_nouns = []
	self.chosen_adj = []
	self.chosen_adj2 = []
	self.chosen_adj = random.choice(adjectives)
	self.chosen_adj2 = random.choice(adjectives)
        
    def _generate_question(self):
        #Choose a question type
        #Populate spots with labels or numbers	
	self.answertype = random.randint(1, 3)
        request = self.q_types[self.answertype]
        question = 'What is the ' + request + ' of \n\t'
	#y= len(self.q_forms) / 4 # get the number of entries in the dict, then divide by 4 (normal, converse, inverse, contrapositive)
	self.x= random.randint(1,(len(self.q_forms) / 4)) # change this number based on the total number of forms
        self.format = self.q_forms[self.x]
        self._choose_labels()
        return question + self.format
        
    def _generate_answer(self):
	self.answer = self.q_forms[(self.answertype * 3) + self.x];
	self.answer = self.answer.replace('$noun',self.chosen_nouns[-1],1)
	self.answer= self.answer.replace('$adjective1', self.chosen_adj)
	self.answer= self.answer.replace('$adjective2', self.chosen_adj2)
	return self.answer
        return 0;
        
    def _choose_labels(self):
	self.format = self.format.replace('$adjective2',self.chosen_adj2)
	self.format = self.format.replace('$adjective1',self.chosen_adj)
	
        self.chosen_nouns.append(random.choice(self.nouns));
        self.format = self.format.replace('$noun',self.chosen_nouns[-1],1)

# Normal, inverse, converse, contrapositive
forms = {1:"If $noun is $adjective1 then it is $adjective2", 2: "$adjective1 implies $adjective2" , 3: "$noun is $adjective1 if it is $adjective2", 4:"If $noun is not $adjective1 then it is not $adjective2", 5: "Not $adjective1 implies not $adjective2", 6: "$noun is $adjective1 if it is $adjective2", 7:"If $noun is $adjective2 then it is $adjective1", 8:"$adjective2 implies $adjective1", 9:"$noun is $adjective2 if it is $adjective1", 10:"If $noun is not $adjective2 then it is not $adjective1", 11:"Not $adjective2 implies not $adjective1", 12:"$noun is not $adjective2 if it is not $adjective1"}

nouns = ["Duck", "Cat","Dog","Elephant", "Pidgeon", "Mouse", "Lion", "Person", "Bearcat", "Horse", "Pig", "Scorpion", "Ant", "Jaguar", "Giraffe"]
adjectives = ["Red","Sunny","Tepid","Green","Angry","Cautious","Raining", "Skying", "Jumping", "Hiking", "Swimming", "Racing"]
types = {1:"inverse", 2: "converse", 3:"contrapositive"}

logic_question = LogicQuestion(nouns,adjectives,types,forms)
print logic_question._generate_question()
print logic_question._generate_answer()
