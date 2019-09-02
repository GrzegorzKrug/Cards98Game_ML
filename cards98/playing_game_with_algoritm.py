import shelve
import numpy as np
import os, sys
from supervised.supervised_data_grab import Grab_Teaching_Data
##from GameCards98 import GameCards98  # importing from diffrent directory

from game.cards98 import GameCards98

win_count = 0
my_predict = Grab_Teaching_Data.attach_score_to_state



X = 10000
for x in range(X):
    game = GameCards98()
    game.reset()
    game.hand_fill()
    score = 0
    app1 = Grab_Teaching_Data()
    
    while True:
        game.hand_fill()
        # game.display_table()
        best_move = app1.attach_score_to_state(None, game.hand, game.piles)[0]
        if best_move is None:
            pass
        else:

            hand, pile = best_move['move']
            score_pre = game.score  # capturing score for comparison
            game.play_card(hand, pile)
            score_gained = game.score - score_pre  # compare score after playing card
            # print('My move', hand + 1, pile + 1, '\t', 'Score gained=', game.score - score_pre)

        status, comment = game.end_condition()
        if status:
            # print('First win, x=', x)
            # input(comment)
            win_count += 1

        if status is not None or game.score < -10 or score_gained < 0:
            # print(comment)
            break
print('Win count =',win_count)
print('Win ratio =',win_count/X*100, '%')

# Easy Version
# Win ratio = 3.5 ~ 4.12 %

# Harder Version
# Win ratio = 0.63 %
