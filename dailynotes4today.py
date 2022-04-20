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

# Get the author from the config file
def getConfig():
	with open('config', 'r') as cf:
		 settings = cf.readlines()
		 auth = settings[0].split('name=')[1].rstrip()
		 edit = settings[1].split('editor=')[1].split("#")[0].rstrip()
	return auth, edit

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

def checkExist(outn):
	exists = os.path.isfile(outn)
	if exists:
		print('Daily notes for this already exist. Cannot overwrite.')
		sys.exit(2)
	else:
		print('New daily notes called\n{}'.format(outn))

def writeOutput(outn, auth, td):
	with open(outn, 'w') as f:
		#Writing yaml header
		f.write('---\nauthor: {0}\ndate: {1}\n---\n\n\n\n'.format(auth, td))
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

def main():
	# check arguments
	if len(sys.argv) != 1:
		usage()
		sys.exit(2)
	
	# setup notes variables
	now = datetime.datetime.now()
	tdate = '{0}-{1}-{2}'.format(now.year, str(now.month).zfill(2), str(now.day).zfill(2))
	author, editor = getConfig()
	outname = '{0}-dailynotes.md'.format(tdate)
	
	# check if notes for today already exist
	checkExist(outname)	
	
	# write output to file
	writeOutput(outname, author, tdate)	
	
	# This will only work with bbedit installed
	if editor != 'None':
		os.system(f'{editor} {outname}')


if __name__ == "__main__":
	main()


