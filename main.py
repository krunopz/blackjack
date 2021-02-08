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

user=list()
dealer=list()
u_score=0
d_score=0

#####FIRST ROUND####################

for i in range(2):
  user.append(random.choice(cards))
  
dealer.append(random.choice(cards))

for num in user:
  u_score+=num

print(f"Your cards {user}, current score {u_score}")
print(f"Dealer's first card {dealer[0]}")
d_score+=dealer[0]

### Whan drawing a card add it to sum
def draw(u_score):
  drawn_card=random.choice(cards)
  if u_score<=10 and drawn_card==11:
    user.append(11)
    u_score=u_score+11
  elif u_score>10 and drawn_card==11:
    user.append(1)
    u_score+=1
  else:
    user.append(drawn_card)
    u_score+=drawn_card
  #PLAYER LOST if he went over 21
  if u_score>21:
      print(f"Your cards {user}, current score {u_score}. You lose!")
      exit()
  else:
    print(f"Your cards {user}, current score {u_score}")
    print(f"Dealer's first card {dealer[0]}")
  return u_score
  return user



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
    if u_score>21:
      print("You lose! Sorry")
      exit
    else:
      next=input("Type 'y' to get another card, type 'n' to pass: ")
      if next!="y" and next!="n":
        next=input("You put a wrong input. Please type 'y' or 'n'")
        if next!="y" and next!="n":
          print("It seams that you don't want to play this game. Game over!")
          exit()
      else:

      #Player ends, dealer starts:
        while d_score<=21 and d_score<=u_score and u_score<=21:
          dealer.append(random.choice(cards))
          d_score=0
          for n in dealer:
            d_score+=n
elif next=='n':
   while d_score<=21 and d_score<=u_score and u_score<=21:
          dealer.append(random.choice(cards))
          d_score=0
          for n in dealer:
            d_score+=n

#results
def result(user,dealer):
  user_final=0
  dealer_score=0
  for i in user:
    user_final+=i
  for i in dealer:
    dealer_score+=i
  if user_final>dealer_score and user_final<=21:
    print("User wins.")
  elif dealer_score>user_final and dealer_score<=21:
    print("Dealer wins.")
  elif user_final==dealer_score and dealer_score<=21:
    print("Draw.")
  elif user_final<dealer_score and dealer_score>21:
    print("User wins.")
  elif user_final>21 and dealer_score<=21:
    print("Dealer wins.")


print(f"Dealer got {dealer}, and his score is {d_score}")
result(user,dealer)



