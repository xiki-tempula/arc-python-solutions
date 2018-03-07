#!/usr/bin/env python

import time
import math
import numpy
import darts

def main ():
    """Time result of Monte--Carlo calculations for a number of sample sizes (log spacing)"""

    # generate values for number of tries

    NVals = numpy.logspace (1, 8, base=10.0, num=6, dtype=numpy.int)

    # List of implementations
    intFuncList = [ 
                 (darts.numQuadrantHitsPython, "results_python.txt", "Pure Python"),
		 (darts.numQuadrantHitsNumPy,  "results_numpy.txt", "NumPy"),
		 (darts.numQuadrantHitsNumba,  "results_numba.txt", "Numba"),
	         (darts.numQuadrantHitsMP, "results_MP.txt", "Multiprocessing")
               ]

    for intFunc, file, name in intFuncList:

	# Open results file...

	fh =  open( file, "w" ) 

    	# compute Pi 
	for numPoints in NVals:
        	t1 = time.time ()
    	     	n1 = intFunc (numPoints)
	     	e1 = math.fabs (4.0 * float (n1) / float (numPoints) - math.pi)
    	     	t1 = time.time () - t1
	     	fh.write("{:d} {:6.4g}\n".format(numPoints, t1))
	        print "{}: Darts={:9d} Time={:6.4e} Error={:12.8e}".format (name,numPoints, t1, e1)

	fh.close()


if __name__ == "__main__":
    main ()
