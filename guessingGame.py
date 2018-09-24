import random

def main():
	#pick a number
	limit = 100
	answer = getRandomNumber(limit)
	while(True):
		#prompt user for guess
		guess = getGuessFromUser(limit)
		#check guess relative to number
		if(guessedCorrectly(guess, answer)):
			print("You got it! The answer was {}.".format(answer))
			return
		#print higher, lower, or equal
		elif(higher(guess, answer)):
			print("Your guess was HIGHER than my number.")
		else:
			print("Your guess was LOWER than my number.")
		#repeat

def getRandomNumber(limit):
	return random.randint(0, limit+1)

def getGuessFromUser(limit):
	return int(input("Guess a number between 0 and {}... ".format(limit)))

def guessedCorrectly(guess, answer):
	if(guess == answer): return True
	return False

def higher(guess, answer):
	if(guess > answer): return True
	return False

if __name__ == "__main__":
	main()