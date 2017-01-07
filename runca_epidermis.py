import os, sys

runCA="/opt/wgs-8.3rc2/Linux-amd64/bin/runCA"
fastaToCA = "/opt/wgs-8.3rc2/Linux-amd64/bin/fastaToCA"

COMMAND_LIST = []
end_of_runca = 'echo "RUNCA HAS FINISHED..."'
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

r_s_output = "outputs/runCA/s_epidermis/"
compare_with_s_epidermis = directory_s_epidermis + "Staphylococcus_epidermidis_RP62A.1con"

contig_directory = "9-terminator/ctg/"

ctg_file = "{}.ctg.fasta"

blast_txt_suffix  = "{}_blast.txt"

command = 'echo "doFragmentCorrection = 0" > spec'
COMMAND_LIST.append(command)
# print(command)

# cat random.seq random_nonmatching.seq > ste_random_merge.seq
command = "cat {} {} > {}".format(directory_s_epidermis + random_seq_file, directory_s_epidermis + random_nonmatching_seq_file, directory_s_epidermis + random_merge_seq_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)
# print(command)

# cat random.qual random_nonmatching.qual > ste_random_merge.qual
command = "cat {} {} > {}".format(directory_s_epidermis + random_qual_file, directory_s_epidermis + random_nonmatching_qual_file, directory_s_epidermis + random_merge_qual_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)

command = "perl {} -l s_epidermis -s {} -q {} > s_epidermis.frg".format(fastaToCA, directory_brucella + random_merge_seq_suffix.format("s_epidermis"), directory_brucella + random_merge_qual_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)
# print(command)
command  = "{} -s spec -d {} -p s_epidermis s_epidermis.frg".format(runCA, r_s_output)
COMMAND_LIST.append(command)
COMMAND_LIST.append(end_of_runca)
COMMAND_LIST.append(start_of_blast)

command = "blast2 -p blastn -i {} -j {} -m9 -o {} -P 95".format(r_s_output + contig_directory + ctg_file.format("s_epidermis"), compare_with_s_epidermis, r_s_output + blast_txt_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)
# print(command)
COMMAND_LIST.append(end_of_blast)
COMMAND_LIST.append(start_of_compare)
command = "./regex_runca.py {}".format(r_s_output + blast_txt_suffix.format("s_epidermis"))
COMMAND_LIST.append(command)
# print(command)

for COMMAND in COMMAND_LIST:
    #print(COMMAND)
    os.system(COMMAND)
