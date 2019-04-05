#!/usr/bin/env python3

# This program converts Celsius to Fahrenheit or viceversa
# by Diego Saavedra-Kloss

from os import system, name

def formula():
    wdyw = input('''
    What do you want to convert?\n
    Type "c" for Celsius to Fahrenheit, or "f" for Fahrenheit to Celsius: ''')
    if wdyw.lower() == 'c':
        c_2_f()
    elif wdyw.lower() == 'f':
        f_2_c()
    else:
        _=system('clear')
        print('Typing "{}"" is incorrect. Please type either "c" or "f".'.format(wdyw))
        formula()

def c_2_f():
    while True:
        c_quest = input('\nEnter a number to convert from Celsius to Fahrenheit: ')
        try:
            type(c_quest) == float or type(c_quest) == int
            fahrenheit = float(c_quest) * (9/5) + (32)
            print("\n{} degrees Celsius is {} degrees Fahrenheit\n".format(c_quest, fahrenheit))
            break
        except ValueError:
            _=system('clear')
            print('Sorry, you must specify a number. For example: "23". \nPlease try again')

def f_2_c():
    while True:
        f_quest = input('\nEnter a number to convert from Fahrenheit to Celsius: ')
        try:
            type(f_quest) == float or type(f_quest) == int
            celsius = (float(f_quest) - 32) * (5/9)
            print("\n{} degrees Fahrenheit is {} degrees Celsius\n".format(f_quest, celsius))
            break
        except ValueError:
            _=system('clear')
            print('Sorry, you must specify a number. For example: "23". \nPlease try again')

def main():
    formula()

if __name__ == '__main__':
    main()
