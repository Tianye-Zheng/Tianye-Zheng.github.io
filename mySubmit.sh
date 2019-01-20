#!/bin/bash

git add .
#if[! $1 ]; then
#	$1='my commit'
#fi
git commit -m "$1"
git push -u origin master
