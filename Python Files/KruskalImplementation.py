#Kruskal MST Implementation

def MSTKruskal(E):
    
    blue = []                            #initialize
    V = set()
    for e in E:
        V.add(e[1])
        V.add(e[2])
    forest = Partition(V)


    P = PriorityQueue()                      #place the edges in a priority queue to be able to find the edge
    P.heapify(E)                             #with smallest edge weight and to not query edges which are not 
                                             #necessary (i.e. sorting first may sort edges we will never use)
    n = len(V)
    while len(blue) != n-1 and not len(P._array) == 0:  #do until blue tree has n-1 edges or until there are no 
        l = P.pop()                                     #edges left to consider
        u = forest.find(l[1])                          
        v = forest.find(l[2])                       #for each (u,v) = e in E, in order by edge weight from
        if u != v:                                  #low to high, check if u,v are  both in the  same partition;
            forest.link(u,v)                        #if not, put them in the same partition and add (u,v)
            blue.append(l)                          #to blue. If they are, skip this edge and go to the edge with  
                                                    #the next smallest edge weight by popping from P.
    return(blue)