import numpy as np
import sklearn.neural_network
# import sklearn.multioutput
import shelve
from supervised_data_grab import *

def __run_count__(readonly=False, step=1):
    num = 0
    try:
        with open('__run_count__.txt', 'r') as file:
            num = int(file.read())

    except FileNotFoundError:
        num = 0
    if not readonly:
        num += step
        with open('__run_count__.txt', 'w') as file:
            file.write(str(num))

    return str(num)

data = Grab_Teaching_Data()
samples_count = 20  # [k]
score_min = 75
nn_dimensions = (100, 64, 50, 8*4)
max_iter = 700
name = 'NN_supervised_' + __run_count__()


# input('Are you sure you want to retrain your network? ...')
print('Ok, collecting samples...')
samples = data.generate_random_states(samples_count, score_min=score_min)

print('Got {0} samples'.format(len(samples)))
print('Average good moves from 1 sample: {}%'.format(str(len(samples)/samples_count/1000*100)))

X = []
Y = []
for sample in samples:
    new_sample = np.concatenate((sample['hand'], sample['piles']))
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
# X = np.array(X)
# X.reshape(1, -1)

print('Learning {} ...'.format(name))
nn1 = sklearn.neural_network.MLPRegressor(nn_dimensions, max_iter=max_iter,)
# nn1 = sklearn.multioutput.MultiOutputClassifier()

time_before = time()  # Not decorated
nn1.fit(X, Y)
learning_time = time() - time_before # Not decorated

print('Time elapsed:', learning_time)
print('Saving to file....')



comment = 'One move per sample, begin samples, end samples'
with shelve.open('NN\\' + name, 'n') as file:
    file['supervised'] = nn1
    file['comment'] = comment

with open('learning_log.txt', 'a') as file:
    file.write('NN name:          {}\n'.format(name))
    file.write('NN comment:       {}\n'.format(comment))
    file.write('All samples:      {} 000\n'.format(samples_count))
    file.write('Samples grabbed:  {} %\n'.format(round((len(Y) / samples_count / 10), 4)))
    file.write('Learning layers:  {}\n'.format(nn_dimensions))
    file.write('Max iters:        {}\n'.format(max_iter))
    file.write('Learning Time:    {} m\n\n'.format(round(learning_time/60, 2)))

# test_X = [[78, 37, 11, 48, 32, 27, 62, 90, 1, 1, 100, 100]]
# test_X = np.array(test_X).reshape(-1,1)

# predicted = nn1.predict(test_X)
# print(predicted)
# # [[0.68037785 1.48963757]]
#
# print('Hand =', predicted[0][0] )
# print('Pile =', predicted[0][1] )
