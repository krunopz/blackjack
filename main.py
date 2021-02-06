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
  score+=num

print(f"Your cards {user}, current score {score}")