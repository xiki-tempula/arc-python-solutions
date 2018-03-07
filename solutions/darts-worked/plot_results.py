#
#
# Takes a set of files containing value data pairs and plot on a single graph
#
# Requires: matplotlib
#

import pylab

#
# File list contains a list of labels and results filenames.
# 
fileList = [ 	
# 	("Python", "results_python.txt"),
		("Numpy", "results_numpy.txt"),	
		("Numba", "results_numba.txt"),	
		("Multiprocessing", "results_MP.txt"),	
#		("MPI4py_4", "results_mpi_4.txt")	
	   ]
	     
#
# for each file read pairs and plot with appropriate label
#
for label, file in fileList:
    data = pylab.loadtxt(file)
    pylab.plot( data[:,0], data[:,1], label=label )

pylab.legend()

#
# Label graph...
#

pylab.title("Results")
pylab.xlabel("No. of darts")
pylab.ylabel("Time (s)")

pylab.show()
