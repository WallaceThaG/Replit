import os
import asciiStuff as asc

def clear():

  os.system("clear")

def login_printer(player):
  
  if player == '1':
    asc.ascii1()
  else:
    asc.ascii2()

def createAcc_printer(player):

  if player == '1':
    asc.ascii3()
  else:
    asc.ascii4()

def endgame_printer(winner, names):

  if winner == names[0]:
    asc.ascii7()
  else:
    asc.ascii8()

def playGame_printer(thing1, thing2, names):

  asc.ascii6()
  print(f"\n{names[0].capitalize()} has [{thing1}] cards   ------   {names[1].capitalize()} has [{thing2}] cards")
  print("\nPress ENTER to draw a card from the top of the deck")
  
