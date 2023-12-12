import asciiStuff as asc
import displayFuncs as disp
import sys


def password_validation(lineNum, player):

  with open("loginDetails.txt", "r") as file:

    for i, line in enumerate(file):
      if i == lineNum - 1:
        thing = line.strip()
        thing = thing.split()
        correctPass = thing[-1]
        break

  for x in range(4, -1, -1):
    if x == 0:
      return False
    password = input("\nEnter password: ")
    if correctPass == password:
      disp.clear()
      asc.ascii5()
      return True
    else:
      disp.clear()
      disp.login_printer(player)
      print("\nIncorrect password.", str(x - 1), "attempt(s) left")

def username_exists(username, player):

  with open("loginDetails.txt", "r") as file:

    lineNum = 0
    
    for i, line in enumerate(file):
      lineNum += 1
      thing = line.strip()
      thing = thing.split(" ")
      correctUser = thing[0]
      if correctUser == username:
        disp.clear()
        disp.login_printer(player)
        print("\nUsername found")
        return True, lineNum

    disp.clear()
    disp.login_printer(player)
    print("\nUsername not found")

    return False, None

def name_writer(name, player):

  if player == '1':
    with open("currentPlayer1.txt", "w") as name1:
      name1.write(name)
  else:
    with open("currentPlayer1.txt", "r") as f:
      foo = f.read()
    if foo == name:
      return True
    else:
      with open("currentPlayer2.txt", "w") as name2:
        name2.write(name)
      return False

def main(player):

  disp.clear()
  disp.login_printer(player)
  
  while True:
    username = input("\nEnter username: ")
    if player == '1':
      exists, lineNum = username_exists(username, player)
      if exists == True:
        valid = password_validation(lineNum, player)
        name_writer(username, player)
        return valid
    else:
      exists, lineNum = username_exists(username, player)
      if exists == True:
        sameName = name_writer(username, player)
        if sameName == False:
          valid = password_validation(lineNum, player)
          return valid
        else:
          print("\nPlease login with a different account to Player 1")
