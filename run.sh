#!/bin/bash


echo "Running on kittens"
/bin/python src/hashcode2017.py input/kittens.in output/kittens.out
echo "Running on me_at_the_zoo"
/bin/python src/hashcode2017.py input/me_at_the_zoo.in output/me_at_the_zoo.out
echo "Running on trending_today"
/bin/python src/hashcode2017.py input/trending_today.in output/trending_today.out
echo "Running on videos_worth_spreading"
/bin/python src/hashcode2017.py input/videos_worth_spreading.in output/videos_worth_spreading.out