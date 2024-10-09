#!/bin/bash
grep -P 'S\r$' titanic.csv | gawk -F, '$3=2' | sed 's/female/F/' | sed 's/male/M/' | cut -d '"' -f3 | gawk -F ' ' '{sum+= $2;count++;} END {print "MEAN=",sum/count}' 