# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:42:20 2022

@author: lodek
"""
#creating a dictionary

dict1 = {"A":"ALPHA",
         "B":"BRAVO",
         "C":"CHARLIE",
         "D":"DELTA",
         "E":"ECHO",
         "F":"FOXTROT",
         "G":"GOLF",
         "H":"HOTEL",
         "I":"INDIA",
         "J":"JULIET",
         "K":"KILO",
         "L":"LIMA",
         "M":"MIKE",
         "N":"November",
         "O":"Oscar",
         "P":"Papa",
         "Q":"QUEBEC",
         "R":"ROMEO",
         "S":"SIERRA",
         "T":"TANGO",
         "U":"UNIFORM",
         "V":"VICTOR",
         "W":"WHISKEY",
         "X":"X-RAY",
         "Y":"YANKEE",
         "Z":"ZULU"
         
         }

#looping through the input

rounds = int(input("HOW MANY PHONETICS DO YOU WANT TO KNOW ABOUT?\n"))


for number in range(rounds):
    print(dict1[str.upper(input("Enter a letter to get it's phonetic:\n"))]) #str.upper/lower eliminates case sensitivity
    

