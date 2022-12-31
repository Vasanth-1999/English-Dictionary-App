# Project 1 - English Dictionary App & Library Book Management System

# English Dictionary App
import json


def new_word():
    with open('words.txt', 'w') as new:
        words = input("Enter a word and its meaning sep by comma :")
        words = words.split(',')
        # wdict = {}
        global wdict
        wdict[words[0]] = words[1]
        json.dump(wdict, new)
        print('Added Successfully')
        # print(display())


def find_word():
    with open('words.txt', 'r') as find:
        word = input('Enter a word to find its meaning :')
        # global wdict
        wdict = json.load(find)
        print(wdict.get(word))


def update_word():
    with open('words.txt', 'w') as update:
        words = input("Enter a word to update its meaning is sep by comma :")
        words = words.split(',')
        global wdict
        wdict[words[0]] = words[1]
        json.dump(wdict, update)
        print("Updated Successfully")
        return update


def display():
    with open('words.txt', 'r') as show:
        print(show)

# def exits():
#     exit()


wdict = {}
print("Main Menu :")
print("Add a new word")
print("Find the meaning")
print("Update a word")
print("Exit")


while True:
    select = input("Enter any option :").title()
    if select == "Add a new word":
        new_word()
    elif select == "Find the meaning":
        find_word()
    elif select == "Update a word":
        update_word()
    elif select == 'Exit':
        print("Good Bye")
        # exit()
        break
    else:
        print("Invalid input")
