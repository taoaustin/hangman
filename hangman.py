import time

def HangMan(name,word):
    '''
    (str,str) -> number
    
    Plays a game of hangman and returns the number of turns
    the player has left once they solve the word. Returns 0
    if player loses.
    '''
    
    print("Hello, " + name, "time to play hangman!")
    print("")
    time.sleep(1)
    print("Start guessing...")
    time.sleep(0.5)
    guesses = ''
    turns = 10
    while turns > 0:         
        failed = 0             
        for char in word:      
            if char in guesses:    
                print(char, end=" ")   
            else:
                print("_", end=" ")    
                failed += 1
                
        if failed == 0:        
            print("\nYou won")
            return turns
        
        print("\n")
        guess_raw = input("guess a character: ").strip().lower()
        guess = guess_raw[0]
        
        if guess_raw == word:
            for char in guess_raw:
                print(char, end=" ")
            print("\nYou won")
            if failed > 1:
                return turns+1
            else:
                return turns
            
        guesses += guess                    
        if guess not in word:
            turns -= 1        
            print("Wrong")    
            print("You have", + turns, 'more guesses')
            if turns == 0:           
                print("You Lose")
                print("The correct word was: "+word)
                return 0


import random

def WordSelect(file):
    '''
    (file)->str

    Returns a random word in the given file that is strictly alphabetic.
    '''
    
    words_raw = open(file).read().lower().split()
    words = []
    for word in words_raw:
        if word.isalpha():
            if word not in words:
                words.append(word)
    return random.choice(words)


def Score(word,turns_left):
    '''
    (str,num)-> tuple or (str,num)

    Returns the given word and the score acheived in a tuple.
    '''
    
    word_sum = 0
    unique_char = ""
    scrabbleEn = {'a': 1, 'j': 8, 'y': 4, 'v': 4, 'e': 1,
              'b': 3, 'n': 1, 'u': 1, 'i': 1, 'l': 1,
              'q': 10, 'c': 3, 'w': 4, 'm': 3, 'p': 3, 
              's': 1, 'x': 8, 'g': 2, 'f': 4, 'z': 10, 
              'd': 2, 't': 1, 'r': 1, 'h': 4, 'k': 5, 'o': 1}
    for char in word:
        if char not in unique_char:
            word_sum += scrabbleEn[char]
            unique_char += char

    return (word, word_sum*(2**turns_left))


import datetime

def Log(name,score,log_file):
    '''
    (str,num,str)->None

    appends the time, name, and score acheived of a game of scrabble into log_file.
    '''
    
    dt = datetime.datetime.now()
    dt_str = str(dt.month)+"-"+str(dt.day)+"-"+str(dt.year)+"_"+\
             dt.time().isoformat("seconds")
    file = open(log_file, "a")
    file.write(dt_str+" "+name+" "+str(score)+"\n")
    







#main
name = input("What is your name? ")

word = WordSelect("Italian Campaign.txt")

turns = HangMan(name,word)

score = Score(word, turns)

score = score[1]

Log(name,score,"Record.txt")

print("Your final score is: " + str(score))
    




            
