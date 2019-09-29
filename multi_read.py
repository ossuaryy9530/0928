import sys
import glob
import os

for input_file in glob.glob(os.path.join(".", "*.txt")):
    with open(input_file, 'r') as filereader:
        
        for row in filereader:
            print("======")
            print("{}".format(row.strip()))
    filereader.close()
