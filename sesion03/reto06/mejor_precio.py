import numpy as np

a = np.array([["", "Acapulco", "Los Cabos", "Cancun"],
              ["Hospedaje", 1500, 3000, 4500], 
              ["Transporte", 800, 1200, 100], 
              ["Excursion", 500, 800, 1200], 
              ["Comida", 120, 240, 360]])

print(a.T[1, 1:])
lowest_sum = np.sum(a.T[1, 1:])
lowest_index = 1
for column in a.T[1:]:
    if np.sum(column) < lowest_sum:
        lowest_sum = np.sum(column)
        lowest_index = np.sum()

print(a)
print("El mejor precio es {} por {}".format(a[0][lowest_index], lowest_sum))