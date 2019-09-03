import tensorflow as tf
import random
from tensorflow import keras
import numpy as np
import math
import matplotlib.pyplot as plt

class RLAgent:
    def __init__(self, num_states, num_actions, batch_size):
        self._num_states = num_states
        self._num_actions = num_actions
        self._batch_size = batch_size

        # Placeholders
        self._states = None
        self._actions = None

        #
        self._logits = None
        self._optimizer = None
        self._var_init = None


if __name__ == '__main__':
    import sys
    import os
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, path)
    from game.cards98 import GameCards98
    app = GameCards98()
    
