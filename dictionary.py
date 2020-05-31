# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:21:22 2020

@author: Aaditree Jaisswal
"""

import json
data = json.load(open(r"C:\Users\Aaditree Jaisswal\Desktop\Guided Projects\dictionary_compact.json"))

n = input("Enter the word you want to search :")

if n in data:
    print(data[n])
