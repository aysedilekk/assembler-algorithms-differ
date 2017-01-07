#!/usr/bin/python3
import collections
import re
import operator
import sys

filename = sys.argv[1]
data = open(filename, 'r').readlines()
#limit = int(data[-1].split(" ")[0].split("_")[1])
# print(limit)
compare_percentage = open('outputs/percentage/velvet_percentage.txt', 'w')
node_x_list = []
for b in range(1,40000):
	for j in data:
		matchObj = re.match(r'^NODE_{}(.*)'.format(b), j)
		if matchObj:
			node_x_list.append(matchObj.group())
			break

output_list = []
for k in node_x_list:
	output_list.append(k.split("\t"))

dict = {}
for node in output_list:
	if float(node[2]) == 100.00:
		dict[node[0]] = 100
	elif float(node[2]) >= 99.00 and float(node[2]) < 100.00:
		dict[node[0]] = 99
	elif float(node[2]) >= 98.00 and float(node[2]) < 99.00:
		dict[node[0]] = 98
	elif float(node[2]) >= 97.00 and float(node[2]) < 98.00:
		dict[node[0]] = 97
	elif float(node[2]) >= 96.00 and float(node[2]) < 97.00:
		dict[node[0]] = 96
	elif float(node[2]) >= 95.00 and float(node[2]) < 96.00:
		dict[node[0]] = 95

identity = dict.values()
l = len(identity)
counter=collections.Counter(identity)
#print(counter)
count = counter.items()
for i,r in count:
	#print(str(i) + "," + str(r/l))
	compare_percentage.write(str(i) + "," + str(r/l) + " ")

compare_percentage.close()
