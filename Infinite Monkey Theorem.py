# Created by Enes Ihsan Aydogan, March 2018.
# I am 16 years old beginner developer. I am not very good at it but i like it.

# Aim is to create the infinite monkey theorem again.

#needed stuff imported.
import random

#alphabet created to pick random numbers and adding them to the letters variable.
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#count variable to count letters.
count = 0
#string to find within the letters.
quote = input("what word do you want to generate: ")
#limitation to quote's lenght. it tooks a lot of time and consumes computer's energy.
while len(quote) > 10:
    print("we cannot take an input longer than 10 characters for the safety of the computer, and it lasts too long.")
    quote = input("what word do you want to generate: ")
print("waiting for computer to calculate...")
print("")
print("fun fact: the possibility to find your unique string is approximately " + str((27**(len(quote)))))
print("")
letters = ""

#generating a random letter and adding it into the letters variable.
while not quote in letters:
    randChar = random.choice(alp)
    letters = (letters + randChar)
    #checking that if the quote is found
    if quote in letters:
        print(quote + ": it took " + (str(count)) + " letters to find the word " + quote)
        break
    #if quote couldn't found yet.
    else:
        count += 1

#printing results
print("")
print(letters)
print("")
print(count)
input("Press enter to contuniune... ")
