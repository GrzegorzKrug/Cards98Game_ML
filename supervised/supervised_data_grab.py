import os, sys
mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append( mypackage_path )
from GameCards98 import GameCards98

class Grab_Teaching_Data(GameCards98):
    def __init__(self):
        self.samples = 10000
        self.states = []
        pass

    def get_game_states(self):
        pass

    def assisng_values_to_states(self):
        pass




app = Grab_Teaching_Data()

# app.start_game()