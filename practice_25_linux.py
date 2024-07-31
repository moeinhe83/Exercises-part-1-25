# Practice_25

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 25', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Get Average
avg = ((10+12+15+16+19+20+19+18+17)/9)

# Print Average
print('AVG ===> {0:.2f}'.format(avg))

# Finish
# Create By Moein Heshmati
