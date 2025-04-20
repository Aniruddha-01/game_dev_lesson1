import random 
options = ["rock", "paper", "scissors"]
player_score = 0
comp_score = 0

for i in range(5):
   player = input("rock, paper or scissors?")
   player = player.lower() 
   computer = random.choice(options)
   print(f"computer chose {computer}")
   if player == computer:
      print("tie")
   elif player == "rock" and computer == "scissors" or player == "paper" and computer    == "rock" or player == "scissors" and computer == "paper":
      print("you win")
      player_score += 1
   elif player == "rock" and computer == "paper" or player == "paper" and computer ==       "scissors" or player == "scissors" and computer == "rock":
      print("you loose")
      comp_score += 1

if comp_score>player_score:
   print("you loose")
elif comp_score<player_score:
   print("you win!")
else:
   print("its a tie")

print(f"your final score:{player_score}/5")
