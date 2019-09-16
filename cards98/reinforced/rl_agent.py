import tensorflow.compat.v1
from tensorflow.compat.v1 import keras
import numpy as np
import random
import math
import matplotlib.pyplot as plt

class RLAgent:
    """
    pip install -q tensorflow==2.0.0-rc0
    """
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

        self._model = None
        self._define_model()

    def _define_model(self):
        self._model = keras.Sequential()
        self._model.add(keras.layers.Dense(150, input_shape=(self._num_states,)))

    # def generator(self, input_shape):
    #     with tf.variable_scope("generator"):
    #         inputs = keras.layers.Input(input_shape)
    #         net = keras.layers.Dense(150, activation=tf.nn.relu, name="fc1")(inputs)
    #         net = keras.layers.Dense(150, activation=tf.nn.relu, name="fc2")(net)
    #         G = keras.layers.Dense(8, activation=tf.nn.relu, name="G")(net)
    #     return G


if __name__ == '__main__':
    import sys
    import os
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, path)
    from game.cards98 import GameCards98
    agent = RLAgent(num_states=98 + 4, num_actions=8+4, batch_size=100)
    app = GameCards98()
