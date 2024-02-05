import random
import string
from words import words

def get_valid_word(words):
	'''Gets random word from a list of words
		keeps cycling through until no - or whitespace found

		Args: 
			words (list): a list of words separated by whitespace and hyphen			
	'''
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)

	return word.upper()

def hangman():
	'''Main game, keeps track of words and correct letters

	'''
	word = get_valid_word(words)
	word_letters = set(word)	#Letters in the word
	alphabet = set(string.ascii_uppercase)
	used_letters = set()	#Keeps track of used letters
	lives = 6
	#Gets user input
	while len(word_letters) > 0 and lives > 0:
		#Feedback on letters used 
		print("You have lives:", lives, "You have used letters ", ' '.join(used_letters))

		#Feedback on what the current word is. i.e (W _ O R D)
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Current word: ', ' '.join(word_list))
		user_input = input("Guess a letter: ").upper()
		if user_input in alphabet - used_letters: 
			used_letters.add(user_input)
			if user_input in word_letters:
				word_letters.remove(user_input)
			else:
				lives -= 1
		elif user_input in used_letters:
			print("You have already used this letter")
		else:
			print("Invalid character")

	if lives == 0:
		print("Sorry you lost. The word was", word)
	else:
		print("You did it, you guessed the word:", word)


if __name__ == '__main__':
    hangman()