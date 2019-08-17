import sys       
import subprocess
import re

#Yusdel Lima Lorenzo

# Calls the R system specifying that commands come from file commands.R
# The commands.R provided with this assignment will read the file named
# data and will output a histogram of that data to the file pageshist.pdf
def runR( ):
    res = subprocess.call(['R', '-f', 'commands.R'])

# log2hist analyzes a log file to calculate the total number of pages
# printed by each user during the period represented by this log file,
# and uses R to produce a pdf file pageshist.pdf showing a histogram
# of these totals.  logfilename is a string which is the name of the
# log file to analyze.
#
def log2hist(logfilename):
    log = open('log', 'r')
    users = {}
    for printString in log:
        line = re.search('user:\s*(?P<user>.*)\s*printer:.*?pages:\s*(?P<pages>\d+)', printString)
        if line:
            userStr = line.group('user')
            userStr.strip()
            count = int(line.group('pages'))
            if userStr in users:
                users[userStr] += count
            else:
                users[userStr] = count
    data = open('data', 'w+')
    for count in users.values():
    	data.write('%d\n' % count)
    data.close()
    log.close()
    
    runR() 
        
    return

if __name__ == '__main__':
    log2hist('log')
