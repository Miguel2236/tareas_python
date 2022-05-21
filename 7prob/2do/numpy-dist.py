#
# select a distribution from numpy
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
import numpy

#binomial
s = numpy.random.binomial(9,0.2,1000)

print(s)

#gumbel
g = numpy.random.gumbel(0,0.1)

print(g)