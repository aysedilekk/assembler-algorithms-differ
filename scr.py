#!/usr/bin/python3
import os, sys
DATASETS_PATH = "datasets"
OUTPUT = "outputs"
BRUCELLA = "brucella"
S_EPIDERMIS = "s_epidermis"
RANDOM_SEQ_FILE = "random.seq"
RANDOM_NM_SEQ_FILE = "random_nonmatching.seq"
MERGE_SUFFIX = "_random_merge.seq"

if len(sys.argv) == 5:
	if sys.argv[1] == "--tool":
		TOOL = sys.argv[2]
		DATASET = sys.argv[4]
		if (sys.argv[2] == "velvet"):
			if (sys.argv[4] == "brucella"):
				os.system('python3 velvet_brucella.py')
			elif (sys.argv[4] == "s_epidermis"):
				os.system('python3 velvet_epidermis.py')
			else:
				raise Exception("The dataset is not found.")
		elif (sys.argv[2] == "runca"):
			if (sys.argv[4] == "brucella"):
				os.system('python3 runca_brucella.py')
			elif (sys.argv[4] == "s_epidermis"):
				os.system('python3 runca_epidermis.py')
			else:
				raise Exception("The dataset is not found.")
		else:
			raise Exception("The tool is not found.")
	else:
		TOOL = sys.argv[4]
		DATASET = sys.argv[2]
else:
	raise Exception("The number of parameters is not enough")
DATASET_PATH = os.path.join(DATASETS_PATH, BRUCELLA) if DATASET.lower().find("brucella") != -1 else os.path.join(DATASETS_PATH, S_EPIDERMIS)
