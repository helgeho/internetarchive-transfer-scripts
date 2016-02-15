#!/usr/bin/env python2.7

import sys
import internetarchive.search
import os.path
from internetarchive import get_files

collection = sys.argv[1]

list_filename = './' + collection + '_files.txt'
if os.path.exists(list_filename):
	sys.exit(0)

list_file = open(list_filename, 'w+')

search = internetarchive.search.Search('collection:' + collection)
for result in search:
	item_id = result['identifier']
	files = []
	if len(sys.argv) < 2: files = get_files(item_id, glob_pattern='*')
	else:
		for glob in sys.argv[1:]:
			files += get_files(item_id, glob_pattern=glob)
	for file in files:
		list_file.write(item_id + "\t" + file.name + "\n")
