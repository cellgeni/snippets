import json
import sys

if len(sys.argv) != 2:
	print("""
	This script cleans notebook outputs that are larger than 1000 items
	USAGE: clean_large_notebook_outputs.py my_notebook.ipynb
	The script will create my_notebook_mod.ipynb""")
	sys.exit("Please provide path to notebook")


fname = sys.argv[1]
with open(fname) as f:
	d = json.loads(f.read())
	
max_size = 1000

for i in range(len(d['cells'])):
 if 'outputs' in  d['cells'][i]:
  if len(d['cells'][i]['outputs']) > max_size:
   d['cells'][i]['outputs'] = []
   
   

with open(fname+"_mod.ipynb", 'w') as f:
    json.dump(d, f)
