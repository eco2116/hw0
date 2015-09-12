# Evan O'Connor (eco2116)
# Intro to Databases
# hw0
# scotch.py

import csv
with open('iowa-liquor-sample.csv') as csvfile:
	reader = csv.reader(csvfile)
	i=0
	for row in reader:
		for entry in row:
			if 'single malt scotch' in entry.lower():
				i += 1
print i
