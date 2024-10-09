#!/bin/bash

for d in */; do
    echo "Pushing " $d 
    cd $d
    git add .
    git commit -a -m "Automatic Push of $d"
    cd ..
done
echo "Finished"
Sleep 2