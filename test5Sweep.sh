#!/bin/bash

# Student Name: Mugdha Chakma
# Student ID  : 22122847

exp_dir=test5sweep`date "+%Y-%m-%d_%H.%M.%S"` # create name for directory - includes timestamp
mkdir $exp_dir                                # make directory for experiment

cp test5.py $exp_dir # copy test5.py file to the test5sweep directory
cp test5Sweep.sh $exp_dir # copy script file to the test5sweep directory
cd $exp_dir # change directory to test5sweep
low_r=$1 # initialize value to variable low_r from first argument of the command
hi_r=$2 # initialize value to variable hi_r from second argument of the command
step_r=$3 # initialize value to variable step_r from third argument of the command
low_a=$4 # initialize value to variable low_a from fourth argument of the command
hi_a=$5 # initialize value to variable hi_a from fifth argument of the command
step_a=$6 # initialize value to variable step_a from sixth argument of the command

echo "Parameters are: "   # print in the terminal
echo "R values : " $low_r $hi_r $step_r # print R values low r high r and step r  
echo "A values : " $low_a $hi_a $step_a # print A values low a high a and step a

for r in $(seq $low_r $step_r $hi_r); # for loop from low r to hi r with increment by steps r 
do
    for a in $(seq $low_a $step_a $hi_a); # nested for loop from low a to hi a with increment by steps a
    do
        echo "Experiment: " $r $a # print value of r and a
        python test5.py $r $a > "SIR_Model_r_${r}_a_${a}.csv"
	echo
    done
done
