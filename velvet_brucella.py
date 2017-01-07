import os, sys
velveth="/opt/velvet_1.2.10/velveth"
velvetg="/opt/velvet_1.2.10/velvetg"

COMMAND_LIST = []
end_of_velvet = 'echo "VELVET HAS FINISHED..."'
start_of_blast = 'echo "BLAST HAS STARTED..."'
end_of_blast = 'echo "BLAST HAS FINISHED..."'
start_of_compare = 'echo "Blast result is pruned and compared...It may take a little time."'

directory_brucella = "datasets/brucella/"
random_seq_file = "random.seq"
random_nonmatching_seq_file = "random_nonmatching.seq"
random_qual_file = "random.qual"
random_nonmatching_qual_file = "random_nonmatching.qual"
random_merge_seq_suffix = "{}_random_merge.seq"
random_merge_qual_suffix = "{}_random_merge.qual"

v_b_output = "outputs/velvet/brucella/"
compare_with_brucella = directory_brucella + "Brucella_suis_1330.1con"
contigs_fa = "contigs.fa"
blast_txt_suffix  = "{}_blast.txt"

# cat random.seq random_nonmatching.seq > brucella_random_merge.seq
command = "cat {} {} > {}".format(directory_brucella + random_seq_file, directory_brucella + random_nonmatching_seq_file, directory_brucella + random_merge_seq_suffix.format("brucella"))
COMMAND_LIST.append(command)

# velveth ~/Desktop/Bioinformatics/VelvetOutput 21 -shortPaired ~/Desktop/Bioinformatics/Datasets/Brucella_suis_1330/brucella_random_merge.seq
command = "{} {} 21 -shortPaired {}".format(velveth, v_b_output, directory_brucella + random_merge_seq_suffix.format("brucella"))
COMMAND_LIST.append(command)
# velvetg ~/Desktop/Bioinformatics/VelvetOutput -exp_cov auto
command = "{} {} -exp_cov auto".format(velvetg, v_b_output)
COMMAND_LIST.append(command)
COMMAND_LIST.append(end_of_velvet)
COMMAND_LIST.append(start_of_blast)

# blast2 -p blastn -i ~/Desktop/Bioinformatics/BrucellaVelvetOutput/contigs.fa -j ~/Desktop/Bioinformatics/Datasets/Brucella_suis_1330/Brucella_suis_1330.1con -m9 -o ~/Desktop/Bioinformatics/BlastResults/BrucellaBlast.txt -P 95
command = "blast2 -p blastn -i {} -j {} -m9 -o {} -P 95".format(v_b_output + contigs_fa, compare_with_brucella, v_b_output + blast_txt_suffix.format("brucella"))
COMMAND_LIST.append(command)

COMMAND_LIST.append(end_of_blast)
COMMAND_LIST.append(start_of_compare)

command = "./regex_velvet.py {}".format(v_b_output + blast_txt_suffix.format("brucella"))
COMMAND_LIST.append(command)


for COMMAND in COMMAND_LIST:
    #print(COMMAND)
    os.system(COMMAND)
