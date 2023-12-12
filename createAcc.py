import asciiStuff as asc
import displayFuncs as disp


def no_spaces(detail, player):

  for character in range(len(detail)):
    if detail[character] == " ":
      disp.clear()
      disp.createAcc_printer(player)
      print("\nThis cannot contain spaces")
      return True
    
  return False

def taken(username, player):

  with open("loginDetails.txt", "r") as file:
      for i, line in enumerate(file):
        thing = line.strip()
        thing = thing.split(" ")
        content = thing[0]
        if content == username:
          disp.clear()
          disp.createAcc_printer(player)
          print("\nUsername already taken")
          return True

  return False

def create_username(player):

  invalid = True
  
  while invalid:
    username = input("\nCreate username: ")
    if len(username) >= 2 and len(username) <= 30:
      invalid = taken(username, player)
      if invalid == False:
        invalid = no_spaces(username, player)
    else:
      disp.clear()
      disp.createAcc_printer(player)
      print("\nUsername must be between 2-30 characters long")
      continue

  disp.clear()
  disp.createAcc_printer(player)
  print("\nValid username")
  return username

def create_password(player):

  invalid = True

  while invalid:
    password = input("\nCreate password: ")
    if len(password) >=5 and len(password) <=30:
      invalid = no_spaces(password, player)
    else:
      disp.clear()
      disp.createAcc_printer(player)
      print("\nPassword must be between 5-30 characters long")
      continue

  print("\nValid password")
  return password

def name_writer(name, player):

  if player == '1':
    with open("currentPlayer1.txt", "w") as name1:
      name1.write(name)
  else:
    with open("currentPlayer2.txt", "w") as name2:
      name2.write(name)

def main(player):

  disp.clear()
  disp.createAcc_printer(player)
  
  details = []

  with open("loginDetails.txt", "a") as deets:
    details.append(create_username(player))
    details.append(create_password(player))
    deets.write(details[0] + " " + details[1] + "\n")

  name_writer(details[0], player)

  disp.clear()
  asc.ascii5()
  
