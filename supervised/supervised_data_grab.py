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

    def convert_list_to_matrix(self, this_list):
        if this_list is None:
            this_list = []
        matrix = np.zeros(98)

        for item in this_list:
            matrix[item - 2] = 1
        return  matrix

    @time_decorator
    def generate_random_states(self, N=None, score_min = 1):
        # Generates random states of the game by randmizing cards in deck, hand and piles
        # returns list of dicts
        # [{deck, hand, piles, move, score},
        # list size = N

        if N is None:
            N = int(self.N)
            print("changed to, N = ", N)

        end_begin_phase = int(N * 1000 * 0.1)
        end_main_phase = int(N * 1000 * 0.8)
        end__end_phase = int(N * 1000 * 0.1)

        self.samples = []

        self.generate_random_states_method(end_begin_phase, phase='begin', score_min=score_min)
        self.generate_random_states_method(end_main_phase, phase='midgame', score_min=score_min)
        self.generate_random_states_method(end__end_phase, phase='endgame', score_min=score_min)  # Hand is changing shape

        return  self.samples

    def generate_random_states_method(self, end, phase='midgame', score_min=1):
        for i in range(end):
            deck = np.arange(2, 100)
            np.random.shuffle(deck)
            piles = [1, 1, 100, 100]

            if phase == 'begin':
                # piles = [1, 1, 100, 100]
                hand = deck[0:8]  # taking 8 random cards to hand
                deck = deck[8:]

            elif phase == 'midgame':
                piles = deck[0:4]  # placing 4 random cards on stacks
                deck = deck[4:]

                hand = deck[0:8]  # taking 8 random cards to hand
                deck = deck[8:]

                random_remove = int(np.random.rand() * 86)  # Cards 2:99 -> 98-8-4=86 -> index from -> 85, int() -> 86
                deck = deck[0:random_remove]  # Remove random cards from deck

            elif phase == 'endgame':
                piles = deck[0:4]  # placing 4 random cards on stacks
                deck = deck[4:]
                hand = deck[:int(np.random.rand() * (7) + 1)]  # taking 8 random cards to hand

                if len(hand) <= 0:
                    continue

                deck = None  # removing deck 

            result = self.attach_score_to_state(deck, hand, piles, score_min)
            if result is None:
                continue
            self.samples += result

    def attach_score_to_state(self, deck, hand, piles, score_min=1, best_move_only=True):
        possible_moves = []
        if deck is None:
            turn = 90 + 8 - len(hand)
        else:
            turn = 90 - len(deck)
        for h,this_hand in enumerate(hand):
            for p, this_pile in enumerate(piles):
                move = (h, p)
                score = self.check_if_move_is_valid(deck, hand, piles, move)
                score = score[1]

                if score < 0:
                    continue
                else:
                    # deck_matrix = self.convert_list_to_matrix(deck)
                    hand_matrix = self.convert_list_to_matrix(hand)
                    # piles_matrix = self.convert_list_to_matrix(piles)

                    this_dict = {'deck': deck, 'hand': hand_matrix, 'piles': piles, 'score': score,
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
                print('Error SDG: Invalid hand index')
                return [False, self.WrongMove]

            elif pile_id < 0 or pile_id > 3:
                print('Error SDG: Invalid pile index')
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
