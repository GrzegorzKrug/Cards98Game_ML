from game.cards98 import GameCards98
from reinforced.rl_agent import RLAgent

class game(GameCards98):
    def main_loop(self):
        ''' Main loop with game logic'''
        while True:
            self.hand_fill()
            status, comment = self.end_condition()

            if status is not None:
                print('\n' * 5)
                return status

            self.display_table()
            self.agent_input()
            self.play_card(self.hand_ind, self.pile_ind)

    def agent_input(self):
        self.hand_ind = 0
        self.pile_ind = 0




app = game()
app.start_game()