from game.cards98 import GameCards98
from reinforced.rl_agent import RLAgent


class Game(GameCards98):
    def main_loop(self):  # override
        ''' Main loop with game logic'''
        while True:
            self.hand_fill()
            status, comment = self.end_condition()

            if status is not None:
                print('\n')
                return status, comment

            self.display_table()
            self.agent_input()
            self.play_card(self.hand_ind, self.pile_ind)
            self.print_move_reward()

    def agent_input(self):
        self.hand_ind = 0
        self.pile_ind = 0

    def print_move_reward(self):
        print("Card played {card} -> Pile {pile}".format(card=self.last_card_played,
                                                         pile=self.pile_ind + 1))
        print("Reward: {reward}".format(reward=self.score_gained))
        print(' _' * 80)


app = Game()
app.start_game()
