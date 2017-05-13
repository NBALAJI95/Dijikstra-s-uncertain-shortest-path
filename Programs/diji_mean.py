import math
import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def calculate(inpt):
	mean = None
	variance = None
	c_square = None
	inp = list()
	for i in inpt:
		inp.append(float(i))	

	if int(inp[2]) == 1:
		mean = inp[3]		
		variance = 0
		c_square = 0
	elif int(inp[2]) == 2:
		mean = (inp[3] + inp[4]) / 2.0
		variance = ((inp[4] - inp[3]) * (inp[4] - inp[3])) / 12.0
		c_square = (1/3.0) *  ((float(inp[4] - inp[3]) / float(inp[4] + inp[3])) * (float(inp[4] - inp[3]) / float(inp[4] + inp[3])))
	elif int(inp[2]) == 3:
		mean = 1.0 / inp[3]		
		variance = 1.0 / (inp[3] * inp[3])
		c_square = 1
	elif int(inp[2]) == 4:
		mean = inp[4] + (1.0 / inp[3])
		variance = 1.0 / (inp[3] * inp[3])
		c_square = (1.0 / (1 + inp[4] * inp[3])) * (1.0 / (1 + inp[4] * inp[3]))
	elif int(inp[2]) == 5:
		mean = inp[3]		
		variance = inp[4]
		c_square = inp[4] / float(inp[3]*inp[3])
	elif int(inp[2]) == 6:
		mean = inp[3]		
		variance = (inp[3] * inp[3] * inp[4])
		c_square = inp[4]

	return [(inpt[0]), (inpt[1]), mean, variance, c_square]

if __name__ == '__main__':
	fin_table = dict()#
	e_dic = dict()#
	f = open('input_daa.txt')
	f_line = f.readline()
	vertices = f_line.split(',')[0]
	v = list()
	edge_wt = list()
	for i in range(1, int(vertices)+1):
		v.append(str(i))
	
	while True:
		readl = f.readline()
		if len(readl) == 0:
			break
		readl = readl.split(',')
		readl = readl[1:]
		tmp = calculate(readl)
		e_dic[str(readl[0])+','+str(readl[1])] = tmp#
		edge_wt.append(tmp[0:3])

	g = Graph()

	for i in v:
		g.add_vertex(i)
	
	for i in edge_wt:
		g.add_edge(str(i[0]), str(i[1]), i[2])

	print 'Graph data:'

	for v in g:
		for w in v.get_connections():
			vid = v.get_id()
			wid = w.get_id()
			fin_table[(str(vid), str(wid))] = False#
			print vid, wid, v.get_weight(w)

	dijkstra(g, g.get_vertex('1'), g.get_vertex('12')) 

	target = g.get_vertex('12')
	path = [target.get_id()]
	shortest(target, path)
	print 'The shortest path : %s' %(path[::-1])
	#
	path_res = path[::-1]
	print '*' * 45
	i = 0 
	j = 1
	n = len(path_res)
	mean = 0
	mean_minus_sd = 0
	mean_plus_sd = 0
	mean_plus_twice_sd = 0
	c_squared = 0
	hops = 0
	dispersion_index = 0 # var/mean
	while j < n and i < n - 1:
		rr = (path_res[i], path_res[j])
		fin_table[rr] = True #
		fin_table[(str(path_res[j]), str(path_res[i]))]  = True#
		mean += e_dic[str(path_res[i])+','+str(path_res[j])][2] 
		mean_minus_sd += e_dic[str(path_res[i])+','+str(path_res[j])][2] - math.sqrt(e_dic[str(path_res[i])+','+str(path_res[j])][3])
		mean_plus_sd += e_dic[str(path_res[i])+','+str(path_res[j])][2] + math.sqrt(e_dic[str(path_res[i])+','+str(path_res[j])][3])
		mean_plus_twice_sd += e_dic[str(path_res[i])+','+str(path_res[j])][2] + 2 * math.sqrt(e_dic[str(path_res[i])+','+str(path_res[j])][3])
		c_squared += e_dic[str(path_res[i])+','+str(path_res[j])][4]
		dispersion_index += e_dic[str(path_res[i])+','+str(path_res[j])][3] / e_dic[str(path_res[i])+','+str(path_res[j])][2]
		i += 1
		j += 1
	hops = n - 1
	print 'Mean:', mean
	print 'Mean - SD:', mean_minus_sd
	print 'Mean + SD:', mean_plus_sd
	print 'Mean + 2 * SD:', mean_plus_twice_sd
	print 'C Squared:', c_squared
	print 'Dispersion Index:', dispersion_index
	print 'Hop count:', hops

	fh = open('RESULTS.csv','a')
	fh.write('CRITERIA, PATH, MEAN, MEAN - SD, MEAN + SD, MEAN + 2 * SD, C SQUARED, DISPERSION INDEX, HOP')
	output = str('\n') + str('MEAN VALUE') + str(',') + str('-'.join(path_res)) + str(',') + str(mean) + str(',')  + str(mean_minus_sd) + str(',')  + str(mean_plus_sd) + str(',')  + str(mean_plus_twice_sd) + str(',')  + str(c_squared) + str(',')  + str(dispersion_index) + str(',')  + str(hops)
	fh.write(output)

	print 'Final Table'
	for i in fin_table.keys():
		print i,
		print '\t',
		print fin_table[i]
