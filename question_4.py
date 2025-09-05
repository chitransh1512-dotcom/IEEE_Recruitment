import numpy as np
matrix = np.random.randint(1, 101, size=(5, 5))
print("Matrix (5x5):")
print(matrix)
print("Maximum:", matrix.max())
print("Minimum:", matrix.min())
print("Mean:", matrix.mean())
normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("Normalised Matrix:")
print(normalized_matrix)
flattened_sorted = np.sort(matrix.flatten())
print("Flattened Array:")
print(flattened_sorted)
middle_matrix = matrix[1:4, 1:4]
print("Middle Matrix:")
print(middle_matrix)
first_row = middle_matrix[0, :]
last_col = middle_matrix[:, -1]
print("First Row of Middle Matrix:", first_row)
print("Last Column of Middle Matrix:", last_col)
dot_product = np.dot(first_row, last_col)
print("Dot Product:", dot_product)
