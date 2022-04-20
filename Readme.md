# Custom MD Notes Template

Created by [Sarah Stevens](https://github.com/sstevens2/)


## Setup

- Update the `config` file include:
	+ your name
	+ favorite command line text editor (leave as None if you don't want it to open the new daily notes in your favorite text editor)
- Run `pip install -r requirements.txt` to install the required packages or `conda create --name <env> --file requirements.txt` to create a conda environment.

## Usage

### Regular daily notes

To make new notes for the day run:
```
python dailynotes4today.py
```
This script will make a a new notes file for today and 
copy over any notes for in the "## Goals for other days this week or later" section.

### Current projects lists

The `current_projs_lists.md` file is an on-going file of current responsibilities. 


## Todo items

- add in scripts to parse weekly notes into single result file
- option to specify file to write to??? See if you need this option?
- Maybe option for making meeting notes template??? maybe with google doc option (if I could figure out API)



