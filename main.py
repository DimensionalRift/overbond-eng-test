from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import dates


def parseLine(line, rec):
    if line[0:4] == "BDBo":
        # Note we check if the record is empty first as there's no point in storing a DIs with no data to graph
        # We have a BDBo, and the DIs is in position 5 of the line
        # Once again I'm using existing structure to speed up the computation
        # I could also check each position individually

        split_line = line.split(';')
        DI = (split_line[5])[3:]# Take only the number from DI
        # Now we have to convert this into a string of the format: DD-MMM-YY
        # I'm going to use datetime and turn it back into a string as its neater than using if statements
        DTDI = datetime(year=int(DI[0:4]), month=int(DI[4:6]), day=int(DI[6:8]))

        rec['DIs'] = DTDI.strftime("%d-%b-%y")

    if line[0] == 'm':
        split_line = line.split(';')
        for entry in split_line: # Have to go through all as there is missing data
            if entry[0:3] == 'BPr':
                rec['BPr'] = (float(entry[3:]))
            if entry[0:3] == 'APl':
                rec['APl'] = (float(entry[3:]))
            if entry[0:2] == 'Pl':
                rec['Pl'] = (float(entry[2:]))

    return rec

def parseRecords(file):
    records = []
    while file.readline() != '': # Will read the first line of every 10 rows, which is not useful data
        record = {}
        for i in range(9): # Now we will look through the remaining 9 rows for useful data
            # We want lines that start with BDBo for DIs
            # We want lines that start with m for BPr
            # We want lines that start with m for APl'
            # We want lines that start with m for Pl
            # I've made the decision to only scan for these lines as the dataset
            # Appears to have a consistent structure, and only looking for these
            # lines saves time.
            # If this were more disorganized I would have to use more general,
            # less efficient methods like scanning every part of every line
            record = parseLine(file.readline(), record)

        records.append(record) #We include empty records as well

    return records

if __name__ == '__main__':
    file = open("XICE_Bond_Close2.tip", encoding="utf8")
    #
    records = parseRecords(file) # List for storing records
    # A record is a dictionary
    file.close()

    # Now we will graph the records

    for record in records:

        if "BPr" in record:
            plt.scatter(record['DIs'], record['BPr'],  color ='blue')
        if "APl" in record:
            plt.scatter(record['DIs'], record['APl'],  color= 'orange')
        if "Pl" in record:
            plt.scatter(record['DIs'], record['Pl'],  color = 'gray')
    patches = []
    plt.xticks(rotation=270) #Had to rotate the labels so as to not have them overlap
    plt.tight_layout()
    patches.append(mpatches.Patch(color='blue', label='BPr'))
    patches.append(mpatches.Patch(color='orange', label='APl'))
    patches.append(mpatches.Patch(color='gray', label='Pl'))

    plt.legend(handles=patches)
    ax = plt.gca()
    ax.xaxis.set_major_locator(dates.AutoDateLocator())
    # Too many dates to list one by one
    plt.show()

