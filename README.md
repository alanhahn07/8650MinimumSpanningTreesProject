## Minimum Spanning Trees using Kruskal’s Algorithm, with added heuristics Path Compression and Union by Rank

This is a repository for my graduate 8650 Data Structures class project. Note that the Python code is written in a version of Python 2.

The full write-up may be found by clicking 8650ProjectWriteUp.pdf above, or by clicking [here](https://github.com/alanhahn07/8650minimumspanningtree/blob/main/8650ProjectWriteUp.pdf). The slide presentation given at the end of the course may be found by clicking 8650ProjectPresentationPrintable.pdf above, or by clicking [here](https://github.com/alanhahn07/8650minimumspanningtree/blob/main/8650ProjectPresentationPrintable.pdf).


## Running the Code

The Python code may be found in the folder "Python and CSV Files" above, or by clickin [here](https://github.com/alanhahn07/8650minimumspanningtree/tree/main/Python%20and%20CSV%20Files). I recommend downloading the entire folder. The files UpdatedImplementation.py and NaiveImplementation.py are the two files that show the results of the two implementations; to run either in the command line, cd into the "Python and CSV Files" folder downloaded to your computer, then evaluate e.g. `python2 UpdatedImplementation.py` or `python2 NaiveImplementation.py` and view the output. 

The output for `python2 UpdatedImplementation.py` should look similar to the fowllowing: 

`Number of edges in graph from csv file is 35592`

`Number of edges in MST is 5877`

`Time to find MST for implementation with path compression and union by rank is 0.624685049057`

The output for the naive implementation is a bit longer, by design, and should throw an error about maximum recursion depth being exceeded.  

## About the Files in the "Python and CSV Files" Folder

KruskalImplementation.py contains the code to build the minimum spanning tree.

PriorityQueue.py contains the code to sort the edges in the weighted graph. 

NaivePartitionClass.py and UpdatedPartitionClass.py contain the code for the naive partition class and the updated partition class, respectively. 

csvinitialize.py is the code to read-in the CSV file, and soc-sign-bitcoinotc.csv is the CSV file that contains the data used to build the graph that is used for the demonstration. 

More detailed information may be found in the 8650ProjectWriteUp.pdf.
