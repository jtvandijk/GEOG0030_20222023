#!/bin/sh

# commit message
commit=$1
branch=$2

# build bookdown
bash _build.sh

# add files
git add .

# git commit
git commit -m "$commit"

# git push
git push origin $branch
