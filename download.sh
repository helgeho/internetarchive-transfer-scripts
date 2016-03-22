#!/bin/sh
./create_filelist.py $1 *.cdx *.cdx.gz *.warc.gz
hadoop fs -ls /user/holzmann/ia1/$1/*/* | awk '{print $8}' | rev | cut -d'/' -f 1 | rev > $1_done.txt
./download_files.py $1 /mnt/ephemeral0/holzmann/tmp /user/holzmann/ia1
