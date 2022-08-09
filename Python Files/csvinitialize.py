import csv
with open('soc-sign-bitcoinotc.csv', 'rb') as f:
    reader = csv.reader(f)
    l = []
    for row in reader:
        l.append((int(row[0]),row[1],row[2]))


#The above reads in the csv file, then puts
#the data into an array, formatted to work
#with the programs below. 

#print len(l), l[:5] 
#will show the length 
#as well as the first 5 elements in the array


#The PriorityQueue class is for sorting the edges
