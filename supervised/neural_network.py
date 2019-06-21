import numpy as np
import sklearn.neural_network
import shelve
from supervised_data_grab import *

input('Are you sure you want to retrain your network? ...')
print('Ok, collecting samples...')

data = Grab_Teaching_Data()
samples_count = 100  # [k]
score_min = 75
samples = data.generate_random_states(samples_count, score_min=score_min)
print('Got {0} samples'.format(len(samples)))
print('Average good moves from 1 sample: {}%'.format(str(len(samples)/samples_count/1000*100)))

X = []
Y = []

for sample in samples:
    new_sample = np.concatenate((sample['hand'], sample['piles'], [sample['turn']]))
    # new_score = []
    # for key, value in sample.items():
    #     if key == 'deck' or key == :
    #         continue
    #     elif key == 'score':
    #         new_score.append(value)
    #     else:
    #         new_sample = new_sample + (list(value))

    X.append(new_sample)
    Y.append( sample['move'])

print('Learning....')
nn1 = sklearn.neural_network.MLPRegressor((300, 50), max_iter=500)
time_before = time()
nn1.fit(X, Y)
print('Time elapsed:', time() - time_before)

print('Saving to file....')
with shelve.open('NN\\' + 'MyNN_with_turn_indicator', 'n') as file:
    file['supervised'] = nn1
    file['comment'] = 'One_move_per_sample\n' \
                      + 'Turn indicator '

# test_X = [[78, 37, 11, 48, 32, 27, 62, 90, 1, 1, 100, 100]]
# test_X = np.array(test_X).reshape(-1,1)

# predicted = nn1.predict(test_X)
# print(predicted)
# # [[0.68037785 1.48963757]]
#
# print('Hand =', predicted[0][0] )
# print('Pile =', predicted[0][1] )
