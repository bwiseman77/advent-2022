#! /usr/bin/env python3
import sys
import heapq

ADJ = (-1, 0, 1)

def adj_cells(Map, i, j, n):
    ''' Get adj cells that are valid '''
    cells = []
    for x in ADJ:
        for y in ADJ:

            # dont add padding or diags
            if abs(x) != abs(y) and Map[i+x][j+y] != 0:  
                # if start, add all 
                if Map[i][j] == "S":
                    cells.append(((i+x)-1)*n + ((j+y)-1))
                # if in z, u can add E
                elif Map[i][j] == "z" and Map[i+x][j+y] == "E":
                    cells.append(((i+x)-1)*n + ((j+y)-1))
                # add if 1 up or any below (make sure we are lowercase so math is happy)
                elif Map[i+x][j+y].islower() and ord(Map[i][j])+1 >= ord(Map[i+x][j+y]):
                    cells.append(((i+x)-1)*n + ((j+y)-1))
            
    return cells

def build_graph(Map, m, n):
    '''Build the graph {source : [list of neighbors]}
        also keep track of index of starting point and end point'''
    g = {}
    start = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            index = ((i-1)*n) + (j-1)
            if Map[i][j] == "S":
                start = index
            elif Map[i][j] == "E":
                end = index

            g[index] = adj_cells(Map, i, j, n)

    return start, end, g

def short_path(g, start):
	''' Finds shortest path to every node from a given node'''

	frontier = []
	visited = {}

	heapq.heappush(frontier, (0, start, start))

	while frontier:
		weight, source, target = heapq.heappop(frontier)

		if target in visited:
			continue

		visited[target] = (source, weight)

		for neighbor in g[target]:
			heapq.heappush(frontier, (weight + 1, target, neighbor))

	return visited

def main():
    
    # read in
    Map = []
    while (line:=sys.stdin.readline().strip()):
        Map.append(list(line))

    # pad with zeros, m=rows, n=cols
    m, n = len(Map), len(Map[0])

    for i in range(m):
        Map[i].insert(0, 0)
        Map[i].append(0)
    
    Map.insert(0, [0 for _ in range(n+2)])
    Map.append([0 for _ in range(n+2)])

    # build the graph
    start, end, graph = build_graph(Map, m, n)

    # answer
    visited = short_path(graph, start)
    print(visited[end][1])

        

if __name__ == "__main__":
    main()
