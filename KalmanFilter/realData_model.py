from pykalman import KalmanFilter
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np


a = genfromtxt('file.csv')

measurements = np.asarray([(399, 293),  (403, 299)])

initial_state_mean1 = [measurements[0, 0],
                      0,
                      measurements[0, 1],
                      0]


initial_state_mean = [a[0, 0],0, a[0, 1],0]

transition_matrix = [[1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 1]]

observation_matrix = [[1, 0, 0, 0],
                      [0, 0, 1, 0]]


kf1 = KalmanFilter(transition_matrices = transition_matrix,
                  observation_matrices = observation_matrix,
                  initial_state_mean = initial_state_mean)

kf1 = kf1.em(a, n_iter=5)
(smoothed_state_means, smoothed_state_covariances) = kf1.smooth(a)


plt.figure(1)
times = range(a.shape[0])
plt.plot(#times, npdata[:, 0], 'bo',
         #times, npdata[:, 1], 'ro',
         times, a, 'bo',
         times, smoothed_state_means[:, 0], 'b--',
         times, smoothed_state_means[:, 2], 'r--',)
plt.show()
