#!/bin/bash

#colors for output -useful-
YELLOW='\033[1;33m'

assemblerArr=(DBG CFG);
toolArr1=(Velvet Velvet2);
toolArr2=(Celera AllPath-LG);

#define filename
echo "Please enter your file name: ";
read fileName;
#define assembler type
printf "Which assembler do you want to use?\n1) ${assemblerArr[0]}\n2) ${assemblerArr[1]}\n";
read assemblerType;

#outputta assembler ismi
if [ $assemblerType == 1 ]
then
  assemblerChoice=${assemblerArr[0]};
else
  assemblerChoice=${assemblerArr[1]};
fi
###

#define assembler tool
if [ $assemblerType == 1 ]
then
  printf "Which assembler tool do you want to use?\n1) ${toolArr1[0]}\n2) ${toolArr1[1]}\n";
  read assemblerTool;

  #outputta tool ismi
  if [ $assemblerTool == 1 ]
  then
    toolChoice=${toolArr1[0]};
  elif [ $assemblerTool == 2 ]
  then
    toolChoice=${toolArr1[1]};
  else
    echo -e "${YELLOW}...wrong choice..."
    exit
  fi
  ###

elif [ $assemblerType == 2 ]
then
  printf "Which assembler tool do you want to use?\n1) ${toolArr2[0]}\n2) ${toolArr2[1]}\n";
  read assemblerTool;

  #outputta tool ismi
  if [ $assemblerTool == 1 ]
  then
    toolChoice=${toolArr2[0]};
  elif [ $assemblerTool == 2 ]
  then
    toolChoice=${toolArr1[1]};
  else
    echo -e "${YELLOW}...wrong choice..."
    exit
  fi
  ###

else
  echo -e "${YELLOW}...wrong choice..."
  exit
fi

#output for velvet
echo -e "${RED}filename ->" $fileName "\nassembler type ->" $assemblerChoice "\nassembler tool ->" $toolChoice
read -r -p "Are you sure? [y/N] " response
if [ -e ~/Desktop/Datasets/$fileName ]
then
  if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
  then
      cd ~/Desktop/Tools/velvet_1.2.10;
      echo `./velveth ~/Desktop/outputDir 21 -shortPaired ~/Desktop/Datasets/$fileName`;
      echo -e "${YELLOW}...finished..."
  else
      echo -e "${YELLOW}...stopped..."
      exit
  fi
else
  echo -e "${YELLOW}...file doesn't exist..."
fi
