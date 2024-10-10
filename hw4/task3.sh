#!/bin/bash
#read titanic.csv with cat
#pass it to grep to filter records with class 2
#use grep again to get the records which embarked at Southampton
#modify data from female to M
#modify data from male to M
#Remove data points for which age is absent using regex of grep and use -o flag to print only the matching pattern literals
#Use gawk to find the sum and then average of the second column which is the column with ages
cat titanic.csv | grep  '^[^,]*,[^,]*,2' | grep  -P 'S\r$' | sed 's/female/F/' | sed 's/male/M/' | grep -o  -E  '[MF],[0-9]+' | gawk -F, '{sum+=$2;count++} END {print "Average Age:",sum/count}'