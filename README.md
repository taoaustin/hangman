# hangman

This program is an implementation of Hangman written in Python.

This is randomly pick a word from the file "Italian Campaign.txt" (and makes sure no numbers or punctuation symbols are attached such as "positions." or "1944,".

the words point value is based off of Scrabble letter values, and (scrabble_value * (2**(guesses_remaining))) is the score formula.

The score is then recorded in a file "Record.txt" (and creates it if it doesn't exist in the same directory as hangman.py) along with the name and date.
