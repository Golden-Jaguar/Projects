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

#Write your code below this line 👇
import random

#print(computer_input)
#if user_input == 0
def Loop():
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    #user_input = int(input1)
    computer_input = random.randint(0, 2)
    print(computer_input)
    if user_input in range(0, 3):
        if user_input == 0 and computer_input == 0:
            print(rock)
            print("Computer Chose:")
            print(rock)
            print("Tie.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 0 and computer_input == 1:
            print(rock)
            print("Computer Chose:")
            print(paper)
            print("You Lose.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 0 and computer_input == 2:
            print(rock)
            print("Computer Chose:")
            print(scissors)
            print("You Win!!")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 1 and computer_input == 0:
            print(paper)
            print("Computer Chose:")
            print(rock)
            print("You Win.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 1 and computer_input == 1:
            print(paper)
            print("Computer Chose:")
            print(paper)
            print("Tie.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 1 and computer_input == 2:
            print(paper)
            print("Computer Chose:")
            print(scissors)
            print("You Loser.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 2 and computer_input == 0:
            print(scissors)
            print("Computer Chose:")
            print(rock)
            print("You Lose.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
        elif user_input == 2 and computer_input == 1:
            print(scissors)
            print("Computer Chose:")
            print(paper)
            print("You Win!")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."

        elif user_input == 2 and computer_input == 2:
            print(scissors)
            print("Computer Chose:")
            print(scissors)
            print("Tie.")
            r = input("Would you like to restart this program?").lower()
            if r == "yes" or r == "y":
                Loop()
            if r == "n" or r == "no":
                print
                "Script terminating. Goodbye."
    else:
        print("Input our of Range")
        r = input("Would you like to restart this program?")
        if r == "yes" or r == "y":
            Loop()
        if r == "n" or r == "no":
            print
            "Script terminating. Goodbye."


Loop()

