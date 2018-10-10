import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard
class Card:
  def __init__(self,suit,rank):
     self.suit=suit
     self.rank=rank
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack$
  def __str__(self):
    return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
class Deck:
  def __init__(self):
    self.cards = []
    for suit in range (4):
      for rank in range (1, 14):
        card = Card(suit, rank)
        self.cards.append(card)
  def deal(self):
if (len(self.names)==0):
       return None
    else:
       return self.names.pop(0)

  def shuffle(self):
      print(random.shuffle(self.cards))
class Player:

    def __init__(self, name: str):
       self.hand = []
        self.name = name

    def __str__(self):
        return self.name
class Poker:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck(cards=generate_deck(),name='Poker deck',reshuffle=False)
        self.players = players
        self.table_cards = []
        print("Created a table with {} players".format(len(self.players)))
    def dealer(self, num_hands):
#dealer starts game by pack of cards 
        list_hands=[]
        for j in range (num_hands):
            list_hands.append(self.deck.deal())
        self.names.append(list_hands)
    def flop(self):
# burn the card  and add  new card is placed on the table
      remove = self.deck.draw()
      self.deck.discard(remove)
      print("removed a card: {}".format(removed))
      for _ in range(0, 3):
        card = self.deck.draw()
        self.table_cards.append(card)
        print("New card on the table: {}".format(card)
#new card on table and they will raise the betting    
    def call(self):
      remove = self.deck.draw()
      self.deck.discard(remove)
      print("Burned a card: {}".format(remove))
      card = self.deck.draw()
      self.table_cards.append(card)
      print("New card on the table: {}".format(card) 
#close the game and bring all cards back 
    def close(self):
        for player in self.players:
          for card in player.hand:
            self.deck.discard(card)
        for card in self.table_cards:
          self.deck.discard(card)
        self.deck.shuffle_back()
        print("Cleanup done")
table = Poker([Player("Jack"), Player("John"), Player("Peter")])
deck=Deck()
deck.deal()
deck.shuffle()
table.dealer()
table.flop()
table.call()
table.call()
table.close()
