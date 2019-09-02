import numpy as np

a = np.array(([2, 1, -3], [5, -4, 1], [1, -1, -4]))
b = np.array(([7, -19, 4]))

x = np.linalg.solve(a, b)

print("Resultados:",  x)

# Validando
valido = np.allclose(np.dot(a, x), b)
print("Resultado valido: ", valido)
