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

import random
print("Welcome to the game of rock paper scissors")
print("let the game begin!")
move=int(input("type 0 for rock, 1 for paper and 2 for scissors: "))

com=random.randint(0,2)

choices=[rock, paper, scissors]
print("\n\n")
print("you chose:")
print(choices[move])
print("computer chose:")
print(choices[com])

if move == com:
  print("its a tie")
elif move==0 and com==1:
  print("you lose (hihi)")
elif move==0 and com==2:
  print("you win")
elif move==1 and com==0:
  print("you win")
elif move==1 and com==2:
  print("you lose (hihi)")
elif move==2 and com==0:
  print("you lose(hihi)")
elif move==2 and com==1:
  print("you win")
else:
  print("invalid number! try agian")  
  