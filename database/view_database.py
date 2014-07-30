#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2014-07-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sqlite3 as lite
import sys


con = lite.connect('paper_data.db')

with con:    
    filename = "stream_of_consciousness_1"
    cur = con.cursor()    
    cur.execute("SELECT * FROM "+filename )

    rows = cur.fetchall()

    for row in rows:
        print row
