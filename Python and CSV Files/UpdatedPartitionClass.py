#This is the Partition Class with the heuristics implemented

class Partition():
    
    def __init__(self,V):                                  #the data structure is a map, and for each node v,
        self._position = {}                                #the value of v is v's parent node and v's rank,
        for v in V:                                        #where v's parent node is initialized to v.
            self._position[v] = [v,0]  
        
    def find(self,v):                           #find finds and returns the representative of the part which
        if self._position[v][0] != v:           #contains v by following the parent node path of v to the 
            self._position[v][0] = self.find(self._position[v][0])  #representative, updating the parent 
        return(self._position[v][0])                            #of each node seen to the representative element. 
    
    def link(self,u,v):                                    #Note that link's inputs are representative elements
        if self._position[u][1] > self._position[v][1]:    #and not arbitrary elements. link takes two
            u,v = v,u                                      #representatives u,v and if rank(u) = rank(v),
        if self._position[u][1] == self._position[v][1]:   #then increase rank(v) by one and set u's parent node 
             self._position[v][1]+=1                       #v. If wlog rank(u) < rank(v), set u's parent node to  
        self._position[u][0] = v                           #v.

