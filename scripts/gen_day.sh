#!/bin/bash
# set up for a new day in advent of code 

# make sure a day was supplied
if [ $# -eq 0 ] ;
then 
  echo "ERROR: You must supply a day number";
  exit 1;
fi

# variables
user=$(whoami);
project_directory="/home/$user/Documents/advent22/";
day=$1;

# create the directory structure
cd $project_directory;
mkdir "day$day";
cd day$day;
for part in 1 2
do
  mkdir $part;
  cd $part;
  mkdir python;
  cd python;
  touch solution.py;
  cd ..;
  mkdir rust;
  cd rust;
  cargo new advent22day${day}part${part};
  cd $project_directory/day$day/;
done

# place the user at the new python file and open it in vim
cd 1/python/;
vim solution.py;
exit 0;

