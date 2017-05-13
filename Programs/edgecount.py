import operator

op_dic = dict()
f = open('RESULTS.csv')
f.readline()
while True:
	read_str = f.readline()
	if len(read_str)<1:
		break
	read_str = read_str.split(',')
	read_str = read_str[1]
	read_str = read_str.split('-')
	i = 0
	j = 1
	n = len(read_str)
	while j < n and i < n - 1:
		if (read_str[i], read_str[j]) in op_dic.keys():
			op_dic[(read_str[i], read_str[j])] += 1
		else:
			op_dic[(read_str[i], read_str[j])] = 1
		i += 1	
		j += 1

x = op_dic
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse = True)
print '\nEdges along with their counts in all the criteria\n'
for i in sorted_x:
	print i

