#
# OPTIONAL
# requires installing stats
#
# select a distribution from stats
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

#Generate random samples from a probability density function using the ratio-of-uniforms method
from scipy import stats

import numpy as np

rng = np.random.default_rng()

rvs = stats.rvs_ratio_uniforms(lambda x: np.exp(-x), umax=1,
                               vmin=0, vmax=2*np.exp(-1), size=1000,
                               random_state=rng)

print(rvs)