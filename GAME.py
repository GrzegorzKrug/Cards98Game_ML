import random  # random
import re  # regex
import json
import sklearn.neural_network
import matplotlib.pyplot as plt
import numpy as np
# import pprint
# import tensorflow
# import keras_gpu
# import keras


# from tensorflow.keras import layers

import texttable as tt

# ks = tensorflow.keras
class GameCard99:
    ''' Piles    1: GoingUp 2: GoingUp
        3: GoingDown 4: GoingDown
        Input: hand_number, pile number ; Separator is not necessary'''
    def __init__(self):
        # self.pile_going_up = [1, 1]
        # self.pile_going_down = [100, 100]
        self.piles = [1, 1, 100, 100]
        self.deck = random.sample(range(2, 100), 98)  # 98)
        self.hand = []

    def calculate_chance_10(self, cards):
        lower_card_chance = []
        higher_card_chance = []
        if len(cards) != 8:
            input(len(cards))

        if len(self.deck) > 0:
            chance = round(1 / len(self.deck) * 100, 2)
            chance = str(chance) + '%'
        else:
            chance = 0

        for card in cards:

            if card - 10 in self.deck:
                lower_card_chance.append(chance)
            elif (card - 10 in self.piles[2:4]) or card - 10 in self.hand:
                lower_card_chance.append('100%')
            else:
                lower_card_chance.append('0%')

            if card+10 in self.deck:
                higher_card_chance.append(chance)
            elif card + 10 in self.piles[0:2] or card + 10 in self.hand:
                higher_card_chance.append('100%')
            else:
                higher_card_chance.append('0%')

        return[lower_card_chance, higher_card_chance]

    def check_move(self, hand_id, pile_id):
        if hand_id < 0 or hand_id > 7:
            # print('Error: Invalid hand index')
            return False

        elif pile_id < 0 or pile_id > 3:
            # print('Error: Invalid pile index')
            return False

        elif pile_id == 0 or pile_id == 1:
            try:
                if self.hand[hand_id] > self.piles[pile_id] or \
                        self.hand[hand_id] == (self.piles[pile_id] - 10):
                    return True
                else:
                    return False
            except IndexError:
                return False

        elif pile_id == 2 or pile_id == 3:
            try:
                if self.hand[hand_id] < self.piles[pile_id] or \
                        self.hand[hand_id] == (self.piles[pile_id] + 10):
                    return True
                else:
                    return False
            except IndexError:
                return False

    def display_table(self):
        print('\n' + '='*5 + ' Turn =', self.turn, '\nCards Left:', self.deck)

        piles = tt.Texttable()
        piles.header(['\\', 'A', 'B'])

        piles.add_row(['↑ Pile ↑', self.piles[0], self.piles[1]])
        piles.add_row(['↓ Pile ↓', self.piles[2], self.piles[3]])
        print(piles.draw())

        hand = tt.Texttable()
        # dupa1 = tt.Texttable()
        # dupa2 = tt.Texttable()
        [lower_chance, higher_chance] = self.calculate_chance_10(self.hand)

        # print(['Lower Chance'] + lower_chance)
        hand.add_row(['Lower Chance'] + lower_chance)
        hand.add_row(['Hand'] + self.hand)
        hand.add_row(['Higher Chance'] + higher_chance)

        print(hand.draw())
        # print(hand.draw())
        # print(hand.draw())

    def end_condition(self):
        end_game = None
        next_move = None
        for hand_id in range(8):
            if next_move:
                break

            for pile_id in range(4):
                next_move = self.check_move(hand_id, pile_id)
                if next_move:
                    break

        if next_move:
            end_game = None
        elif len(self.hand) == 0 and len(self.deck) == 0:
            end_game = True
        else:
            end_game = False

        return end_game

    def get_play_input(self):
        # Returns index based on input
        print('Select Card and pile:')
        game_input = input()
        res = re.findall(r'\d', game_input)

        if len(res) == 2:
            return int(res[0]), int(res[1])
        else:
            return[0, 0]

    def input_random(self):
        a = round(random.random()*7)+1
        b = round(random.random()*3)+1
        # print(a, b)
        return a, b

    def hand_fill(self):
        while len(self.hand) < 8 and len(self.deck) > 0:
            self.hand.append(self.deck[0])
            self.deck.pop(0)
        self.hand.sort()

    def play_card(self, hand_id, pile_id):
        if hand_id < 0 or hand_id > 7:
            print('Error: Invalid hand index')
            return None

        elif pile_id < 0 or pile_id > 3:
            print('Error: Invalid pile index')
            return None

        elif pile_id == 0 or pile_id == 1:
            if self.hand[hand_id] > self.piles[pile_id] or \
                    self.hand[hand_id] == (self.piles[pile_id] - 10):
                self.piles[pile_id] = self.hand[hand_id]
                self.hand.pop(hand_id)

            else:
                print('Not valid move!')
                return None

        elif pile_id == 2 or pile_id == 3:
            if self.hand[hand_id] < self.piles[pile_id] or \
                    self.hand[hand_id] == (self.piles[pile_id] + 10):
                self.piles[pile_id] = self.hand[hand_id]
                self.hand.pop(hand_id)
            else:
                print('Not valid move!')
                return None
        self.turn += 1

    def reset(self):
        self.__init__()

    def start_game(self, load_save=False):
        self.reset()

        if load_save:
            file = open('data/temp.json', 'r')
            self.deck = json.load(file)
            file.close()

        result = self.tick_game()
        if result:
            print("\nYou win")
        else:
            print("\nYou lost")

    def tick_game(self):
        self.turn = 0
        while True:

            self.hand_fill()
            # input(self.hand)
            self.display_table()
            status = self.end_condition()

            if status is not None:
                return status

            [hand_no, pile_no] = self.get_play_input()
            # [hand_no, pile_no] = self.input_random()
            self.play_card(hand_no - 1, pile_no - 1)


app = GameCard99()
app.start_game()
# app.start_game(load_save=True)

# file = open('data/temp.json', 'w')
# json.dump(app.deck, file)
# file.close()

# data = dump(app.deck, Loader=Loader)

