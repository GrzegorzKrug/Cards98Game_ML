import os, sys
import  numpy as np
import shelve

mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append( mypackage_path )
from GameCards98 import GameCards98

class Grab_Teaching_Data():
    def __init__(self):
        self.N = 100000
        self.states = []
        pass

    def get_game_states(self, N=None):
        if N is None:
            print("changed to, N = ",self.N)
            N = self.N

        self.states = []
        for _ in range(N):
            print("N:", _)  # boring waiting :D

            cards = np.arange(2, 100)
            np.random.shuffle(cards)

            stacks = cards[0:4]  # placing 4 random cards on stacks
            cards = cards[4:]

            hand = cards[0:8]  # taking 8 random cards to hand
            cards = cards[8:]

            random_remove = round(np.random.rand() * 85)  # 2:99 -> 98 cards, 98-8-4=86 -> index from 0=85
            cards = cards[0:random_remove]

            points = self.choose_card(cards, hand, stacks)

            self.states.append((cards, hand, stacks, points))
        return  self.states

    def choose_card(self, cards, hand, stacks):
        return 0




app = Grab_Teaching_Data()

N = 1000 * 1
states = app.get_game_states(N)
for sample in states:
    print(sample)
with shelve.open('data', 'n') as file:
    file['decks'] = decks
    # file['decks'] = file['decks'] + decks  # appending Data





# file = shelve.open('data', 'r')
# file = shelve.open('data', 'r')
# file.close()
