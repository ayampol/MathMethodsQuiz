class QuizState(object):
    def __init__(self):
        self.type = type;
        self.score = {'correct': 0, 'wrong': 0};
        self.total_questions = -1;
        self.questions_so_far = [];
        self.answers_so_far = [];

    def check_answer(self,choice,question_blob):
        self._update_question_total();
        self.questions_so_far.append(question_blob);
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
        