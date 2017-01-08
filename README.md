## HOW DO ASSEMBLER ALGORITHMS DIFFER?

![gif](https://media.giphy.com/media/3o7TKuNppMPOUQwEJW/source.gif)

## Description
   Identifying the best assembler algorithm with using different assembler algorithms
  ([Velvet](https://www.ebi.ac.uk/~zerbino/velvet/) & [Celera Assembler](http://wgs-assembler.sourceforge.net/wiki/index.php/RunCA)) and comparing their results.

## Requirements
* [Python 3.0](https://www.python.org/download/releases/3.0/)
* [RunCA 8.3](http://wgs-assembler.sourceforge.net/wiki/index.php/RunCA)
* [Velvet](https://www.ebi.ac.uk/~zerbino/velvet/)
* Linux Distribution
* Blast2

  ```
  sudo apt-get install blast2
  ```

## Datasets
* [Brucella suis](ftp://ftp.cbcb.umd.edu/pub/data/asmg_benchmark/Brucella_suis_1330.tar.gz)
* [Staphylococcus epidermidis RP62A](ftp://ftp.cbcb.umd.edu/pub/data/asmg_benchmark/Staphylococcus_epidermidis_RP62A.tar.gz)

## Steps
* Download the datasets and copy the files to "datasets/brucella" and "datasets/s_epidermis"
* Run script as
```
./script.py --tool TOOL_NAME --dataset DATASET_NAME
```
e.g:
```
./scr.py --tool velvet --dataset brucella
./scr.py --tool runca --dataset s_epidermis
```

## What Does Script Do
* For Velvet Tool:
  - Script merges the random.seq and random_nonmatching.seq in the datasets
  - Velvet works and the 'contigs.fa' file occurs
  - Blast works with the 'contigs.fa' and the full genome in the datasets
  - Another script pruns the blast result and calculate the rate of percentages (min. 95%)
* For RunCA Tool:
  - RunCA works with .FRG files so;
  - Script merges the random.seq and random_nonmatching.seq and merges the random.qual and random_nonmatching.qual
  - with using fastaToCA script these merges are converted to .FRG files
  - RunCA works and results occurs in 4 different files
  - Script merges these files and blast works
  - As Velvet Tool step, another script pruns the blast result and calculate the rate of percentages (min. 95%)
