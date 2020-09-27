
"""0 — rock
1 — Spock
2 — paper
3 — lizard
4 — scissors"""

import random

def name_to_number(name):
  name = name.lower()
  if name == 'rock':
    return 0
  elif name == 'spock':
    return 1
  elif name == 'paper':
    return 2
  elif name =='lizard':
    return 3
  else:
    return 4  

def number_to_name(number):
  if number in range(5):
    if number == 0:
      return 'rock'
    elif number == 1:
      return 'Spock'
    elif number == 2:
      return 'paper'
    elif number == 3:
      return 'lizard'
    else:
      return 'scissors'
  else:
    return('Number out of range')

def rpsls(player_choice):
  print(" ")
  
  player_number = name_to_number(player_choice)
  print('You choose',player_choice)
  
  comp_number = random.randrange(5)
  comp_choice = number_to_name(comp_number)
  print('Computer choses',comp_choice)

  diff = player_number - comp_number
  if (diff % 5 == 3) or(diff % 5 == 4):
    return (print("Computer Wins! :)"))
  elif diff == 0:
    return (print("Tie Game :|"))
  else:
    return (print("You win! :( "))
  
# test your code
def player_input():
  player_choice = input("Enter your choice:  ")
  rpsls(player_choice)


while True:
  player_input()
  play_again = input("Do you want to play again?(y/n):  ")
  if play_again =='y':
    player_input()
    print(" ")
  else:
    print('Thank you, Bye!')
    break
