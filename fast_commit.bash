#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./fast_commit.bash 'commit message'"
    exit 1
fi

git add .
git commit -m "$1"
git push
