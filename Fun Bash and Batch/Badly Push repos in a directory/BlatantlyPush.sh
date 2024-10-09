#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR

for d in */; do
    echo "Pushing " $d 
    cd $d
    git add .
    git commit -a -m "Automatic Push of $d"
    git push
    cd ..
done
echo "Finished"
Sleep 2