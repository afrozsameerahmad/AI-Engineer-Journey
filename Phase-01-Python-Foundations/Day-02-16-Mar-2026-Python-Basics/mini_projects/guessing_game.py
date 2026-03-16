import random
jackpot = random.randint(1, 100)
guess = int(input("Welcome to the Guessing Game  Guess the jackpot number between 1 and 100: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Too low guess higher.")
    else:
        print("Too high guess lower.")
    guess = int(input("Enter your guess: "))
    counter += 1
print(f"Congratulations You guessed the jackpot number {jackpot} in {counter} attempts.")  

#output
'''
Welcome to the Guessing Game  Guess the jackpot number between 1 and 100: 56
Too high guess lower.
Enter your guess: 43
Too low guess higher.
Enter your guess: 44
Too low guess higher.
Enter your guess: 46
Too high guess lower.
Enter your guess: 45
Congratulations You guessed the jackpot number 45 in 5 attempts.
'''
