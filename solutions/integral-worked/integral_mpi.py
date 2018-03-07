#!/usr/bin/env python

from mpi4py import MPI
import math
import numpy
import integral

def main (comm):
    """Compute a definite integral using the trapezium rule"""

    # size and rank of communicator
    size = comm.Get_size()
    rank = comm.Get_rank()

    # interval ends
    a,b = -1.0, +1.0

    # array with values for number of points
    NVals = numpy.logspace (1, 8, base=10.0, num=6, dtype=numpy.int)

    if rank == 0:
    	fh =  open( "results_mpi_{:d}.txt".format(size), "w" ) 

    # compute Pi (as a definite integral) using two methods
    for N in NVals:

        # use Wtime to time processing
        wt = MPI.Wtime()

        # calculate local integration limits

        h = (b - a) / float (N) 
        N1 = (float(N)* rank)   / size
        N2 =  float(N)*(rank+1) / size
        aProc = a + N1 * h
        bProc = a + N2 * h

        # local integral value
        valProc = integral.trapintNumPy (aProc, bProc, N2-N1)

        # reduce values
        valProcVec = numpy.array ([valProc])
        valVec     = numpy.zeros (1, dtype=float)
        comm.Reduce (valProcVec, valVec, op=MPI.SUM, root=0)

        # use Wtime to time processing
        wt = MPI.Wtime() - wt

        # root process writes result
        if rank == 0:
            fh.write("{:d} {:6.4e}\n".format(N, wt))
            e1 = math.fabs (valVec[0] - math.pi)
	    print "MPI({:d}) N={:9d} Time={:6.4e} Error={:12.8e}".format( size, N, wt, e1 )


    if rank ==0:
        fh.close()

if __name__ == "__main__":
    """Run with a large number of points"""
    main (MPI.COMM_WORLD)
