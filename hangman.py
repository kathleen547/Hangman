import random
from wordlist import wordlist

def chooseAWord(wordlist):
    word = random.choice(wordlist)
    while True:
        if '-' in word or ' ' in word:
            word = random.choice(wordlist)
        else:
            break
    return word

w = chooseAWord(wordlist)
word = w.upper()
guessed1 = str('_' * len(word))
print(guessed1)
guessed = list(guessed1)
userLetters = set()
chances = 6

while True:
    print('Guess a letter: ')
    flag = True
    a = input()
    if a.isalpha():
        letter = a.upper()
    else:
        print('Wrong value! Try again')
        continue
    if letter in userLetters:
        flag = False
    userLetters.add(letter)
    print(userLetters)
    for number, i in enumerate(word):
        if letter == i:
            guessed[number] = letter
            flag = False
    if flag == True:
        chances -= 1
    print('Chances: ', chances)
    b = "".join(guessed)
    print(b)
    if chances == 0:
        print('You lost! The word is ', w)
        break
    if b.count('_') == 0:
        print('You won!')
        break