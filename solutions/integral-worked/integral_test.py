#!/usr/bin/env python

import time
import math
import integral
import numpy
import cpintegral

import matplotlib.pyplot as plt


def main ():
    """Compute a definite integral using the trapezium rule"""

    # interval ends
    a,b = -1.0, +1.0

    # List for results
    r1,r2,r3,r4 = ([],[],[],[])
 
    # List of trapezium counts
    NVals = numpy.logspace (1, 8, base=10.0, num=6, dtype=numpy.int)

    # compute Pi 

    for N in NVals:
    	# pure Python
    	t1 = time.time ()
    	v1 = integral.trapintPython (a, b, N)
	e1 = math.fabs (v1 - math.pi)
    	t1 = time.time () - t1
	r1.append(t1)
#	print "Python: {:9d}\t{:6.4g}\t{:6.4g}".format(N, t1, e1)

    	# Python Numpy
    	t2 = time.time ()
    	v2 = integral.trapintNumPy (a, b, N)
	e2 = math.fabs (v2 - math.pi)
    	t2 = time.time () - t2
	r2.append(t2)
#	print "NumPy:  {:9d}\t{:6.4g}\t{:6.4g}".format(N, t2, e2)

    	# Python Numba
    	t3 = time.time ()
    	v3 = integral.trapintNumba(a, b, N)
	e3 = math.fabs (v3 - math.pi)
    	t3 = time.time () - t3
	r3.append(t3)
#	print "Numba:  {:9d}\t{:6.4g}\t{:6.4g}".format(N, t3, e3)

	# Cython
        t4 = time.time ()
        v4 = cpintegral.trapint (a, b, N, 4)
	e4= math.fabs (v4 - math.pi)
        t4 = time.time () - t4
	r4.append(t4)
#	print "Cython: {:9d}\t{:6.4g}\t{:6.4g}".format(N, t4, e4)

#   plt.plot(NVals, r1, label='Python')
    plt.plot(NVals, r2, label='NumPy')
    plt.plot(NVals, r3, label='Numba')
    plt.plot(NVals, r4, label='Cython')
    plt.xlabel('Number of trapezoids')
    plt.ylabel('Time (s)')

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main ()
