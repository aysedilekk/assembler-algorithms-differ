import collections
import re
import operator

data = open('a.txt', 'r').readlines()
#print(data)
node_1_list = []
for j in data:
	#print(type(j))
	for b in range(1,4):
		matchObj = re.match(r'^NODE_{}(.*)'.format(b), j)

		if matchObj:
			node_1_list.append(matchObj.group())
		# else:
		# 	print("yok")

a = []
for k in node_1_list:
	a.append(k.split("\t"))

print(a)
#
# first = list(enumerate(a,0))
# #print(first)
#
# dictt = {}
# new = []
# for i,j in first:
# 			#print(j)
# 			for b in range(1,4):
# 				matchObj = re.match(r'^NODE_{}'.format(b), j[0])
# 				if matchObj:
# 					#node_1_list.append(matchObj.group())
# 					dictt[i] = j[3]
# 					new.append(max(dictt, key=dictt.get))
#
# # print(first[new])
#
#
# for i in range(len(new)):
# 	print(first[new[i]])
#

#print(node_1_list)
data_list = []

for i in data:
	line = i.split("\t")
	son = []
	for l in line:
		son.append(l)
	data_list.append(son)

# new_list = []
# for i in range(len(data_list)):
# 	new_list.append(data_list[i][0])
# 	new_list.append(data_list[i][3])
# print(new_list)

#
# dict = {}
#
# for node in data_list:
# 	if node[2] == "100.00":
# 		dict[node[0]] = 100
# 	elif node[2] >= "99.00" or node[2] < "100.00":
# 		dict[node[0]] = 99
# 	elif node[2] >= "98.00" or node[2] < "99.00":
# 		dict[node[0]] = 98
# 	elif node[2] >= "97.00" or node[2] < "98.00":
# 		dict[node[0]] = 97
# 	elif node[2] >= "96.00" or node[2] < "97.00":
# 		dict[node[0]] = 96
# 	elif node[2] >= "95.00" or node[2] < "96.00":
# 		dict[node[0]] = 95
#
# #print(dict)
#
#
# identity = dict.values()
# #print(identity)
# l = len(identity)
# #print(l)
#
#
# counter=collections.Counter(identity)
# #print(counter)
#
#
# count = counter.items()
#
#
# # for i,r in count:
# # 	print(str(i) + " --> " + str(r/l))
