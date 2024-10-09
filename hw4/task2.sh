#!/bin/bash
#grep "CSC510" \dataset1/file* | sort | uniq -c | cut -d: -f1 | grep -E -v "[1-2] " | sort -r | grep -E -o "dataset1/file_[0-9]*"
#grep "CSC510" \dataset1/file* | sort | uniq -c | cut -d: -f1 | grep -E -v "[1-2] " | sort -r | gawk '{print $1, $2}'
#grep "CSC510" \dataset1/file* | sort | uniq -c | cut -d: -f1 | grep -E -v "[1-2] " | sort -r | grep -E -o "dataset1/file_[0-9]*" | xargs ls -l | sort -k5,5nr | gawk '{print $9}'
#grep "CSC510" \dataset1/file* | sort | uniq -c | cut -d: -f1 | grep -E -v "[1-2] " | grep -E -o "dataset1/file_[0-9]*" | xargs ls -l | sort -k5,5nr | gawk '{print $9}' | xargs grep "CSC510" | cut -d: -f1 | uniq -c | sort -r | grep -E -o "file_[0-9]*" | sed 's/file_/filtered_/'

grep -rl "sample" dataset1/file* | xargs grep -c "CSC510" | awk -F: '$2 >= 3' | gawk -F: '{cmd="ls -l \"" $1 "\" | cut -d\" \" -f5"; cmd | getline size; close(cmd); print $1 ":" $2 ":" size}' | sort -t: -k2,2nr -k3,3nr | cut -d: -f1 | sed 's/.*\/file_/filtered_/'

#Output
#file_20
#file_10
#file_4
#file_24
#file_14
#file_22
#file_2
#file_30
#file_3
#file_23
#file_13
#file_12