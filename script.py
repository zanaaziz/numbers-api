# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:57:59 2017

@author: Zana
"""

import requests

number = input("Enter a whole number:\n")

if number.isdigit():
    response = requests.get("http://numbersapi.com/" + str(number))
    print("\n" + response.text)
    
else:
    print("You didn't enter a whole number, but here's a random number fact anyways!")
    
    import random
    random_number = random.randrange(1, 200)
    response = requests.get("http://numbersapi.com/" + str(random_number))
    print("\n" + response.text)