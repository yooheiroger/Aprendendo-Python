class QuizBrain:
    def __init__(self,list_question):
        self.list_question = list_question
        self.question_number = 0

    def show_question(self,list_question):
        print(f'Q.{self.question_number+1}: ',list_question[self.question_number].text)

    def cheking_answer(self,guess,list_question,add_points):
        if guess == list_question[self.question_number].answer:
            self.question_number += 1
            return True
        else:
            print("Wrong answer!")
            return False
    def last_question(self,list_question):
        if self.question_number >= len(list_question):
            print('You won the game!!!')
            return True
        return False



    def next_question(self,list_question):
        print(f'Q.{self.question_number+1}: ',list_question[self.question_number].text)






