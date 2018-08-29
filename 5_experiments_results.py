# analysis of experimental results

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