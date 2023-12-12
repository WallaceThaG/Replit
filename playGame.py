import asciiStuff as asc
import displayFuncs as disp
import saveStats
from colorama import *
from time import sleep

p1Current = ''
p2Current = ''

def card_drawer(card):

  val = card[-1]
  col = card[0]

  for value in range(1,11):
    if val != '0':
      space = ' '
      fill = '_'
      if int(val) == value:
        v = val
        break
    else:
      v = '10'
      space = ''
      fill = ''

  if col == 'R':
    c = Back.RED
  elif col == 'Y':
    c = Back.YELLOW
  else:
    c = Back.BLACK

  tb = Back.BLACK
  
  end = Style.RESET_ALL

  asciiCard = ['+_______+',
               f'|{tb + v + end}{c + space}     |{end}',
               '|       |',
               f'|   {tb + col + end}{c}   |{end}',
               '|       |',
               f'|_____{fill}{tb + v + end}{c}|{end}',
               '+       +']

  return asciiCard, c, end

def same_colour():

  if p1Current.startswith(p2Current[0]):
    return True, p1Current[0], p2Current[0]

  return False, p1Current[0], p2Current[0]

def higher(sharedCurrents, names, sharedCards):

  def printer(num):

    print(f"\n{names[num].capitalize()} got the higher value card! {names[num].capitalize()} steals!")

  val1 = int(sharedCurrents[0][-1])
  if val1 == 0:
    val1 = 10
  val2 = int(sharedCurrents[1][-1])
  if val2 == 0:
    val2 = 10
  
  if val1 > val2:
    printer(0)
    card_collection(0, 1, sharedCurrents, sharedCards)
    return True
  else:
    printer(1)
    card_collection(1, 0, sharedCurrents, sharedCards)
    return False

def card_collection(list, other, sharedCurrents, sharedCards):

  sharedCards[list].append(sharedCurrents[list])
  sharedCards[list].append(sharedCurrents[other])

def colour_comparison(col1, col2, sharedCurrents, names, sharedCards):

  def printer(num, wum):

    if wum == 0:
      phrase = 'Red beats black'
    elif wum == 1:
      phrase = 'Yellow beats red'
    else:
      phrase = 'Black beats yellow'

    print(f"\n{phrase}! {names[num].capitalize()} steals!")
  
  rb = ['R', 'B']
  yr = ['Y', 'R']
  
  if col1 in rb and col2 in rb:
    if col1 == 'R':
      printer(0, 0)
      card_collection(0, -1, sharedCurrents, sharedCards)
      return True
    else:
      printer(1, 0)
      card_collection(1, 0, sharedCurrents, sharedCards)
      return False
  elif col1 in yr and col2 in yr:
    if col1 == 'Y':
      printer(0, 1)
      card_collection(0, -1, sharedCurrents, sharedCards)
      return True
    else:
      printer(1, 1)
      card_collection(1, 0, sharedCurrents, sharedCards)
      return False
  else:
    if col1 == 'B':
      printer(0, 2)
      card_collection(0, -1, sharedCurrents, sharedCards)
      return True
    else:
      printer(1, 2)
      card_collection(1, 0, sharedCurrents, sharedCards)
      return False

def turn(deck, name, sharedCurrents):

  global p1Current, p2Current

  topCard = deck[-1]

  asciiCard, c, end = card_drawer(topCard)
  
  print(f"\n{name.capitalize()} draws: \n")

  for line in asciiCard:
    print(c + line + end)
  
  with open("currentPlayer1.txt", "r") as file:
    content = file.read()
    if content == name:
      p1Current = topCard
      sharedCurrents.append(p1Current)
    else:
      p2Current = topCard
      sharedCurrents.append(p2Current)

def game_loop(player1Count, player2Count, deck, names, player1Cards, player2Cards, sharedCards):

  size = len(deck)
  
  for card in range(size, 0, -1):
    size = len(deck)
    if size % 2 == 0: 
      sharedCurrents = []
      turn(deck, names[0], sharedCurrents)
      input("\n -> ")
    else:
      turn(deck, names[1], sharedCurrents)
      sameColour, p1CurrentCol, p2CurrentCol = same_colour()
      if sameColour == True:
        higherValue = higher(sharedCurrents, names, sharedCards)
        if higherValue == True:
          player1Count += 2
        else:
          player2Count += 2
      else:
        winningColour = colour_comparison(p1CurrentCol, p2CurrentCol, sharedCurrents, names, sharedCards)
        if winningColour == True:
          player1Count += 2
        else:
          player2Count += 2
      input("\n -> ")
      disp.clear()
      disp.playGame_printer(player1Count, player2Count, names)
    deck.pop()

  return player1Count, player2Count, player1Cards, player2Cards

def endgame(player1Count, player2Count, names, player1Cards, player2Cards):

  if player1Count > player2Count:
    winner = names[0]
    loser = names[1]
    diff = player1Count - player2Count
    winningCards = player1Cards
  else:
    winner = names[1]
    loser = names[0]
    diff = player2Count - player1Count
    winningCards = player2Cards

  saveStats.main(winner, loser, player1Count, player2Count)

  def epic_reveal(winningCards):  
  #This function is the best thing ever achieved in programming history

    disp.clear()
    
    for card in range(len(winningCards)):
      print("\n")
      sleep(0.03)
      asciiCard, c, end = card_drawer(winningCards[card])
      for line in range(len(asciiCard)):
        if card % 2 == 0:
          print(" "*line + c + asciiCard[line] + end)
          sleep(0.03)
        else:
          space = 7 - line
          print(" "*space + c + asciiCard[line] + end)
          sleep(0.03)

    print("\nPress ENTER to continue")
    input(" -> ")
  
  disp.clear()
  asc.ascii10()
  print(f"\nCongratulations {winner.capitalize()}! You won by {diff} cards!")
  print("\nPress ENTER to reveal the winning cards!")
  input(" -> ")

  epic_reveal(winningCards)

  disp.clear()
  asc.ascii9()
  disp.endgame_printer(winner, names)

  valid = True

  while True:
    disp.clear()
    asc.ascii9()
    disp.endgame_printer(winner, names)
    if valid == False:
      print("\nInvalid, please try again")
    print("\nWould you like to see your cards again? [Y/N]")
    answer = input(" -> ").lower()
    if answer not in ['y','n']:
      valid = False
    elif answer == 'y':
      valid = True
      epic_reveal(winningCards)
    else:
      break

def main(deck, names):

  player1Count = 0
  player2Count = 0
  player1Cards = []
  player2Cards = []
  sharedCards = [player1Cards, player2Cards]

  disp.clear()
  disp.playGame_printer(player1Count, player2Count, names)
  input()

  p1Count, p2Count, p1Cards, p2Cards = game_loop(player1Count, player2Count, deck, names, player1Cards, player2Cards, sharedCards)
  endgame(p1Count, p2Count, names, p1Cards, p2Cards)
