import os, sys
import  numpy as np
import shelve
from time import  time

mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append( mypackage_path )
from GameCards98 import GameCards98

class Grab_Teaching_Data():
    def __init__(self):
        self.N = 100000
        self.states = []
        pass

    def generate_random_states(self, N=None):
        # Generates random states of the game by randmizing cards in deck, hand and piles
        # returns list of dicts
        # [{deck, hand, piles, move, score},
        # list size = N

        if N is None:
            print("changed to, N = ",self.N)
            N = self.N

        self.states = []
        for _ in range(N):
            print("N[k]:", _/1000)  # boring waiting :D

            deck = np.arange(2, 100)
            np.random.shuffle(deck)

            piles = deck[0:4]  # placing 4 random cards on stacks
            deck = deck[4:]

            hand = deck[0:8]  # taking 8 random cards to hand
            deck = deck[8:]

            random_remove = round(np.random.rand() * 85)  # 2:99 -> 98 cards, 98-8-4=86 -> index from 0=85
            deck = deck[0:random_remove]

            result_sample = self.choose_card(deck, hand, piles)

            if type(result_sample) is list:
                for element in result_sample:
                    self.states.append(element)
            else:
                self.states.append(result_sample)

        return  self.states

    def choose_card(self, deck, hand, piles):
        this_dict = {'deck':deck, 'hand': hand, 'piles':piles, 'score':1, 'move':(0,0)}
        multi_dict = [this_dict, this_dict]
        return  multi_dict




app = Grab_Teaching_Data()

N = 1000 * 1000
states = app.generate_random_states(N)
# for sample in states:
#     print(sample)

os.makedirs(os.path.abspath(os.path.join('data')), exist_ok=True)
time0 = time()
with shelve.open('data\learning', 'n') as file:
    # file.clear()
    file['learning'] = states
    # file['decks'] = file['decks'] + decks  # appending Data

print(time() - time0)
# file = shelve.open('data', 'r')
# file.close()
