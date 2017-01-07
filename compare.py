#!/usr/bin/python3
velvet_percentage = "outputs/percentage/velvet_percentage.txt"
runca_percentage = "outputs/percentage/runca_percentage.txt"

data = open(velvet_percentage, 'r').read()

a = data.split(" ")

velvet_output_list = []
for i in a:
    velvet_output_list.append(i.split(","))

print(velvet_output_list)

data_2 = open(runca_percentage, 'r').read()

a_2 = data_2.split(" ")

runca_output_list = []
for i in a_2:
    runca_output_list.append(i.split(","))

print(runca_output_list)

for i,j in velvet_output_list:
    for k,l in runca_output_list:
        if (i == k):
            print(i + "%" + " >> " + j +  " velvet" + " - " + l +  " runca")
            break
