#!/usr/bin/env sh
# simple script to make the npo_ prefixes superflouous
command=$1
shift
if case $command in  "npo_"*) true;; *) false;; esac; then
  $command "$@"
else
  npo_$command "$@"
fi
