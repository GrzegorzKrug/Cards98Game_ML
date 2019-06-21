import os, sys
import  numpy as np
import shelve
from time import  time

mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append( mypackage_path )
# from GameCards98 import GameCards98

def time_decorator(some_func):
    def check_time(*args, **kwargs):
        time0 = time()
        output = some_func(*args, **kwargs)
        # print('Excecuted  "{0}()"'.format(some_func.__name__))
        print('Time elapsed: {0}'.format(time() - time0))
        return output
    return  check_time

class Grab_Teaching_Data():
    def __init__(self):
        self.N = 100
        self.states = []

        # score_factor = 10
        self.WrongMove = -1
        self.SkipMove = 100

    def get_dict_score(self, this_dict):
        return this_dict['score']

    @time_decorator
    def generate_random_states(self, N=None, score_min = 1):
        # Generates random states of the game by randmizing cards in deck, hand and piles
        # returns list of dicts
        # [{deck, hand, piles, move, score},
        # list size = N

        if N is None:
            N = int(self.N)
            print("changed to, N = ", N)
        end = int(N * 1000 + 1)


        self.samples = []
        for i in range(1, end):
            # if (((i ) % 100) == 0):
            #     print("N :" + "{0}k".format( i/1000).rjust(8))  # boring waiting :D

            deck = np.arange(2, 100)
            np.random.shuffle(deck)

            piles = deck[0:4]  # placing 4 random cards on stacks
            deck = deck[4:]

            hand = deck[0:8]  # taking 8 random cards to hand
            deck = deck[8:]

            random_remove = round(np.random.rand() * 85)  # 2:99 -> 98 cards, 98-8-4=86 -> index from 0=85
            deck = deck[0:random_remove]

            result = self.attach_score_to_state(deck, hand, piles, score_min)
            if result is None:
                continue
            self.samples += result

        return  self.samples

    def attach_score_to_state(self, deck, hand, piles, score_min=1, best_move_only=True):
        possible_moves = []
        turn = 90 - len(deck)
        for h,this_hand in enumerate(hand):
            for p, this_pile in enumerate(piles):
                move = (h, p)
                score = self.check_if_move_is_valid(deck, hand, piles, move)
                score = score[1]

                if score < 0:
                    continue
                else:
                    this_dict = {'deck': deck, 'hand': hand, 'piles': piles, 'score': score,
                                 'move': (h, p), 'turn':turn}
                    possible_moves.append(this_dict)

        if best_move_only and len(possible_moves) > 0:
            best_move = max(possible_moves, key=self.get_dict_score)

            if best_move['score'] >= score_min:
                return [best_move]
            else:
                return

        elif len(possible_moves) > 0:
            good_moves = [move for move in possible_moves if move['score'] >= score_min]
            return good_moves

        # elif type(possible_moves) is dict and possible_moves['score'] >= score_min:
        #     print("it is dict")
            # return [possible_moves]

        else:
            return

    def check_if_move_is_valid(self, deck, hand, piles, move):
        #
        # Returns List [Bool, Score]
        # Plays Card from hand to pile.
        # Checks for Valid move.
        # Invalid moves return None.
        # Add Turn Counter at proper moves.
        #

        hand_id, pile_id = move
        score_factor = 100 - abs(hand[hand_id] - piles[pile_id])
        try:
            if hand_id < 0 or hand_id > 7:
                print('Error: Invalid hand index')
                return [False, self.WrongMove]

            elif pile_id < 0 or pile_id > 3:
                print('Error: Invalid pile index')
                return [False, self.WrongMove]

            elif pile_id == 0 or pile_id == 1:  # Rising Piles
                if hand[hand_id] > piles[pile_id]:
                    # piles[pile_id] = hand[hand_id]
                    # hand.pop(hand_id)
                    return [True, score_factor]

                elif hand[hand_id] == (piles[pile_id] - 10):
                    # piles[pile_id] = hand[hand_id]
                    # hand.pop(hand_id)
                    return [True, self.SkipMove]
                else:
                    # print('Not valid move!')
                    return [False, self.WrongMove]

            elif pile_id == 2 or pile_id == 3:  # Lowering Piles
                if hand[hand_id] < piles[pile_id]:
                    # piles[pile_id] = hand[hand_id]
                    # hand.pop(hand_id)
                    return [True, score_factor]

                elif hand[hand_id] == (piles[pile_id] + 10):
                    # piles[pile_id] = hand[hand_id]
                    # hand.pop(hand_id)
                    return [True, self.SkipMove]

                else:
                    # print('Not valid move!')
                    return [False, self.WrongMove]
            else:
                input('Impossible! How did u get here?!')
        except IndexError:
            print('IndexError: Why?!')
            return [False, self.WrongMove]


# app = Grab_Teaching_Data()
#
# N = 10  # N=10 Takes up to 10s, N=100 -> 18s
# samples = app.generate_random_states(N)

# for sample in samples:
#     print(sample['score'])


# os.makedirs(os.path.abspath(os.path.join('data')), exist_ok=True)
# with shelve.open('data\learning', 'n') as file:
#     file['learning'] = states
#     # file['decks'] = file['decks'] + decks  # appending Data
