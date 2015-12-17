class QuizState(object):
    def __init__(self):
        self.type = type;
        self.score = {'correct': 0, 'wrong': 0};
        self.total_questions = 0;
        self.questions_so_far = '';
        self.answers_so_far = [];

    def check_answer(self,choice,question_blob):
        self._update_question_total();
        curr_str = '';
        
        for i in question_blob:
            print str(i) + ' <--- That\'s an i!!'
            if i != None:
                if len(i) == 2:
                    if str(i[1]) == 'correct':
                        curr_str = '\t' + str(i[0]) + ' <== Right answer!'+ '\n'
                    elif choice == str(i[1]):
                        curr_str = 'You chose ~>' + str(i[0]) + '\n'
                    else:
                        curr_str = '\t' + str(i[0]) + '\n'
                else:
                    curr_str = str(i) + '\n'
                self.questions_so_far = self.questions_so_far + curr_str;
        
        if (choice == 'correct'):
            self._rightanswer();
        else:
            self._wronganswer();
        
    def _update_question_total(self):
        self.total_questions = self.total_questions + 1;
    
    def _rightanswer(self):
        self.score['correct'] = self.score['correct'] + 1;
        
    def _wronganswer(self):
        self.score['wrong'] = self.score['wrong'] + 1;
        
    def get_result(self): 
        result = 'You got ' + str(self.score['correct']) + ' out of ' + str(self.total_questions) + ' correct. '
        return result;
        
