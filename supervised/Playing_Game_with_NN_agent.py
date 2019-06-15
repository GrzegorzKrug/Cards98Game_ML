import shelve
import numpy as np
import os, sys

# LAST TRAIN
# Time elapsed: 21.650238513946533
# Got 1071477 samples
# Average good moves from 1 sample: 10.71477

mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append(mypackage_path)

from GameCards98 import GameCards98

with shelve.open('MyNN2') as file:
    nn1 = file['supervised']
    file['comment'] = 'Functions is bad, multiple moves from same samles'

# test_X = [[39, 53, 96, 13, 4, 90, 58, 72, 1, 4, 99, 100]]
# print(nn1.predict(test_X))


game = GameCards98()
game.reset()
game.hand_fill()
game.display_table()
score = 0
while True:
    game.hand_fill()
    # card_array = game.cards_left_in_array()
    game.display_table()

    hand = game.hand
    piles = game.piles

    table = [np.concatenate((hand, piles, [100]))]  # searching score 100
    move = nn1.predict(table)

    hand, pile = int(round(move[0][0])), int(round(move[0][1]))
    # print(hand)
    # print(pile)

    print('My move', hand + 1, pile + 1)
    game.play_card(hand, pile)
    print('Score =', game.score)

    # input('next...')
    status = game.end_condition()
    if status is not None or game.score < - 10:
        print('Game Over!')
        break



game.display_table()
print('End Game')
