__author__ = 'louciampanelli'

"""
Modern Physics - Chapter 7 - Question 37:

An electron is in an l = 3 state of the hydrogen atom.
What possible angles might the angular momentum vector make with the z-axis?

"""

from math import acos, sqrt, degrees

Lz = [3,2,1,0,-1,-2,-3]

# h = plancks constant
h = 6.626E-43

for l in Lz:
    print 'Lz: ' + str(l) + ' - ' + str(degrees(acos(h*l/(sqrt(12)*h))))
