count = 0
# to set the count as 0
import random
sticks = random.randint(1,20)
print("How many sticks in the pile:", sticks)
# to random the number of sticks
print("There are",sticks, "in the pile")
# showing the number of sticks in the pile
name = input("What is your name? ")
# to ask for the player name
def x(sticks, pick):
  return print("There are ", sticks - pick, "sticks in the pile")
# set function to print the amount of stick that left
while sticks != 0:
  pick = int(input(name + " how many sticks you will take (1 or 2) "))
  #set the loop that if we still have sticks player need to take the stick out
  if pick == 1:
    x(sticks, pick)
    sticks = sticks - pick
    count = count + 1
  #pick stick out 1 the stick in the pile will decrease and show the stick that was left
  elif pick == 2 and sticks > 1:
    x(sticks, pick)
    sticks = sticks - pick
    count = count + 1
  #pick stick out 2 and the stick in the pile have to be more than 1 the stick in the pile will decrease and show the stick that was left
  elif pick == 2 and sticks < 2:
    print("There are no enough sticks to take")
  #If the stick in the pile is less than 2 and we want to pick to it will show that not enough sticks
  elif pick > 2 :
    print("No you can not take more than 2 sticks!")
  #show "No you can not take more than 2 sticks!" when input more than 2
  else :
    print("No you can not take less than 1 stick!")
  #show "No you can not take less than 1 stick!" when input less than 1
print("OK. There is no stick left in the pile. You spent", count, "times")
# after the sticks equal to 0, it will show the times that we use to play