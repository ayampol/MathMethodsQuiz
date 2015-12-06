from Tkinter import *
from string import Template
import math
import random

class LogicQuestion(object):
    
    def __init__(self, nouns, adjectives, q_types, q_forms):
        self.dict = dict(noun=nouns,adjective=adjectives);
        self.adjectives = adjectives;
        self.nouns = nouns;
        self.q_types = q_types;
        self.q_forms = q_forms;
        self.chosen_nouns = [];
        self.chosen_adjs = [];
        
    def _generate_question(self):
        #Choose a question type
        #Populate spots with labels or numbers
        request = random.choice(self.q_types);
        question = 'What is the ' + request + ' of \n\t';
        self.format = random.choice(self.q_forms);
        self._choose_labels();
        return question + self.format;
        
    def _generate_answer(self):
        #What did we ask for? request
        #Create 4 possible answers - the inverse, converse, contrapositive and something else
        #Inverse is toss in nots
        #Converse is flip question
        #Contrapositive is do both
        return 0;
        
    def _choose_labels(self):
        self.adjs_count = self.format.count("$adjective")
        self.nns_count = self.format.count("$noun")
        
        for c in range(self.adjs_count):
            self.chosen_adjs.append(random.choice(self.adjectives));
            self.format = self.format.replace('$adjective',self.chosen_adjs[-1],1);
            self.adjectives.remove(self.chosen_adjs[-1]);
            
        for c in range(self.nns_count):
            self.chosen_nouns.append(random.choice(self.nouns));
            self.format = self.format.replace('$noun',self.chosen_nouns[-1],1);

nouns = ["duck", "cat","dog","elephant"]
adjectives = ["red","sunny","tepid","green","angry","cautious","raining"]
types = ("inverse","contrapositive","converse")
forms = ( "If $noun is $adjective then it is $adjective", "$adjective implies $adjective", "$noun is $adjective if it is $adjective",)

logic_question = LogicQuestion(nouns,adjectives,types,forms);
print logic_question._generate_question();