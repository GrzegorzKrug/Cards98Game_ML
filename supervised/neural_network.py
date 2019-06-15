import sklearn
from supervised_data_grab import *

data = Grab_Teaching_Data()
k = 0.1
samples = data.generate_random_states(k)
print('Got {0} samples'.format(len(samples)))
print('Average good moves from 1 sample: {}'.format(str(len(samples)/k/1000)))



X = []
Y = []

for sample in samples:
    new_sample = []
    new_score = []
    for key, value in sample.items():
        if key == 'deck':
            continue
        elif key == 'score':
            new_score.append(value)
        else:
            new_sample = new_sample + (list(value))

    X.append(new_sample)
    Y = Y + new_score


nn1 = sklearn.neural_network.MLPRegressor(max_iter=1000)
nn1.fit(X, Y)