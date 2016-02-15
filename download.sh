#!/bin/sh
./create_filelist.py $1 *.cdx *.cdx.gz *.warc.gz
./download_files.py $1 /mnt/ephemeral0/holzmann/tmp /user/holzmann/ia1
