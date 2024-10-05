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

hand=[rock,paper,scissors]
import random
user=input("What do you want to choose? Type 0 for rock, 1 for paper and 2 for scissors")
user=int(user)
print(hand[user])
computer=random.randint(0,2)
print("Computer chose:\n")
print(hand[computer])
if user==0 and computer==2:
    print("you win!")
elif user==2 and computer==0:
    print("You lose!")
elif user>computer:
    print("you win!")
elif user<computer:
    print("you lose!")
elif user==computer:
    print("It's a tie")
else:
    print("Invalid input")