#!/usr/bin/env python2.7

import sys
import os
from internetarchive import get_item

collection = sys.argv[1]
staging_path = sys.argv[2]
hdfs_path = sys.argv[3]

list_file = open('./' + collection + '_files.txt')
done_file = open('./' + collection + '_done.txt', 'a')

done = [line.rstrip('\n') for line in open('./' + collection + '_done.txt')]
staging = []

# clear staging path
if os.path.exists(staging_path + "/" + collection):
	os.system("rm -r " + staging_path + "/" + collection)
os.system("mkdir -p " + staging_path + "/" + collection)

max_staging = 10
for line in [line.rstrip("\n") for line in list_file]:
        segments = line.split("\t")
        item_id = segments[0]
        filename = segments[1]
	if (filename not in done) and (filename not in staging):
		no_gz = filename.lower().rstrip(".gz")
		ext = no_gz.split(".")[-1]

		os.system("mkdir -p " + staging_path + "/" + collection + "/" + ext)

		item = get_item(item_id)
		file = item.get_file(filename)
		while True:
			try:
				file.download(staging_path + "/" + collection + "/" + ext + "/" + filename)
				break
			except Exception as e:
				print "Error (" + str(e) + "), try again..."

		staging.append(filename)
		if len(staging) >= max_staging:
			os.system("hadoop fs -copyFromLocal " + staging_path + "/" + collection + " " + hdfs_path)
			os.system("rm -r " + staging_path + "/" + collection)
			for staged in staging:
				done.append(staged)
				done_file.write(staged + "\n")
			staging = []

os.system("hadoop fs -copyFromLocal " + staging_path + "/" + collection + " " + hdfs_path)
os.system("rm -r " + staging_path + "/" + collection)
for staged in staging:
	done_file.write(staged + "\n")
