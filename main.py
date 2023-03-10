import random

def guess(x):
    random_number = random.randint(1, x) # returns a random number for you to guess between 1 and x
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f'Congratulations! You have guessed the number {random_number} correctly.')



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C)??').lower()
        if feedback == 'h':
            high = guess - 1 # adjusting the upper bound
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly')

computer_guess(1000)
