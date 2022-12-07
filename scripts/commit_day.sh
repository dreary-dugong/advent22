#!/bin/bash
# create a git commit for a part of a day in advent of code

# check for arguments
if [[ -z $1 ]] ; then
    echo 'ERROR: You must supply a day';
    exit 1;
fi
if [[ -z $2 ]] ; then
    echo 'ERROR: You must supply a part';
    exit 1;
fi
if [[ -z $3 ]] ; then
    echo 'ERROR: You must supply a language';
    exit 1;
fi

# variables
day=$1
part=$2
language=$3
starting_loc=$(pwd);
user=$(whoami);
project_directory="/home/$user/Documents/advent22";
day_directory="$project_directory/day$day";
part_directory="$day_directory/$part"

python_directory="$part_directory/python"
rust_project_directory="$project_directory/rust/advent22day${day}part${part}"

# formatting
if [ $language == "python" ] ; 
then
  cd $python_directory;
  python3 -m black .;
elif [ $language == "rust" ] ; 
then
  cd $rust_project_directory;
  cargo fmt;
else
  echo "ERROR: unknown language $language"
  exit 1;
fi

# git commit
cd $project_directory;
git add "$part_directory/$language";
git commit -m "day $day part $part in $language";

cd $starting_loc;




