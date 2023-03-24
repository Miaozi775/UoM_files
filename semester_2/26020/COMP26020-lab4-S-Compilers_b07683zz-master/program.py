import sys

if __name__ == '__main__':
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    
    # record the graph
    map = {} # dict: node -> node
    vt = [] # element: (node, number of neighbour)
    # read the input file
    for line in open(inputfile).readlines():
        line = line.strip().split(' ')
        u = int(line[0])
        map[u] = {}
        vt.append( [u,len(line)] )
        for i in range(1,len(line)):
            v = int(line[i])
            map[u][v] = True
            
    # rank the nodes according to the number of neighbours in descending order,
    # than with the lowest id
    vt = sorted(vt, key=lambda x:(-x[1],x[0]))
    
    # record the final result
    color = {} # node -> color
    # go through each node
    for (u,_) in vt:
        # record the colors used by its neighbours
        neighbour_color = {}
        for v in map[u]:
            if v in color:
                neighbour_color[color[v]] = True
        # go through all the colors
        for c in [chr(ord('A')+i) for i in range(26)]:
            if c not in neighbour_color:
                color[u] = c
                break
    
    # write the result
    f = open(outputfile,"w")
    vt = sorted(vt, key=lambda x:x[0])
    for (u,_) in vt:
        f.write(str(u)+color[u]+"\n")
    f.close()
