import collections

data = open('data.txt', 'r').readlines()
#print(data)


data_list = []
for i in data:
	line = i.split("\t")
	son = []
	for l in line:
		son.append(l)
	data_list.append(son)
#print(data_list)



dict = {}

for node in data_list:
	if node[2] == "100.00":
		dict[node[0]] = 100
	elif node[2] == "99.00":
		dict[node[0]] = 99
	elif node[2] == "98.00":
		dict[node[0]] = 98
	elif node[2] == "97.00":
		dict[node[0]] = 97
	elif node[2] == "96.00":
		dict[node[0]] = 96
	elif node[2] == "95.00":
		dict[node[0]] = 95

#print(dict)


identity = dict.values()
#print(identity)
l = len(identity)
#print(l)


counter=collections.Counter(identity)
#print(counter)


count = counter.items()


for i,r in count:
	print(str(i) + " --> " + str(r/l))













	









