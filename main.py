from random import randint;

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
  out=""
  if len(hand)==2 and calculateHand(hand)=="21":
    out+="Black Jack!"

def showHands():
  print ("Your hand "+printList(playerHand)+"\nTotal = "+calculateHand(playerHand))
  blackJack(playerHand)
  print("\n")
  print("Dealer hand " +printList(dealerHand)+"\nTotal = "+calculateHand(dealerHand))
  blackJack(dealerHand)

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

dealHands()
showHands()


#GAME########################################
