from Tkinter import *
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
	
    def get_question(self):
        self._generate_question()
        self._generate_answer()
        self._generate_wrong_answers()
        #print self.wronganswer1,'+',self.wronganswer2,'+',self.wronganswer3
        QUESTION = [(self.question),
                    (self.answer,'correct'),
                    (self.wronganswer1,'no'),
                    (self.wronganswer2,'bad'),
                    (self.wronganswer3,'wrong')]
                    
        return QUESTION
        
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
        self.question = question + self.format
        return question + self.format
        
    def _generate_answer(self):
	self.answer = self.q_forms[(self.answertype * 3) + self.x];
	self.answer = self.answer.replace('$noun',self.chosen_nouns[-1],1)
	self.answer= self.answer.replace('$adjective1', self.chosen_adj[-1])
	self.answer= self.answer.replace('$adjective2', self.chosen_adj2[-1])
	return self.answer

    def _generate_wrong_answers(self):
	i = 0
	for i in range(0, 2):
	       self.wronganswer1 = self.q_forms[(i * 3) + self.x];
	       if (self.wronganswer1 != self.answer):
				break
	for i in range(0, 2):
	       self.wronganswer2 = self.q_forms[(i * 3) + self.x];
	       if ((self.wronganswer2 != self.answer) and (self.wronganswer2 != self.wronganswer1)):
				break
	i= 0
	while(1):
		i = i+1;
		self.wronganswer3 = self.q_forms[i];
		if ((self.wronganswer3 != self.answer) and (self.wronganswer3 != self.wronganswer1) and (self.wronganswer3 != self.wronganswer2)):
				break
	self._label_wrong_answers()			
	return self.wronganswer1, self.wronganswer2, self.wronganswer3
	
        
    def _choose_labels(self):
        self.chosen_adj.append(random.choice(self.adjectives))
	self.chosen_adj2.append(random.choice(self.adjectives))
	self.format = self.format.replace('$adjective2',self.chosen_adj2[-1])
	self.format = self.format.replace('$adjective1',self.chosen_adj[-1])
	
        self.chosen_nouns.append(random.choice(self.nouns));
        self.format = self.format.replace('$noun',self.chosen_nouns[-1],1)
        
    def _label_wrong_answers(self):
        for i in vars(self):
            if 'wronganswer' in i:
                x = getattr(self,i)
                #print x.replace('$adjective2',self.chosen_adj2[-1]).replace('$adjective1',self.chosen_adj[-1]).replace('$noun',self.chosen_nouns[-1],1)
                setattr(self, i, x.replace('$adjective2',self.chosen_adj2[-1]).replace('$adjective1',self.chosen_adj[-1]).replace('$noun',self.chosen_nouns[-1],1))      


# Normal, inverse, converse, contrapositive
forms = {1:"If $noun is $adjective1 then it is $adjective2", 2: "$adjective1 implies $adjective2" , 3: "$noun is $adjective1 if it is $adjective2", 4:"If $noun is not $adjective1 then it is not $adjective2", 5: "Not $adjective1 implies not $adjective2", 6: "$noun is $adjective1 if it is $adjective2", 7:"If $noun is $adjective2 then it is $adjective1", 8:"$adjective2 implies $adjective1", 9:"$noun is $adjective2 if it is $adjective1", 10:"If $noun is not $adjective2 then it is not $adjective1", 11:"Not $adjective2 implies not $adjective1", 12:"$noun is not $adjective2 if it is not $adjective1"}

nouns = ["Duck", "Cat","Dog","Elephant", "Pigeon", "Mouse", "Lion", "Person", "Bearcat", "Horse", "Pig", "Scorpion", "Ant", "Jaguar", "Giraffe"]
adjectives = ["Red","Sunny","Tepid","Green","Angry","Cautious","Raining", "Skiing", "Jumping", "Hiking", "Swimming", "Racing","Shrieking","Happy"]
types = {1:"inverse", 2: "converse", 3:"contrapositive"}

logic_question = LogicQuestion(nouns,adjectives,types,forms)
print logic_question.get_question()

