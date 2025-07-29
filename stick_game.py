def x(sticks,pile):
  return print("There are", sticks - pick ,"sticks left in the pile.")
# to make function for showing the amount os sticks that still in the pile
name = input("What is your name? ")
# to ask for the player name
sticks = int(input("numbers of stick:" ))
# to add the number of sticks
print("There are",sticks, "in the pile")
# showing the number of sticks in the pile
k = int(input("The maximum number of sticks that can be pick: "))
# to make the rule for number of stick that can pick
print("You can pick", k, "sticks per turn")
turn = "I"
# to set the turn for python
while sticks > 0:
  if turn == "I":
    if sticks <= k:
      pick = sticks
    # to make a program pick k if k is greater or equal to sticks
    else:
      pick = (sticks - 1) % (k + 1)
      if pick == 0:
          pick = 1
      #to calculate if sticks - 1 has no fraction, program will take 1 stick to give the program an advantage over player
    print("I take", pick , ",there are", sticks - pick, "sticks in the pile")
    # to print the number of stick that program pick
    sticks = sticks - pick
    if sticks == 0:
        print ("I take the last stick, YOU WON")
        turn = None
    # to set condition when program got the last stick, it will show that it lost and the turn won't change
    else:
        turn = "You"
    #to change turn to player
  else:
    pick = int(input("How many sticks will you take? : "))
    #to input the number of stick that player want to pick
    if pick >= 1 and pick <= k and pick <= sticks:
    #player need to pick more than 1 but less than k and the pick need to equal or less than stick in the pile
      x(sticks,pick)
      sticks = sticks - pick
      if sticks == 0:
        print("You take the last stick, I WON(Python WON)")
        #if sticks = 0 it will show "You take the last stick, I WON(Python WON)
      else:
        turn = "I"
        #to change turn back to program
    elif pick > sticks:
      print("There are no enough sticks to take")
      #condition when the sticks in the pile is less than the stick that player want to take.
    elif pick > k :
      print("No you can not take more than", k, "sticks!")
      #condition to prevent player take more sticks than the maximum number of stick that can take
    else :
      print("No you can not take less than 1 stick!") 
      #condition for prevent player take less than 1 stick   

#1. AI need to think in Winning position and losing position using modulo calculate. In the formula we need to minus 1 to make AI not the one who get the last stick.
# the losing postion is n ≡ 1 mod (k+1) or 1, k+2, 2k + 3 ... .If the AI in losing postion it will take 1 and make player in losing position.
#2. Yes, the AI should win every rounds.
#3. The strategy of the AI won't change.
