import shelve
import numpy as np
import os, sys
from supervised_data_grab import Grab_Teaching_Data

mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append(mypackage_path)
from GameCards98 import GameCards98  # importing from diffrent directory


my_predict = Grab_Teaching_Data.attach_score_to_state

game = GameCards98()
game.reset()
game.hand_fill()
score = 0
app1 = Grab_Teaching_Data()
while True:
    game.hand_fill()
    # game.display_table()

    # hand = game.hand
    # piles = game.piles
    # turn = game.turn


    # def attach_score_to_state(self, deck, hand, piles, score_min=1, best_move_only=True):
    best_move = app1.attach_score_to_state(None, game.hand, game.piles)[0]
    if best_move is None:
        pass
    else:

        hand, pile = best_move['move']
        score_pre = game.score  # capturing score for comparison
        game.play_card(hand, pile)
        print('My move', hand + 1, pile + 1, '\t', 'Score gained=', game.score - score_pre)

    # input('next...')
    status, comment = game.end_condition()
    if status:
        input(comment)
    if status is not None or game.score < - 10:

        print(comment)
        break

game.display_table(show_chances=False)

