import os, sys
velveth="/opt/velvet_1.2.10/velveth"
velvetg="/opt/velvet_1.2.10/velvetg"

COMMAND_LIST = []
end_of_velvet = 'echo "VELVET HAS FINISHED..."'
start_of_blast = 'echo "BLAST HAS STARTED..."'
end_of_blast = 'echo "BLAST HAS FINISHED..."'
start_of_compare = 'echo "Blast result is pruned and compared...It may take a little time."'

directory_s_epidermis = "datasets/s_epidermis/"
random_seq_file = "random.seq"
random_nonmatching_seq_file = "random_nonmatching.seq"
random_qual_file = "random.qual"
random_nonmatching_qual_file = "random_nonmatching.qual"

random_merge_seq_suffix = "{}_random_merge.seq"
random_merge_qual_suffix = "{}_random_merge.qual"

v_s_output = "outputs/velvet/s_epidermis/"

compare_with_s_epidermis = directory_s_epidermis + "Staphylococcus_epidermidis_RP62A.1con"

contigs_fa = "contigs.fa"
blast_txt_suffix  = "{}_blast.txt"

# cat random.seq random_nonmatching.seq > ste_random_merge.seq
command = "cat {} {} > {}".format(directory_s_epidermis + random_seq_file, directory_s_epidermis + random_nonmatching_seq_file, directory_s_epidermis + random_merge_seq_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)

# velveth ~/Desktop/Bioinformatics/VelvetOutput 21 -shortPaired ~/Desktop/Bioinformatics/Datasets/Brucella_suis_1330/s_epidermis_random_merge.seq
command = "{} {} 21 -shortPaired {}".format(velveth, v_s_output, directory_s_epidermis + random_merge_seq_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)
# velvetg ~/Desktop/Bioinformatics/VelvetOutput -exp_cov auto
command = "{} {} -exp_cov auto".format(velvetg, v_s_output)
COMMAND_LIST.append(command)
COMMAND_LIST.append(end_of_velvet)
COMMAND_LIST.append(start_of_blast)

command = "blast2 -p blastn -i {} -j {} -m9 -o {} -P 95".format(v_s_output + contigs_fa, compare_with_s_epidermis, v_s_output + blast_txt_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)

COMMAND_LIST.append(end_of_blast)
COMMAND_LIST.append(start_of_compare)

command = "./regex_velvet.py {}".format(v_s_output + blast_txt_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)
# print(command)

for COMMAND in COMMAND_LIST:
    #print(COMMAND)
    os.system(COMMAND)
