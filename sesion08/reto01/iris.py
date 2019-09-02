import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print("{:7}: {:.2f}".format("Media", mu))
print("{:7}: {:.2f}".format("Mediana", med))
print("{:7}: {:.2f}".format("Des std", sd))
