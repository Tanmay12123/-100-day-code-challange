class QuizBrain():
    
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def chocie(self,):
        current_question = self.question_list[self.question_number]
        input(f"Q.{question_number} : {current_question}(True/False)")
        