#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR

for d in */; do
    echo "Pulling " $d 
    cd $d
    git pull
    cd ..
done
echo "Finished"
Sleep 2