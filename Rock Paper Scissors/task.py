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

print("Let's play ROCK, PAPER, SCISSORS!!")
choice = int(input("Type 0 for ROCK, 1 for PAPER, and 2 for SCISSORS\n"))
computer_choice = random.randint(0,2)

if choice == 0:
    print("You have chosen ROCK")
    print(rock)
elif choice == 1:
    print("You have chosen PAPER")
    print(paper)
elif choice == 2:
    print("You have chosen SCISSORS")
    print(scissors)
else:
    print("INVALID OPTION.")

print("-----------------------------------------")
print("The computer plays...")
if computer_choice == 0:
    print("ROCK!")
    print(rock)
if computer_choice == 1:
    print("PAPER!")
    print(paper)
if computer_choice == 2:
    print("SCISSORS!")
    print(scissors)
print("-----------------------------------------")
if (choice == 0 and computer_choice == 0) or (choice == 1 and computer_choice == 1) or (choice == 2 and computer_choice == 2):
    print("DRAW!")
if (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print("You LOSE!")
if (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You WIN!")