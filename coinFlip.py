import random

def main():
	play = True
	while(play):
		styleBoard()
		play = False
		#flip coin
		answer = flipCoin()
		#prompt user for guess
		guess = getGuessFromUser()
		#check if guess if correct
		if(guessedCorrectly(guess, answer)):
			print("Correct. It was {}!".format(answer))
			play = askToPlayAgain()
		else:
			#ask to play again
			print("Incorrect. It was {}.".format(answer))
			play = askToPlayAgain()
			
def styleBoard():
	print()
	print("------------------------------")
	print()

def flipCoin():
	number = random.randint(0, 2)
	if(number == 0): return "Heads".lower()
	return "Tails".lower()

def getGuessFromUser():
	return input("*Flips Coins*... Heads or Tails? ").lower()

def guessedCorrectly(guess, answer):
	if(answer == "heads"):
		if(guess == "heads" or guess == "h"):
			return True
	else:
		if(guess == 'tails' or guess == 't'):
			return True
	return False

def askToPlayAgain():
	answer = input("Would you like to play again? Y/N... ").lower()
	if(answer == 'yes' or answer == 'y'): return True
	print("Thank you for playing.")
	return False
		
if __name__ == "__main__":
	main()