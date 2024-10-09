#!/bin/bash
#first get all the records that embarked in southampton
#then filter these records with the condition 2nd class
#Replace Female with F and Male with M in that order. We get the following example:
#882 0 2 "Markun  Mr. Johann" M 33 0 0 349257 7.8958  S
#Then use " as delimiter and get the 3rd column after the name. 
#After delimiting using " , the third column/field will have a set of columns as shown below:
#F 25 0 1 230433 26  S
#The second column in that is age
#Sum the age and calculate the mean
grep -P 'S\r$' titanic.csv | gawk -F, '$3=2' | sed 's/female/F/' | sed 's/male/M/' | cut -d '"' -f3 | gawk -F ' ' '{sum+= $2;count++;} END {print "MEAN=",sum/count}' 