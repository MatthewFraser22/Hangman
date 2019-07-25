import random
from game import game

file = open('words.txt','r')
file2 = open('Graphics.txt','r')
word = ''

image = file2.readlines()
words = file.readlines()

x = random.randint(6,370102+1)
word = words[x]

word = word.strip()

win = game(word,image)

if win == True:
    print("Good word you have cracked the word!")
else:
    print("Good try, maybe next time.")




