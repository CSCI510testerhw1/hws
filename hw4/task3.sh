#!/bin/bash

#grep -P 'S\r$' titanic.csv | gawk -F, '$3=2' | sed 's/female/F/' | sed 's/male/M/' | cut -d '"' -f3 | grep -E "\s[MF]\s[0-9]" | gawk -F ' ' '{sum+= $2;count++;} END {print "MEAN=",sum/count; print "SUM=",sum;print "COUNT=",count}'
grep  '^[^,]*,[^,]*,2' titanic.csv | grep  -P 'S\r$' | sed 's/female/F/' | sed 's/male/M/'