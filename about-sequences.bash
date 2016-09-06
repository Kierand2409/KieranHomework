#!/bin/bash
cd ..
cd ..
cd compskillsf16
cd Homework
cd Resources

echo "Kieran, summary of about-sequences" >output.txt

pwd >>output.txt

echo "Number of sequences:" >>output.txt

grep ">" HW1-sequences.fsa >temp.txt
wc -l temp.txt >>output.txt

tail --lines=12 HW1-sequences.fsa >>output.txt
