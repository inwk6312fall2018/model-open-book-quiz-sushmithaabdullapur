class Card:
  def __init__(self,rank,suit):
     self.rank=rank
     self.suit=suit
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack$
  def __str__(self):
    return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
  def __lt__(self,other):
    t1=self.suit,self.rank
    t2=other.suit,other.rank
    print(t1,t2)
    return t1<t2
card1=Card(1,0)
card2=Card(2,3)
print(card1)
#if Card.suit_names[card1.suit]<Card.suit_names[card2.suit]:
  #print("card1 is less")
#else:
else:
 # print("card2 is greater")
class Desk:
  def __init__(self):
    self.cards=[]
    for suit in range (4):
      for rank in range(1,14):
          cards=Card(suit,rank)
          self.cards.append(cards)
  def __str__(self):
    res=[]
    for i in self.cards:
      res.append(str(i))
    return '\n'.join(res)
deck=Desk()
print(deck) 
