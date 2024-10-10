#!/bin/bash

cat titanic.csv | grep  '^[^,]*,[^,]*,2' | grep  -P 'S\r$' | sed 's/female/F/' | sed 's/male/M/' | grep  -E  '^[1-9]*..,[0-9],2,".*",[MF],[0-9]+' | cut -d '"' -f3 | gawk -F, '{sum+= $3;count++;} END {print "MEAN=",sum/count; print "SUM=",sum;print "COUNT=",count}'