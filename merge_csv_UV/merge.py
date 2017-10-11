import pandas as pd
import numpy as np
import glob

### I want to merge .csv fils generated from Beckmann UV-Vis to one .csv file

# glob generates a list of filename with .csv
# * means everything, there are other arguments too
datasets = glob.glob('*.csv')

# print here is just to get an idea of how glob works

#print type(datasets)
#print datasets
#print len(datasets)
#print range(len(datasets))


# generate an empty DataFrame for concat.
frames = pd.DataFrame()

# write a for loop
# read_csv as DataFrame
# pd.read_csv(filename, sep = delimiter, header = starting row, skiprows = skip the rows after header, 
# names = name for the columns, nrows = read these rows after skiprows)
# I name the column by filename
# concat the starting empty DataFrame with the ones read, axis = 1 makes it append along the columns
# not exactly sure how it works, but it works this way

for idx in range(len(datasets)):
    frame_right = pd.read_csv(datasets[idx], sep = ',,', skiprows = 48, nrows = 91, header = None, names = ['Time', datasets[idx]])
    frames = pd.concat([frames,frame_right], axis = 1)

# print here is also just to get an idea of how final looks like

#print frames                                                                                                            

frames.to_csv('test.csv', header = True)
