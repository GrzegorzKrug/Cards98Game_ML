import tensorflow
from tensorflow import keras
from GameCards98 import GameCards98

class MyAgent(GameCards98):
    def __init__(self):
        GameCards98.__init__(self)
        self.old_get_user_input = self.get_user_input
        self.last_score = 0

    def agent_move(self):
        return 0.35, 0.7

    def denormalize_int(self, *args):
        for element in args:
            if len(element) != 2:
                raise ValueError # invalid input, must containt 2 numbers
            elif element[0] < 0 or element[0] > 1:
                raise ValueError  # invalid input, input must be in range <0, 1>

            yield int(round(element[0]  * element[1]))

    def get_last_move_score(self):
        last_score = self.score - self.last_score
        # print('Last Move Score:', last_score)
        self.last_score = self.score
        return last_score

    def get_user_input(self):
        #
        # Reading numbers from input
        # Method Return:
        #   True:   Move
        #   None:   Command
        #   False:  Stop or Interrupts
        #   Second object is score feedback
        #
        print('New agent input')
        self.hand_ind, self.pile_ind = -1, -1
        self.get_last_move_score()
        input()
        move = True

        if move:
            hand, pile = self.agent_move()
            hand, pile = self.denormalize_int((hand,3),(pile, 7))
            self.hand_ind = hand
            self.pile_ind = pile
            return True

        else:
            game_input = input('Give me command')
            for word in game_input:
                word = word.lower()

                if 'res' in word or 'new' in word:
                    self.reset()
                    return None

                elif 'end' in word or 'over' in word:
                    return False

    def main_loop(self):
        #
        # Agent Tick, to RE WRITE !!!
        #
        while True:
            self.hand_fill()
            card_array = self.cards_left()
            status = self.end_condition()
            if status is not None:
                print('\n' * 5)
                return status

            self.display_table()

            user_input = self.get_user_input()  # Replace user input with NN

            if user_input:
                _, score = self.play_card(self.hand_ind, self.pile_ind)
                self.score += score

            elif user_input is False:
                return False  # Interupted by user
            else:
                pass

# GameCards98.old_get_user_input = GameCards98.get_user_input
app1 = MyAgent()
# app1.start_game()

model = tf.keras.Model(inputs=inputs, outputs=predictions)
