# NOTES **
# I want to add the ability to choose your news provider or choose multiple or all if so desired
# if search comes up empty, suggest similar words to user (synonyms.com)
# add the ability for Wikipedia pages on relevant subjects to the user search
# add the ability for the user to choose world or US news
# add personal stocks
# TURN THIS INTO A PERSONAL ASSISTANT

import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
import wikipedia
import Personal_assistant_func
dictionary = PyDictionary()
P = Personal_assistant_func


def headlineScanner():

    NPR = ['NPR', 'npr', 'Npr', 'n.p.r.']
    CNN = ['CNN', 'cnn', 'C.N.N.']
    FOX = ['fox', 'FOX', 'Fox']

    keyword = input('What are you looking for?')
    sites = input('What website would you like to pull from?')

    if sites in NPR:
        P.npr(keyword, sites)
    elif sites in CNN:
        P.cnn(keyword, sites)
    elif sites in FOX:
        P.fox(keyword, sites)


headlineScanner()
