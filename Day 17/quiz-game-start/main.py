from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    answer_text = question['answer'].lower()
    new_question = Question(question_text,answer_text)
    question_bank.append(new_question)
    # What was done here, it is normal get information from the internet or some data base in this format (look in data.py)
    # Convert in object

# print(question_bank[0].text)
# print(question_bank[0].answer)
points = 0
quiz_game = QuizBrain(question_bank)
game_on = True
while game_on:
    # questions.show_question(question_bank)
    quiz_game.next_question(question_bank)
    guess = input('Type "True" or "False": ').lower()
    while guess not in ['true', 'false']:
        guess = input('Type "True" or "False": ').lower()
    correct_incorrect= quiz_game.cheking_answer(guess, question_bank, points)
    if correct_incorrect:
        print('Correct answer, keep going')
        points += 1
        print(f'Your score: {points}')
    else:
        print(f'Your final score: {points}')
        game_on = False

    end_game = quiz_game.last_question(question_bank)
    if end_game:
        break
    print('-'*50)











