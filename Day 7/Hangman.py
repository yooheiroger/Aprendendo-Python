import random
from Hangman_words import word_list
from Hangman_logo import stages, logo
from nltk.corpus import words


def generate_random_word():
    word_list = words.words()#nltk random word
    easy_words = [word for word in word_list if len(word) <= 6] # generates a word with 6 or less letters
    random_word = random.choice(easy_words)
    return random_word

def guess_the_word_right_choice(letter, list_word,hidden_word):
    for i in range(len(list_word)):
        if letter == list_word[i]:
            hidden_word[i] = letter
    return hidden_word
#
# def refresh_list_word(new_list, hidden_word):
#     for i in range(len(hidden_word)):
#         if new_list[i] == hidden_word[i]:
#             hidden_word.append(new_list[i])
#     return hidden_word

# def guess_the_word_wrong(letter, list_word):
#     lives = 0
#     for i in range(len(list_word)):
#         if letter != list_word[i]:
#             lives = 1
#     return lives
# GAME START HERE
stages = stages
logo_game = logo
letters_guessed = []
print('welcome to the hangman game')
print(logo_game)
# word = list(generate_random_word())
word = (random.choice(word_list))
print(word)
hidden_word = []
for i in range(len(word)):
    hidden_word.append('_')
lives = 6
print(stages[lives])
while lives > 0:
    print(f'---------------------- Lives remaining {lives}------------------')
    print(hidden_word)
    letter_choice = input('Please guess the letter').strip().lower()
    letters_guessed.append(letter_choice)
    correct_guess = False
    same_letter = False
    # print(letters_guessed)
    for i in range(len(letters_guessed)):
        if letter_choice == letters_guessed[i]:
            same_letter = True
    if same_letter == True:
        print(f'You already choose this letter ({letter_choice})')
    if letter_choice.isalpha():
        for i in range(len(word)):
            if letter_choice == word[i]:
                hidden_word = guess_the_word_right_choice(letter_choice, word, hidden_word)
                print(hidden_word)
                correct_guess = True
        letters_guessed.append(letter_choice)
        if not correct_guess:
            print(f'This letter it is not in the word ({letter_choice}). You lose a life')
            lives -= 1
        # if lives == 0:
        #     print('GAME OVER')
        #     print(stages[0])
        if hidden_word == word:
            print('Congratulation you won the game')
            break

    else:
        print('Invalid input, tyr again')
    print('''***************************************************************************************************************
    ''')
    if lives == 0:
        print('Game Over')
    print(stages[lives])




