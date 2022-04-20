#! /usr/bin/env python3

"""dailynotes4today.py : Setup dailynotes each day"""

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

import pandas as pd, sys, os
import datetime
import glob
import os

def usage():
	print("Usage: dailynotes4today.py")
	print("This script by default takes no args and it makes and sets up \
			a new daily notes file with today's date. If one exists you can add \
			an arg to name the new file.")

if len(sys.argv) != 1:
	usage()
	sys.exit(2)


# Get the author from the config file
def getAuthor():
	with open('config', 'r') as cf:
		 configfile = cf.read()
		 auth = configfile.split('name=')[1]
	return auth

# Get last notes and carry over the long term goals list
def carryover():
	try:
		noteslist = sorted(glob.glob('*-dailynotes.md'))
		noteslist.remove('template-dailynotes.md') # removing template from list of notes
		lastnotes = noteslist[-2] # -1 will be today's notes
	except IndexError:
		print("No Lastnotes")
		return ''
	if len(noteslist) == 2: # if no previous notes exist in the current folder, use template
		lastnotes = 'template-dailynotes.md'
	with open(lastnotes,'r') as ln:
		lnitems = ln.read().split(  \
		'## Goals for other days this week or later')[1].split(  \
		'<!--- END OF GOALS SECTION -->')[0]
		return lnitems

def main():
	# setup notes variables
	now = datetime.datetime.now()
	tdate = '{0}-{1}-{2}'.format(now.year, str(now.month).zfill(2), str(now.day).zfill(2))
	author = getAuthor()
	outname = '{0}-dailynotes.md'.format(tdate)
	
	# check if notes for today already exist
	exists = os.path.isfile(outname)
	if exists:
		print('Daily notes for this already exist. Cannot overwrite.')
		sys.exit(2)
	else:
		print('New daily notes called\n{}'.format(outname))
	
	
	# write output to file
	with open(outname, 'w') as f:
		#Writing yaml header
		f.write('---\nauthor: {0}\ndate: {1}\n---\n\n\n\n'.format(author, tdate))
		# Writing main text
		f.write('## Goals for today\n\n\n\n')
		f.write('## Goals for other days this week or later')
		carry = carryover()
		if carry == '':
			f.write('\n')
		else:
			f.write(carry)
		f.write('<!--- END OF GOALS SECTION -->\n\n\n')
		f.write('## Other notes / Links to other notes\n\n\n\n')
		f.write('### Notes from work\n\n\n\n')
	
	
	# This will only work with bbedit installed
	os.system('bbedit {}'.format(outname))


if __name__ == "__main__":
	main()


