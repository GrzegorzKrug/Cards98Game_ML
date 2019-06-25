import shelve
import numpy as np
import os, sys
from supervised_data_grab import Grab_Teaching_Data

mypackage_path = os.path.abspath(os.getcwd() + '..' + 'mypackage')
sys.path.append(mypackage_path)
from GameCards98 import GameCards98  # importing from diffrent directory

win_count = 0
my_predict = Grab_Teaching_Data.attach_score_to_state
for x in range(100):
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

# Win count = 412
# Win % = 4.12
