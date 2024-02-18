#!/usr/bin/env bash
username=$1
output_path=$2

# Check if output path extists, otherwise create it
if [ ! -d  $output_path ]; then
	mkdir -p $output_path
else
	:
fi
cd $output_path

# Change the IFS to split by comma
while IFS= read -r repo
do
	echo "Processing $repo for user $username"
	git clone git@github.com:$username/$repo
done
