import random

def pickGuess(number):
	if(number == 1):return 1 
	return (int)(number/2)
	
def squareGuess(guess):
	return guess**2

def foundRoot(guessSquared, number, uncertainty):
	return ((guessSquared + uncertainty > number) and (guessSquared - uncertainty < number))

def computeNewGuess(guess, guessSquared, number):
	return (guess + (number/guess))/2

def root(number):
	if(number == 0): return "No root"
	guess = pickGuess(number)
	guessSquared = squareGuess(guess)
	uncertainty = 0.001
	while(True):
		#print(guess)
		if(foundRoot(guessSquared, number, uncertainty)):
			return guess
		guess = computeNewGuess(guess, guessSquared, number)
		guessSquared = squareGuess(guess)
		
def main():
	number = int(input("Give me a number: "))
	print("The square root of {} is approximately... {}".format(number, root(number)))
	
main()