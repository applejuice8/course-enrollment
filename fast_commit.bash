#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./fast_commit.bash 'commit message'"
    exit 1
fi

echo
echo "Executing 'git add .'"
git add .

echo
echo "Executing 'git commit -m \"$1\"'"
git commit -m "$1"

echo
echo "Executing 'git push'"
git push
