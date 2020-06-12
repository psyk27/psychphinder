# coding: UTF-8
import pandas as pd
from colorama import init, Style
import sys
import os
from fuzzywuzzy import fuzz

init()
clear = lambda: os.system('cls')
counter = 0

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

df = pd.read_csv('dataframe.csv')

while True:
    # Introductiom
    logo = open('logo_mod.txt','r',encoding='UTF-8')
    print('\033[92m' + logo.read() + '\033[0m')
    print('\033[92m' + 'Welcome to psychphinder! One word, all lowercase, ph for the f.' + '\n' + 'Created by u/Psyk27 for the r/psych community.' + '\033[0m')
    sentence = input('\n' + "Enter a sentence: ")
    print('\n')

    for i in range(0, len(df)):
        Token_Set_Ratio = fuzz.token_set_ratio(sentence,df.iloc[i,4])
        if(Token_Set_Ratio >= 95) and (len(sentence) - 2 <= len(df.iloc[i,4])):
            counter += 1
            if(df.iloc[i,0] != 'ññ'):
                print(Style.BRIGHT + 'Season ' + str(df.iloc[i,0]) + ', Episode ' + str(df.iloc[i,1]) + ': ' + str(df.iloc[i,2]) + '. Time: ' + df.iloc[i,3] + Style.RESET_ALL +'\n' + str(df.iloc[i-1,4]) + '\n' + '\033[92m' + str(df.iloc[i,4]) + '\033[0m' + '\n' + str(df.iloc[i+1,4]) + '\n')
            else:
                print(Style.BRIGHT + 'Psych: The Movie' + '. Time: ' + df.iloc[i,3] + Style.RESET_ALL +'\n' + str(df.iloc[i-1,4]) + '\n' + '\033[92m' + str(df.iloc[i,4]) + '\033[0m' + '\n' + str(df.iloc[i+1,4]) + '\n')
    print("\n" + str(counter) + " coincidences were found. You know that's right." + "\n")
    ans = input('Would you like to search for another sentence? (y/n): ')
    if(ans == 'n'):
        break
    else:
        counter = 0
        clear()

print('\033[92m' + 'Suck it!')
input()
