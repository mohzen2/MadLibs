#This project focuses on using string concatenation to combine elements, basically how to put strings together.
import numpy as np

#user = ",my name is Joe " # input string variable

# # multiple ways is can be done
# print("Hello world " + user)
# print("Hello world {}".format(user))
# print(f"Hello world {user}")
def madlib():

    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous Person: ")

    madlib = f"Copmuter programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

    print(madlib)

madlib()

#This is the basic premise and now we can combine multiple Madlib prompts to create a cohesive Madlib story or increase any number of strings and variables