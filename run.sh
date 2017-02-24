#!/bin/bash

cwd=`pwd`
files=`ls ${cwd}/input`

for file in $files
do
    filename=$(basename "$file")
    #extension="${filename##*.}"
    filename="${filename%.*}"
    echo "Running on ${filename}."
    /usr/bin/python src/hashcode2017.py input/$file output/${filename}.out
done

