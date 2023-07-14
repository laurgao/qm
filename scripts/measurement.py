import numpy as np

# Define a matrix
ket_0 = np.array([1, 0])
A = np.outer(ket_0, ket_0)

# Compute the product of the matrix and its conjugate transpose
A_conj = np.conj(A.T)
A_prod = np.dot(A, A_conj)

# Compute the identity matrix of the same size as the original matrix
I = np.eye(A.shape[0])

# Check if the matrix is unitary
is_unitary = np.allclose(A_prod, I)

print("Matrix A:\n", A)
print("Is A unitary?", is_unitary)
