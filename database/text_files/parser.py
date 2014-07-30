#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2014-07-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""
import sqlite3 as lite
import sys
import os


def main():
	file_extension='txt'
	filename = "stream_of_consciousness_1"
	file_pointer = open(filename+'.'+file_extension)
	i = 0
	infomation = []
	for line in file_pointer:
		i=i+1
		#print str(i) + " " + line
		line = line.strip('\n')
		parsed_line = line.split('\t')
		print parsed_line
		infomation.append(parsed_line)
	



	con = lite.connect('../paper_data.db')

	with con:
		cur = con.cursor()    
		cur.execute("DROP TABLE IF EXISTS {0}".format(filename))
		cur.execute("CREATE TABLE {0}(label TEXT, entry TEXT)".format(filename))
		cur.executemany("INSERT INTO {0} VALUES( ?, ?)".format(filename), infomation)

if __name__ == '__main__':
	main()

