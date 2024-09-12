import random

#rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

 #Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
list_computer = [rock, paper,scissor]
user_input = int(input("What do you choose? Type 0 for Rock 1 for paper and 2 for scissor\n"))
print(list_computer[user_input])


print("Computer choose")
computer_choice = random.randint(0,2)
print(list_computer[computer_choice])

if user_input == 0 and computer_choice == 2:
    print("You win")
elif user_input ==2 and computer_choice == 2:
    print("you win")
elif user_input == 1 and computer_choice == 0:
    print("you win")
elif user_input == computer_choice:
    print("its a draw")
else:
    print("you loose")