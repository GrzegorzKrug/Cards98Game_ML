from supervised_data_grab import Grab_Teaching_Data

data = Grab_Teaching_Data()
k = 10
samples = data.generate_random_states(k)
print('Got {0} samples'.format(len(samples)))
print('Average good moves from 1 sample: {}'.format(str(len(samples)/k/1000)))