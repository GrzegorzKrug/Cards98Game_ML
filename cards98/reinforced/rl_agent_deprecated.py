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

        self._define_model()

    def _define_model(self):
        self._states = tf.compat.v1.placeholder(tf.float32, shape=[None, self._num_states])

        fc1 = tf.layers.dense(self._states, 150, activation=tf.nn.relu)

        # model = Sequential()
        # fc2 = tf.layers.dense(fc1, 50, activation=tf.nn.relu)
        # self._logits = tf.layers.dense(fc2, self._num_actions)
        #
        # self._qsa = tf.compat.v1.placeholder(tf.float32, shape=[None, self._num_actions])


if __name__ == '__main__':
    import sys
    import os
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, path)
    from game.cards98 import GameCards98
    agent = RLAgent(num_states=98+4, num_actions=8+4, batch_size=100)
    app = GameCards98()
