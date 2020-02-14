#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:28:28 2020

@author: andy

Done using tutorial at: https://www.youtube.com/watch?v=t8YkjDH86Y4

"""

import random

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
class Deck():
    def __init__(self):
        self.cards = []
        self.build()
        print("Deck has been built")
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
                #print("{} of {}".format(v, s))
                
    def show(self):
        for card in self.cards:
            card.show()
     
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()
    
class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
        
    def showHand(self):
        for card in self.hand:
            card.show()
    
    def discard(self):
        return self.hand.pop()



deck = Deck()
deck.shuffle()

#deck.show()

bob = Player("Bob")
bob.draw(deck).draw(deck)
bob.showHand()
