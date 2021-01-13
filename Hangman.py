import random
from os import system
import sys

HANGMAN_ART = ['''
     ,+---------^
      \         |
      /         |
      \         |
                |
                |
                |
                |
                |
                |
                |
                |
           ===========''', '''
     ,+---------^
      \         |
      /         |
      \         |
      O         |
                |
                |
                |
                |
                |
                |
                |
           ===========''', '''
      ,+---------^
      \         |
      /         |
      \         |
      O         |
      |         |
                |
                |
                |
                |
                |
                |
           ===========''', '''
     ,+---------^
      \         |
      /         |
      \         |
      O         |
     /|         |
                |
                |
                |
                |
                |
                |
           ===========''', '''
     ,+---------^
      \         |
      /         |
      \         |
      O         |
     /|         |
     / \        |
                |
                |
                |
                |
                |
           ===========''', '''
     ,+---------^
      \         |
      /         |
      \         |
      O         |
     /|\        |
     / \        |
                |
                |
                |
                |
                |
           ===========''']
       
       
 
wordbank = 'time year people way car man thing woman life child world school state family student group country problem hand part place case week company system program'.split()
Playcounter = 0
userwins = 0
userloss = 0
def Clear():
	system('clear')
	
def mainTitle(user_wins, user_losses, games_played):
	on_menu = True
	print('''
 |  \/  |     (_)       |  \/  |                 
 | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _ 
 | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |
 | |  | | (_| | | | | | | |  | |  __/ | | | |_| |
 |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|
                                                 
                                                
To View Stats, type Stats!

To Play the Game type Go!

To Quit the game type Quit or Exit!                                     
                                                ''')
	if userwins > 0 | userloss > 0:                                     
		winrate = user_wins / user_losses
	else:
		winrate = 0
	user_input = input()
	if on_menu == True:
		if user_input.lower() == 'go':
			on_menu = False
			return True
		elif user_input.lower() == 'stats' or 'stat':
			Clear()
			print('''
  / ____|__   __|/\|__   __/ ____|
 | (___    | |  /  \  | | | (___  
  \___ \   | | / /\ \ | |  \___ \ 
  ____) |  | |/ ____ \| |  ____) |
 |_____/   |_/_/    \_\_| |_____/ 
                                  
                                  ''')
		
			print('''   _
||W |||I |||N |||S ||  (_)   
||__|||__|||__|||__||   _  
|/__\|/__\|/__\|/__\|  (_)   ''' + str(user_wins))
			print('''
 ____ ____ ____ ____ ____ ____    _
||L |||O |||S |||S |||E |||S ||  (_)   
||__|||__|||__|||__|||__|||__||   _    
|/__\|/__\|/__\|/__\|/__\|/__\|  (_)  ''' + str(user_losses))
			print('''                  _
||W |||I |||N |||R |||A |||T |||E ||  (_)   
||__|||__|||__|||__|||__|||__|||__||   _  
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|  (_)  ''' + str(winrate) + '%')
			print('''                                                _
|G |||A |||M |||E |||S |||       |||P |||L |||A |||Y |||E |||D | |  (_)   
||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__||   _   
|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|  (_) ''' + str(games_played))
			print()
			print('type back to go back to main menu')
			user_input = input()
			if user_input.lower() == 'back' or 'b':
				mainTitle(userwins, userloss, Playcounter)
			else:
				print('Please type b or back to go back to Main Menu')
				user_input = input()
		elif user_input.lower() == 'quit' or 'q':
			sys.exit()
		elif user_input.lower() == 'exit' or 'e':
			sys.exit()
		else:
			mainTitle(userwins, userloss, playcounter)
		
def gameDisplay(incorrect_letter, correct_letter, word):
	Clear()
	print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                 
''')


	print(HANGMAN_ART[len(incorrect_letter)])
	print('Letters missed = \n')
	for _char in incorrect_letter:
		print(_char, end=' ')
	print()
	
	blanks = '_' * len(word)
		
	for i in range(len(word)):
		if word[i] in correct_letter:
			blanks = blanks[:i] + word[i] + blanks[i+1:]
			
			for _char in blanks:
				print(_char, end =' ')
			print()
					
def getWord(_wordbank):
	index = random.randint(0, len(_wordbank) - 1)
	return _wordbank[index]


def getGuess(taken_letter):
	while True:
		print('Guess a letter')
		guess = input()
		guess = guess.lower() #make guess lowercase to test against alphabet
		if len(guess) != 1:
			print('Please enter ONE letter')
		elif guess in taken_letter:
			print('Letter has been taken already. Please enter another letter')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a ENGLISH LETTER')
		else:
			return guess

def playAgain():
	global Playcounter
	print('Would you like to play again? yes or no')
	user_playagain = input()
	user_playagain = user_playagain.lower()
	if user_playagain.lower() == 'yes':
		Playcounter +=1
		return 1
	elif user_playagain.lower() == 'no':
		return 0
	else:
		print('please enter yes or no')
		


missedChar = ''
correctChar = ''
word = getWord(wordbank)
gameOver = False

mainTitle(userwins, userloss, Playcounter)
while True:
	gameDisplay(missedChar, correctChar, word)
	
	guess = getGuess(missedChar + correctChar)
	
	if guess in word:
		correctChar = correctChar + guess
		
		#check if game won
		wordCorrect = True
		for i in range(len(word)):
			if word[i] not in correctChar:
				wordCorrect = False
				break
		if wordCorrect:
			userwins +=1
			print('''
					              *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *   CONGRATULATIONS!  *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    ''')
			gameOver = True
	else:
		missedChar = missedChar + guess
		
		if len(missedChar) == len(HANGMAN_ART) - 1:
			gameDisplay(missedChar, correctChar, word)
			print('''
 ___________.._______
| .__________))______|                       
| | / /      ||                                 
| |/ /       ||                           
| | /        ||.-''.                        
| |/         |/  _  \                        
| |          ||  `/,|                           
| |          (\\`_.'      YOU LOSE                  
| |         .-`--'.                             
| |        /Y . . Y\                   
| |       // |   | \\                   
| |      //  | . |  \\                    
| |     ')   |   |   (`                
| |          ||'||                             
| |          || ||                     
| |          || ||                  
| |          || ||                          
| |         / | | \                           
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .''')
			print('You have guess too many times and failed. \n You guessed: ' +
					str(len(missedChar)) + ' missed guesses & ' +
					str(len(correctChar)) + ' correct guesses. \n' +
					'The word was: ' + word)
			userloss +=1
			gameOver = True
	
	if gameOver:
		if playAgain() == 1:
			missedChar = ''
			correctChar = ''
			gameOver = False
			word = getWord(wordbank)
			Clear()
		else:
			mainTitle(userwins, userloss, Playcounter)
			
