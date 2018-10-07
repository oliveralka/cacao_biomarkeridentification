# To parse OpenMS .consensusxml and extract filenames from map or QBIC Barcode

import re
import csv

# path to consensusXML
filepathin = 
# path to output.csv
filepathout =

f = open(filepathin, 'r')
fo = open(filepathout, 'w')
lmap = []

#grep consensusXML map entry
for line in f.readlines():
        if re.compile('<map id.*>').search(line):
            lmap.append(line)
lmap = map(str.strip, lmap)

#grep names from map entry
id = []
names = []
for i in lmap:
    #m = re.search('09116(.+?).featureXML',i).group(1)
    n = re.search('map id="(\d+)"',i).group(1)
    m = re.search('centroided_(.+?)_',i).group(1)
    id.append(n)
    names.append(m)

rows = zip(id, names)

writer = csv.writer(fo, dialect='excel')
for row in rows:
    writer.writerow(row)



