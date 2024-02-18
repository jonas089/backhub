# Backhub - a profile based Github repository backup script
A developer's GitHub is their CV & identity => I was worried about downtime and chose to quickly write some subjectively convenient backup scripts that I personally find useful.

## WIP
To be done: Backup private repos.

## Prerequisites
SSH/GPG key setup is not explained here as it is best practice and industry standard.

python3

## Run the backup script

```
python3 backup.py
```

=> enter username, e.g. `$ jonas089`

=> enter the page_size, e.g. amount of repos

=> enter the output path e.g. `$ ./`

Wait as the script clones from your profile repo-by-repo.
