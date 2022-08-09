#Naive version of the partition class. Does not implement the rank heuristic or path compression

class Partition():              
                                
    def __init__(self,V):
        self._position = {}                   #data structure is still a map, but key value is only parent node
        for v in V:                           #instead of parent, rank
            self._position[v] = v
        
    def find(self,v):
        if self._position[v] == v:                #this function does not update the parent nodes along the parent
            return(v)                             #node path to be the representative element, it only follows  
        else:                                     #the parent node path and returns the representative of the  
            return(self.find(self._position[v]))  #part which contatins v.
    
    def link(self,u,v):                        #just changes representative u's parent node from u 
        self._position[u] = v                  #to the representative v