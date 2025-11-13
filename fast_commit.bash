#!/bin/bash

msg="$*"

if [ -z "$msg" ]; then
    echo "Usage: ./fast_commit.bash 'commit message'"
    exit 1
fi

echo
echo "Executing 'git add .'"
git add .

echo
echo "Executing 'git commit -m \"$msg\"'"
git commit -m "$msg"

echo
echo "Executing 'git push'"
git push
