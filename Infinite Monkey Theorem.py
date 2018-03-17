# Created by EIA, March 2018.
# I am a beginner developer. I am not very good at it but i enjoy to it.

# Aim is to create the infinite monkey theorem again.

#needed stuff imported.
import random
import string

#alphabet created to pick random numbers and adding them to the letters variable.
alp = string.ascii_lowercase

#count variable to count letters.
count = 0
#string to find within the letters.
quote = input("what word do you want to generate: ")
#limitation to quote's lenght. it tooks a lot of time and consumes computer's energy.
print("waiting for computer to calculate...")
print("")
print("fun fact: the possibility to find your unique string is approximately 1/" + str((27**(len(quote)))))
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
