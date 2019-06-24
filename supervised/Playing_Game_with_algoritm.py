import shelve
import numpy as np
import os, sys



mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append(mypackage_path)

from GameCards98 import GameCards98



with shelve.open('NN\\' + 'NN_supervised_' + last_num) as file:
    nn1 = file['supervised']


game = GameCards98()
game.reset()
game.hand_fill()
score = 0
while True:
    game.hand_fill()
    # card_array = game.cards_left_in_array()
    # game.display_table()

    hand = game.hand
    piles = game.piles
    turn = game.turn
    hand_matrix = convert_list_to_matrix(hand)
    # deck_matrix = convert_list_to_matrix(deck)

    table = [np.concatenate((hand_matrix, piles))]
    move = nn1.predict(table)

    hand, pile = int(round(move[0][0])), int(round(move[0][1]))
    # print(hand)
    # print(pile)


    score_pre = game.score
    game.play_card(hand, pile)
    # print('My move', hand + 1, pile + 1)
    print('My move', hand + 1, pile + 1, '\t', 'Score gained=', game.score - score_pre)

    # input('next...')
    status = game.end_condition()
    if status is not None or game.score < - 10:
        print('Game Over!')
        break



game.display_table()
print('End Game')
