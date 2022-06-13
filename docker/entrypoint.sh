#!/usr/bin/env sh
# simple script to make the npo_ prefixes superflouous
command=$1
shift
if [ "$command" == "" ] ; then
    echo << EOF
No argument given. Try e.g. following arguments.
# frontend apis
media_get  --help
media_changes  --help
media_follow_changes  --help
media_iterate  --help
media_search  --help
pages_get  --help
pages_search  --help
schedule_get  --help
schedule_search  --help
check_credentials  --help

# backend apis
mediabackend  --help
mediabackend_get  --help
pagesbackend  --help
EOF
    exit
fi
if case $command in  "npo_"*) true;; *) false;; esac; then
  $command "$@"
elif [ $(which "npo_$command" > /dev/null ; echo $?)  = 0 ]; then
  npo_$command "$@"
else
  $command "$@"
fi
