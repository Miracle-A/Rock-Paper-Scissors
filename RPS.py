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

user_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n")

if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("You typed an invalid number, you lose")


random_selection = (f"{rock}, {paper}, {scissors}")
names = random_selection.split(", ")

import random
computer_choice = random.choice(names)
print(f"Computer choose:\n{computer_choice}")

if (user_choice == "0") and (computer_choice == paper):
    print("You lost, paper defeats rock")
elif (user_choice == "0") and (computer_choice == rock):
    print("You drew")
elif (user_choice == "0") and (computer_choice == scissors):
    print("You win, rock defeats scissors")
elif (user_choice == "1") and (computer_choice == scissors):
    print("You lose, scissors defeats paper ")
elif (user_choice == "1") and (computer_choice == paper):
    print("You drew")
elif (user_choice == "1") and (computer_choice == rock):
    print("You win, paper defeats rock")
elif (user_choice == "2") and (computer_choice == paper):
        print("You win, scissors defeats paper")
elif (user_choice == "2") and (computer_choice == scissors):
        print("You drew")
elif (user_choice == "2") and (computer_choice == rock):
        print("You lose, rock defeats scissors")
else:
    print("invalid number")
