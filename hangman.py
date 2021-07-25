#importing the libraries
import os, time, sys, random
try:
    from termcolor import colored
except ModuleNotFoundError:
    os.system('python3 -m pip install termcolor')
from termcolor import colored

#clearing the console before strating the game ;)
os.system('clear')

#variables
game_board = []
man = ''
wrong_choices = 0
running = True
zero = 0
choices = []
#copy the en_words.txt's path
file = open('en_words.txt', 'r')
word_list = []
#hangmanpics source/"https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c"
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while True:
    line = file.readline()
    if not line:
        break
    else:
        word_list.append(line)


def generate_word(language = 'en'):
    if language == 'en':
        word = random.choice(word_list)
    else:
        print("NOTE: WE DON'T SUPPORT YOUR LANGUAGE THE WOR WILL BE IN ENGLISH")
        word = random.choice(word_list)
    word = word.lower()
    return word

#generating the word
content = generate_word()

#making the board
for string in str(content):
    if string == ' ':
        game_board.append(' / ')
    else: 
        game_board.append('_ ')

#game class
class game():

    

    #drawing the game
    def draw_game():
        for element in game_board:
            print(element, end = '')
        print('\n')

    #the move function
    def move():
        zero = 0
        global wrong_choices
        choice = input('which letter? ')
        if choice == content:
            os.system('clear')
            print('the word was ' + colored(content, 'blue'))
            print(colored('YOU WON!', 'green'))
            sys.exit(0)
        choice = choice.lower()
        if choice in choices:
            print(colored('you have been used this letter!', 'red'))
            time.sleep(0.05)
        else:
            choices.append(choice)
        if choice in content:
            choice = choice
            for string in content:
                if string == choice:
                    game_board[zero] = choice + ' '
                zero += 1
        else:
            print('wrong choice')
            wrong_choices += 1

    #draws the man
    def draw_man():
        global man
        global running
        if wrong_choices == 0:
            pass 
        elif wrong_choices == 1:
            man = HANGMANPICS[0]
        elif wrong_choices == 2:
            man = HANGMANPICS[1]
        elif wrong_choices == 3:
            man = HANGMANPICS[2]
        elif wrong_choices == 4:
            man = HANGMANPICS[3]
        elif wrong_choices == 5:
            man = HANGMANPICS[4]
        elif wrong_choices == 6:
            man = HANGMANPICS[5]
        elif wrong_choices == 7:
            man = HANGMANPICS[6]
        else:
            print('you lost the word was ' + content)
            running = False
        print(colored(man, 'red'))

    #draws the moves that have been moved
    def draw_moves():
        for move in choices:
            print(colored(move + ' ', 'green'), end = '')

    #running the game while it's not over    
    while running:
        draw_game()
        move()
        os.system('clear')
        print('you have been used:')
        draw_moves()
        draw_man()

#running the game
game()

#quiting the code
quit()
