import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you chose?")
player_choice = input("Type 0 for Rock, 1 for Paper and 2 for Scissors ")

if player_choice == "0":
  print(f"You chose: \n{rock}")
elif player_choice == "1":
  print(f"You chose: \n{paper}")
elif player_choice == "2":
  print(f"You chose: \n{scissors}")
else:
  print("This option does not exist")

random_choice = random.randint(0,2)

if random_choice == 0:
  print(f"Computer chose: \n{rock}")
elif random_choice == 1:
  print(f"Computer chose: \n{paper}")
elif random_choice == 2:
  print(f"Computer chose: \n{scissors}")

if player_choice == str(random_choice):
  print("It's a draw")
elif (player_choice == "0" and random_choice == 2) or (player_choice == "1" and random_choice == 0) or (player_choice == "2" and random_choice == 1):
  print("You win")
else:
  print("You lose")

