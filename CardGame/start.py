import random
import asciiStuff as asc
import login
import createAcc
import playGame
import displayFuncs as disp

colours = ['Black', 'Red', 'Yellow']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
players = ['1', '2']
names = []


def write_names():

  with open("currentPlayer1.txt", "r") as name1:
    content = name1.read()
    names.append(content)

  with open("currentPlayer2.txt", "r") as name2:
    content = name2.read()
    names.append(content)


def create_deck():

  deck = []

  for colour in colours:
    for value in values:
      card = f"{colour} {value}"
      deck.append(card)

  return deck


def play(deck, names):

  playGame.main(deck, names)


def authorise(deck):

  def guest_login(player):

    with open(f"currentPlayer{player}.txt", "w") as gFile:
      gFile.write(f"guest{player}")

  for player in players:
    disp.clear()
    asc.ascii5()
    if player == '1':
      asc.ascii7()
      flipFlop = True
    else:
      asc.ascii8()
      flipFlop = False

    while True:
      decision = input(
        f"\nPlayer {player}, please:\n -> Login with an existing account [1]\n -> Create a new account [2]\n -> Play as guest [3]\nENTER: "
      )
      if decision not in ('1', '2', '3'):
        disp.clear()
        asc.ascii5()
        if flipFlop == True:
          asc.ascii7()
        else:
          asc.ascii8()
        print("\nInvalid, please try again")
      elif decision == '1':
        valid = login.main(player)
        if valid == False:
          return valid
        break
      elif decision == '2':
        createAcc.main(player)
        break
      else:
        guest_login(player)
        break

  write_names()
  play(deck, names)


def play_again():

  disp.clear()
  asc.ascii10()

  while True:
    print("\nPlay again? [Y/N]")
    answer = input(" -> ").lower()
    if answer not in ('y', 'n'):
      disp.clear()
      asc.ascii10()
      print("\nInvalid please try again")
      continue
    elif answer == 'y':
      disp.clear()
      return True

    return None


def main(reset, firstGame):

  while True:
    deck = create_deck()
    random.shuffle(deck)
    if firstGame == True and reset == None:
      break
    if firstGame == True and reset == True:
      firstGame = False
    if reset == False and firstGame == True:
      valid = authorise(deck)
      if valid == False:
        break
      firstGame == False
      reset = play_again()
    elif reset == True and firstGame == False:
      deck = create_deck()
      random.shuffle(deck)
      play(deck, names)
      firstGame == False
      reset = play_again()
    else:
      break

  print("\nBye!")
