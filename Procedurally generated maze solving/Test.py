import os
import sys
import subprocess
import time
import numpy as np
from PIL import Image
#by Yusdel Lorenzo 2019
cpuTrials = []
path = os.getcwd() + '/Solver.py'
for file in os.listdir(os.getcwd()+'/TestSet/'):
    if file.endswith(".jpg"):
        img_path = os.getcwd() + '/TestSet/' + file
        print('\nRunning A Star on: ' +file)
        t0 = time.time()
        subprocess.call(['python', 'Solver.py', img_path, "result.png"])
        t1 = time.time()
        total = t1-t0
        cpuTrials.append(total)
        print('Finished in: ' + str(total) +' seconds')
        img = Image.open('result.png')
        choice = input('Open result image? \nEnter: Y or N -> ')
        if choice == 'Y' or choice == 'y':
            img.show()
cpuAverage = str(np.mean(cpuTrials))
print('\nAverage time: '+ cpuAverage + 'seconds')
