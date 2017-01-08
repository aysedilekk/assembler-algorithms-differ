#!/usr/bin/python3

import collections
import re
import operator
import sys

filename = sys.argv[1]
data = open(filename, 'r').readlines()
#limit = int(data[-1].split(" ")[0].split("_")[1])
compare_percentage = open('outputs/percentage/runca_percentage.txt', 'w')
# print(limit)
node_x_list = []

for b in range(0,4000):
	for j in data:
		if b < 10 and b >= 0:
			matchObj3 = re.match(r'^utg718000000000{}(.*)'.format(b), j)
			if matchObj3:
				node_x_list.append(matchObj3.group())
				break
		elif b < 100 and b > 9:
			matchObj3 = re.match(r'^utg71800000000{}(.*)'.format(b), j)
			if matchObj3:
				node_x_list.append(matchObj3.group())
				break
		elif b < 1000 and b > 99:
			matchObj3 = re.match(r'^utg7180000000{}(.*)'.format(b), j)
			if matchObj3:
				node_x_list.append(matchObj3.group())
				break
		else:
			matchObj = re.match(r'^ctg718000000{}(.*)'.format(b), j)
			matchObj1 = re.match(r'^deg718000000{}(.*)'.format(b), j)
			matchObj2 = re.match(r'^scf718000000{}(.*)'.format(b), j)
			matchObj3 = re.match(r'^utg718000000{}(.*)'.format(b), j)

			if matchObj:
				node_x_list.append(matchObj.group())
				break
			elif matchObj1:
				node_x_list.append(matchObj1.group())
				break
			elif matchObj2:
				node_x_list.append(matchObj2.group())
				break
			elif matchObj3:
				node_x_list.append(matchObj3.group())
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
