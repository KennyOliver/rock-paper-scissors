import random
#====================
def rps_game():
  print("\nEnter an item:\n\t[R] Rock\n\t[P] Paper\n\t[S] Scissors")
  
  player_item = input("\t--> ").upper()
  while player_item not in ['R','P','S']:
    player_item = input("\t--> ").upper()
  
  computer_rand_int = random.randint(1,3)
  if computer_rand_int == 1:
    computer_item = 'R'
  elif computer_rand_int == 2:
    computer_item = 'P'
  elif computer_rand_int == 3:
    computer_item = 'S'
  
  if player_item == 'R':
    if computer_item == 'R':
      print("Tie!")
    elif computer_item == 'P':
      print("You win!")
    elif computer_item == 'S':
      print("Computer wins!")
  
  elif player_item == 'P':
    if computer_item == 'R':
      print("Computer wins!")
    elif computer_item == 'P':
      print("Tie!")
    elif computer_item == 'S':
      print("You win!")
  
  elif player_item == 'S':
    if computer_item == 'R':
      print("Computer wins!")
    elif computer_item == 'P':
      print("You win!")
    elif computer_item == 'S':
      print("Tie!")
#====================
print("<-- ROCK PAPER SCISSORS -->")

run = 'Y'
while run in ['Y','YES']:
  rps_game()
  run = input("\nWould you like to play again?\n\t[Y] Yes\n\t[N] No\n\t--> ").upper()
  while run not in ['Y','YES','N','NO']:
    run = input("\t--> ").upper()