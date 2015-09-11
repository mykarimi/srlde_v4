#!/usr/bin/env python
"""Author: M. Yassine Karimi"""
"""Date: July the 14th, 2015"""
"""Project BiographyNet: "Time Will Tell A Different Story" """
"""VU University Amsterdam"""

import os
import sys
import glob   
import csv
import fileinput
import lxml
import itertools
from os import listdir
from collections import Counter
sys.path.append('/home/yassine/twtads/KafNafParserPy')
from KafNafParserMod import *

for files in os.listdir('weyerman-processed/'):
	my_parser = KafNafParser('weyerman-processed/'+files) 
	
	filename = files
	target = open('weyerman-extracted/'+filename+'.csv','w')
	for predicate in my_parser.get_predicates():
	    	my_predicates = ''
	   	for predid in predicate.get_span().get_span_ids():
	     		pred = my_parser.get_term(predid)
	    		tokspan = pred.get_span().get_span_ids()
			for tokid in tokspan:
	      	 		token = my_parser.get_token(tokid)
	     	 		ttext = token.get_text()
 			my_predicates += ttext + ''
		for role in predicate.get_roles():
   			my_tokens = ''
  			for termid in role.get_span().get_span_ids():
      				term = my_parser.get_term(termid)
      				tokspan = term.get_span().get_span_ids()
				for tokid in tokspan:
        				token = my_parser.get_token(tokid)
        				ttext = token.get_text()
					pos = term.get_pos()
    				my_tokens += ttext + ' '
 			target_text = "%s\t%s\t%s\n" % (my_predicates.rstrip(),role.get_sem_role(),my_tokens.rstrip())
		target.write(target_text.encode('utf-8'))	
	target.close()



