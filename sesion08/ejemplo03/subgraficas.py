import matplotlib.pyplot as plt

fig, (pl1, pl2) = plt.subplots(2)
x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
num_bins = 6
n, bins, patches = pl2.hist(x, num_bins, facecolor = 'green')
pl1.scatter(x,y)
plt.show()