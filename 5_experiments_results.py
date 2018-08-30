# analysis of experimental results

# BEFORE YOU RUN THIS SCRIPT:
# 1. CREATE A DIR CALLED 'results' - from cmd line type 'mkdir results'
# 2. MOVE ALL *.csv MODEL OUTPUT FILES INTO 'results'
# 3. DOING IT THIS WAY ALLOWS YOU TO CREATE AN ARBITRARY # OF MODELS TO TEST
#    AND YOU CAN STILL RUN THIS SCRIPT WITHOUT TYPING OUT ALL THE FILE NAMES


from os import listdir
from pandas import read_csv
from pandas import DataFrame
from matplotlib import pyplot

# load all .csv results into a dataframe
train, test = DataFrame(), DataFrame()
directory = 'results'
for name in listdir(directory):
    if not name.endswith('csv'):
        continue
    filename = directory + '/' + name
    data = read_csv(filename, header=0)
    experiment = name.split('.')[0]
    train[experiment] = data['train']
    test[experiment] = data['test']

# plot results on train
train.boxplot(vert=False)
pyplot.show()
# plot results on test
test.boxplot(vert=False)
pyplot.show()