import shelve
import numpy as np
import os, sys


def convert_list_to_matrix(this_list):
    if type(this_list) == int:
        this_list = [this_list]

    matrix = np.zeros(98)
    for item in this_list:
        matrix[item - 2] = 1
    return matrix


mypackage_path = os.path.abspath(os.getcwd() + '..' + 'mypackage')
sys.path.append(mypackage_path)
from GameCards98 import GameCards98 # importing from diffrent directory

with open('__run_count__.txt', 'r') as file:
    last_num = file.read()

with shelve.open('NN\\' + 'NN_supervised_' + last_num) as file:
    nn1 = file['supervised']


game = GameCards98()
game.reset()
game.hand_fill()
game.display_table()
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

    score_pre = game.score  # capture score
    game.play_card(hand, pile)  # play Card
    score_gained = game.score - score_pre  # compare score after playing card

    print('My move', hand + 1, pile + 1, '\t', 'Score gained=', score_gained)  # Show me move

    status, comment = game.end_condition()
    if status is not None or game.score < - 10 or score_gained < 0:
        print('Game Over!')
        break


game.display_table()
print('End Game')
