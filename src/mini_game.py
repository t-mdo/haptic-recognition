##
## mini RPS game
##
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  'tie': "Yawn it's a tie!",
  'won': "Yay you won!",
  'lost': "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "Player: %s" % user_choice
  print "AI: %s" % computer_choice

  if user_choice == computer_choice:
      	print message['tie']
  ## check combinaisions when player wins
  elif user_choice == options[0] and\
       computer_choice == options[2]\
       or\
       user_choice == options[1] and\
       computer_choice == options[0]\
       or\
       user_choice == options[2] and\
       computer_choice == options[1]:
    print message['won']
  else:
    print message['lost']
  print ''
  print ' --- '
  print ''

def play_RPS():
  print "Rock, Paper, or Scissors?"
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

while 42:
	play_RPS()