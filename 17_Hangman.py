import random
from collections import Counter
WORDS = ['mango','cricket','butterfly']
word = random.choice(WORDS)
letter_guessed = ''
chances = len(word) + 3
correct = 0
flag = 0

for i in word:
    print('_', end=' ')
print()

try:
    while chances != 0 and flag == 0:
        print()
        chances -= 1
        try:
            guess = input('Guess a single letter: ')
        except:
            print('Enter only a letter!')
            continue
        if not guess.isalpha():
            print('Enter a LETTER!')
            continue
        elif len(guess) > 1:
            print('Enter a SINGLE letter!')
            continue
        elif guess in letter_guessed:
            print('You have already guessed this letter!')
            continue

        #if we guess correctly
        if guess in word:
            k = word.count(guess)
            for _ in range(k):
                letter_guessed += guess #letter guessed will be stored in l_t

        for char in word:
            if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                print(char, end=' ')
                correct = 1
            elif Counter(letter_guessed) == Counter(word):
                print('Congradulations! You have Won')
                print(word)
                flag = 1
                break
            else:
                print('_', end=' ')
            #if chances are used up
        if chances <= 0 and Counter(letter_guessed) != Counter(word):
            print('You lost! Try Again..')
            print(f'The word was {word}')
except KeyboardInterrupt:
    print('Try Again!')