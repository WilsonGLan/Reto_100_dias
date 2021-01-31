from platform import system as sys
from os import system

def clean_screen():
    if sys() == 'Linux':        
        system("clear")
    else:        
        system("cls")