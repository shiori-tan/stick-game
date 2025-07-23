import random
# to import random function
def x(sticks,pile):
  return print("There are", sticks - pick ,"sticks left in the pile.")
# to make function for showing the amount os sticks that still in the pile
name = input("What is your name? ")
# to ask for the player name
sticks = int(input("numbers of stick:" ))
# to add the number of sticks
print("There are",sticks, "in the pile")
# showing the number of sticks in the pile
turn = "I"
# to set the turn for python
while sticks > 0:
  if turn == "I":
    pick = random.randint(1, min(2, sticks))
    print("I take" ,pick , ",there are", sticks - pick, "sticks in the pile")
    sticks = sticks - pick
    #To make the program random 1 or 2 sticks
    if sticks == 0:
      print("I take the last stick, YOU WON")
      #if sticks = 0 it will show "I take the last stick, YOU WON"
    else:
      turn = "You"
      #if stick > 0, It change turn to player
  else:
    pick = int(input("How many sticks will you take? (1 or 2): "))
    # to input the number of stick that we will take
    if pick == 1 or (pick == 2 and sticks > 1):
      x(sticks,pick)
      sticks = sticks - pick
    #if we take 1 or 2 stick and the stick in the pile is more than 2 it will show the amount of stick that left in the pile
      if sticks == 0:
        print("You take the last stick, I WON(Python WON)")
        #if sticks = 0 it will show "You take the last stick, I WON(Python WON)
      else:
        turn = "I"
        #if stick > 0, It change turn to player 
    elif pick == 2 and sticks < 2:
      print("There are no enough sticks to take")
    # if player try to take 2 stick while the pile has stick less than 2 it will show "There are no enough sticks to take"
    elif pick > 2 :
      print("No you can not take more than 2 sticks!")
    #if player try to take more than 2 sticks it will show "No you can not take more than 2 sticks!"
    else :
      print("No you can not take less than 1 stick!")
    #if player try to take less than 1 stick it will show "No you can not take less than 1 stick!"
    #It won't change the playe until player take the stick out correctly

#1. It should take the stick in order to make the player need to play on 4 sticks.
#2. Yes, the AI should win every round.
#3. The strategy of the AI will change but it still has the similar pattern as before.
