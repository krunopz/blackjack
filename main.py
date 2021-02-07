############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack=21

user=list()
dealer=list()
u_score=0
d_score=0
#Starting the game... User and the dealer take two cards

for i in range(2):
  user.append(random.choice(cards))
  
dealer.append(random.choice(cards))

for num in user:
  u_score+=num

print(f"Your cards {user}, current score {u_score}")
print(f"Dealer's first card {dealer[0]}")


def draw(u_score):
  user.append(random.choice(cards))
  u_score=0
  for num in user:
    u_score+=num

  print(f"Your cards {user}, current score {u_score}")
  print(f"Dealer's first card {dealer[0]}")
  return u_score



#next step: to draw another card, or to stop
next=input("Type 'y' to get another card, type 'n' to pass: ")
if next!="y" and next!="n":
  next=input("You put a wrong input. Please type 'y' or 'n'")
  if next!="y" and next!="n":
    print("It seams that you don't want to play this game. Game over!")
    exit()
elif next=="y":
  while next=="y":
    draw(u_score)
    next=input("Type 'y' to get another card, type 'n' to pass: ")
    if next!="y" and next!="n":
      next=input("You put a wrong input. Please type 'y' or 'n'")
      if next!="y" and next!="n":
        print("It seams that you don't want to play this game. Game over!")
        exit()

#Player ends, dealer starts:
while d_score<=21 and d_score<=u_score and u_score<=21:
  dealer.append(random.choice(cards))
  d_score=0
  for n in dealer:
    d_score+=n

#results
def result(u_score,d_score):
  print(f"user:  {u_score}")
  print(f"dealer:  {d_score}")
  if u_score>d_score and u_score<=21:
    print("User wins.")
  elif d_score>u_score and d_score<=21:
    print("Dealer wins.")
  elif u_score==d_score and d_score<=21:
    print("Draw.")







print(f"Dealer got {dealer}, and his score is {d_score}")
result(u_score,d_score)



