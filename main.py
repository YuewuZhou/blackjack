from random import randint;

#returns the string number value
def calculateHand (hand):
  value=0
  ace=0
  for card in hand:
    if card=="J" or card=="Q"or card=="K":
      value=value+10
    elif card=="A":
      value+=11
      ace+=1
    else:
      value+=card
  while ace>0:
    if value<22:
      return str(value)
    else:
      value-=10
      ace-=1
  return str(value)

def addCard(hand,times):
  for a in range(0,times):
    hand.append(cards[randint(0,12)])

def dealHands():
  playerHand.clear()
  addCard(playerHand,2)
  dealerHand.clear()
  addCard(dealerHand,2)

def printList(hand):
  output=""
  for each in hand:
    output+="["+str(each)+"] "
  return output

def blackJack(hand):
  if len(hand)==2 and calculateHand(hand)=="21":
    return True
  return False

def showHands():
  print()
  print ("Your hand "+printList(playerHand)+"\nTotal = "+calculateHand(playerHand))
  print("\n")
  print("Dealer hand " +printList(dealerHand)+"\nTotal = "+calculateHand(dealerHand))
  print()

def playAgain():
  response=input('Would you like to play again Y/N ?\n')
  if response=="Y" or response=="y":
    return True
  elif response=="N"or response=='n':
    return False
  else:
    print("That is not a valid response. The game will now exit")
    return False

def hit(hand):
  addCard(hand,1)
  showHands()
  if int(calculateHand(hand))<22:
    return True
  else:
    return False

def stay():
  response=input("Would you like to hit? Y/N\n")
  if response=='Y' or response =='y':
    return False
  elif response=="N"or response=='n':
    return True
  else:
    print("That is not a valid response.")
  
def dealersTurn(hand):
  while int(calculateHand(hand))<16:
    addCard(hand,1)

def showResult(playerHand,dealerHand):
  if int(calculateHand(dealerHand))>21 :
    print("You win!")
  elif int(calculateHand(playerHand))>int(calculateHand(dealerHand)) and int(calculateHand(playerHand))<22:
    print("You win!")
  elif int(calculateHand(playerHand))==int(calculateHand(dealerHand)):
    print("Push. It's a draw.")
  else:
    print("You have lost.")

#SETUP###########################################
#players=0
cards=[]
for i in range(2,11):
 cards.append(i)
cards.append("J")
cards.append("Q")
cards.append("K")
cards.append("A")
playerHand=[]
dealerHand=[]

#FUNCTIONS########################################

while True:
  dealHands()
  showHands()
  if blackJack(playerHand):
    print("You win!")
  elif blackJack(dealerHand):
    print("You have lost.")

  counter=True
  while counter:
    if stay():
      break
    counter=hit(playerHand)
  dealersTurn(dealerHand)
  showHands()
  showResult(playerHand,dealerHand)
  if not playAgain():
    break
  print("#########################")
