def game(word,graphics):
    done = False
    badguesses = 0
    FAIL = 11
    length = len(word)
    guesses = []
    blank = []
    wordarray = []
    count = 0
    cd = 11
    win = False
    
    print("Begin by guessing a letter you have 11 chances:")
    print()
    print("'#guessed' to list all guessed attempts")
    print()
    print("The word is {} long".format(length))
    print()
    for i in range(length):
        blank.append("_")  
    while badguesses < FAIL and win == False:
        print(blank)
        userguess = input("Enter, type '#guessed' to see guessed letters: ")
        while userguess in guesses:
            userguess = input("Enter, type '#guessed' to see guessed letters: ")
        
        if userguess == '#guessed':
            print(guesses)
        
        elif userguess not in word:
            print()
            cd -= 1
            print("Letter not found, you have {} guesses remaning".format(cd))
            print()
            for i in range(0,badguesses):
                print(graphics[i])
            badguesses += 1

        elif userguess in word:
            count = 0
            while count < length:
                if word[count] == userguess:
                    index = word.find(userguess)
                    blank[count] = userguess
                count += 1
        if userguess == word:
            win =  True
        else:
            for i in word:
                wordarray.append(i)
            if blank == wordarray:
                win = True       
        guesses.append(userguess)
    
    return win