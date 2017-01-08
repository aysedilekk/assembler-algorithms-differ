import os, sys

#copy tools to opt
runCA="/opt/wgs-8.3rc2/Linux-amd64/bin/runCA"
fastaToCA = "/opt/wgs-8.3rc2/Linux-amd64/bin/fastaToCA"

COMMAND_LIST = []
end_of_runca = 'echo "RUNCA HAS FINISHED..."'
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

r_b_output = "outputs/runCA/brucella/"
compare_with_brucella = directory_brucella + "Brucella_suis_1330.1con"

contig_directory = "9-terminator/"

ctg_file = "{}.fasta"

blast_txt_suffix  = "{}_blast.txt"

command = 'echo "doFragmentCorrection = 0" > spec'
COMMAND_LIST.append(command)
# print(command)

# cat random.seq random_nonmatching.seq > brucella_random_merge.seq
command = "cat {} {} > {}".format(directory_brucella + random_seq_file, directory_brucella + random_nonmatching_seq_file, directory_brucella + random_merge_seq_suffix.format("brucella"))
COMMAND_LIST.append(command)
# cat random.qual random_nonmatching.qual > brucella_random_merge.qual
command = "cat {} {} > {}".format(directory_brucella + random_qual_file, directory_brucella + random_nonmatching_qual_file, directory_brucella + random_merge_qual_suffix.format("brucella"))
COMMAND_LIST.append(command)

# perl fastaToCA -l brucella -s ~/Desktop/Bioinformatics/Datasets/Brucella_suis_1330/brucella_random_merge.seq -q Datasets/Brucella_suis_1330/brucella_random_merge.qual > brucella.frg
command = "perl {} -l brucella -s {} -q {} > brucella.frg".format(fastaToCA, directory_brucella + random_merge_seq_suffix.format("brucella"), directory_brucella + random_merge_qual_suffix.format("brucella"))
COMMAND_LIST.append(command)
# print(command)
# runCA -s spec -d runCAOutput -p brucella brucella.frg
command  = "{} -s spec -d {} -p brucella brucella.frg".format(runCA, r_b_output)
COMMAND_LIST.append(command)
# print(command)
COMMAND_LIST.append(end_of_runca)
COMMAND_LIST.append(start_of_blast)

merge_url = "outputs/runCA/brucella/9-terminator/"

#merge .scf .ctg .deg .utg
command  = "cat {} {} {} {} > {}".format(merge_url + "brucella.ctg.fasta", merge_url + "brucella.scf.fasta",merge_url + "brucella.deg.fasta",merge_url + "brucella.utg.fasta",merge_url+"brucella.fasta")
COMMAND_LIST.append(command)

# blast2 -p blastn -i ~/Desktop/Bioinformatics/BrucellaVelvetOutput/contigs.fa -j ~/Desktop/Bioinformatics/Datasets/Brucella_suis_1330/Brucella_suis_1330.1con -m9 -o ~/Desktop/Bioinformatics/BlastResults/BrucellaBlast.txt -P 95
command = "blast2 -p blastn -i {} -j {} -m9 -o {} -P 95".format(r_b_output + contig_directory + ctg_file.format("brucella"), compare_with_brucella, r_b_output + blast_txt_suffix.format("brucella"))
COMMAND_LIST.append(command)
COMMAND_LIST.append(end_of_blast)
COMMAND_LIST.append(start_of_compare)
command = "./regex_runca.py {}".format(r_b_output + blast_txt_suffix.format("brucella"))
COMMAND_LIST.append(command)

for COMMAND in COMMAND_LIST:
    #print(COMMAND)
    os.system(COMMAND)
