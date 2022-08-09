execfile('csvinitialize.py')
execfile('PriorityQueue.py')
execfile('UpdatedPartitionClass.py')
execfile('KruskalImplementation.py')

import timeit
print "Number of edges in graph from csv file is",len(l)
start = timeit.default_timer()
t = MSTKruskal(l); 
print "Number of edges in MST is",len(t)
print "Time to find MST for implementation with path compression and union by rank is",timeit.default_timer() - start