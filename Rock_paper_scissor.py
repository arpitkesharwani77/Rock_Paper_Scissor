import random
print("Welcome to rock paper scissors game.")

print('''\nThe winning rules are:

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
''')
print('''choose :
1 for Rock ✊ 

2 for Paper 🫲

3 for scissors ✌️
''')
comp_score = 0
user_score = 0
tie = 0
repeat = "Yes"
while repeat == "Yes" or repeat == "yes":
  choice = {1: "Rock ✊", 2: "Paper🫲", 3: "Scissors✌️"}
  user = int(input("Enter your input: "))
  not_valid = True
  while not_valid:
    if user < 0 or user > 3:
      print("Invalid Input!\nPlease choose input from 1 to 3\n")
      user = int(input("Enter your input: "))
    else:
      print("You have choosen:", choice[user], "\n")
      not_valid = False

  comp = random.randint(1, 3)
  print("computer has choosen:", choice[comp], "\n")

  praising_words = [
      "well Done!", "Bravo!", "Splendid!", " Wonderful", "Congratulation!",
      "Marvellous!", "Amazing!", "Astonishing!", "Awesome!", "Spectacular!"
  ]

  print("The result is:")

  if (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3
                                                                and comp == 1):
    print("Computer Wins! 😒")
    comp_score += 1
  elif user == comp:
    print("Tie")
    tie += 1
  else:
    print(random.choice(praising_words), "You have won! 🎁")
    user_score += 1
  repeat = input(
      "\nDo you want to play again! Type 'yes' otherwise type 'exit': ")
print(f"The total score of computer is {comp_score}")
print(f"The total score of yours: {user_score}")
print(f"The total score of tie:{tie}")
if comp_score > user_score:
  print("The final winner is computer 😒")
elif comp_score < user_score:
  print("Congratulations! You are the final WINNER 🎁")
else:
  print("Tie")
