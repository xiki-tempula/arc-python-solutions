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

    # List of trapezium counts
    NVals = numpy.logspace (1, 8, base=10.0, num=6, dtype=numpy.int)

    # List of implementations
    intFuncList = [ 
                 (integral.trapintPython, "results_python.txt", "Pure Python"),
		 (integral.trapintNumPy,  "results_numpy.txt", "NumPy"),
		 (integral.trapintNumba,  "results_numba.txt", "Numba"),
		 (cpintegral.trapint,	 "results_cython.txt", "Cython")
               ]

    for intFunc, file , name in intFuncList:

	# Open results file...

	fh =  open( file, "w" ) 

    	# compute Pi 
	for N in NVals:
        	t1 = time.time ()
    	     	v1 = intFunc (a, b, N)
	     	e1 = math.fabs (v1 - math.pi)
    	     	t1 = time.time () - t1
	     	fh.write("{:d} {:6.4g}\n".format(N, t1))
		print "{}: N={:9d} Time={:6.4e} Error={:12.8e}".format( name, N, t1, e1 )
	fh.close()


if __name__ == "__main__":
    main ()
