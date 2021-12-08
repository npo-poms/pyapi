#!/usr/bin/env sh
# simple script to make the npo_ prefixes superflouous
command=$1
shift
if case $command in  "npo_"*) true;; *) false;; esac; then
  $command "$@"
elif [ $(which "npo_$command" > /dev/null ; echo $?)  = 0 ]; then
  npo_$command "$@"
else
  $command "$@"
fi
