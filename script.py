# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:57:59 2017

@author: Zana
"""

# this package allows us to make HTTP requests
import requests

# user input prompt
number = input("Enter a whole number:\n")

# checks if the user input is valid, if true, it'll make a GET request using that number and respond with a fact about it
if number.isdigit():
    response = requests.get("http://numbersapi.com/" + str(number))
    print("\n" + response.text)

# if user input is not valid, it'll notify the user accordingly and then give them a fact about some random generated number
else:
    print("You didn't enter a whole number, but here's a random number fact anyways!")

    import random
    random_number = random.randrange(1, 200)
    response = requests.get("http://numbersapi.com/" + str(random_number))
    print("\n" + response.text)
