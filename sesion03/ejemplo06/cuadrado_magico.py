import numpy as np

arr = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])

def es_cudrado_magico(arr):
    value = np.sum(arr[0])
    for row in arr:
        if np.sum(row) != value:
            return False
    for column in arr.T:  # Traspuesta
        if np.sum(column) != value:
            return False
    return True


arr = np.array([[2, 7, 6], [9, 1, 5], [3, 4, 8]])

if __name__ == "__main__":
    print(arr)
    result = es_cudrado_magico(arr)
    print("Es cuadrado mágico? {}".format(result))