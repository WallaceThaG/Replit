def save(person, quant, winningStats):

  if winningStats == True:
    fname = 'winners.txt'
  else:
    fname = 'losers.txt'

  with open(f"{fname}", "a") as file:
    file.write(f"{person} {quant}\n")

def higher_num(count1, count2):

  if count1 > count2:
    return count1, count2
  else:
    return count2, count1

def main(winner, loser, count1, count2):
  
  higher, lower = higher_num(count1, count2)
  save(winner, higher, True)
  save(loser, lower, False)
