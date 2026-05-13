import numpy as np

# 1. Vector
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print("x:", x)
print("y:", y)
print("x + y:", x + y)
print("x * y:", x * y)
print("dot product:", np.dot(x, y))

# 2. Matrix
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[10, 20],
              [30, 40],
              [50, 60]])

print("A shape:", A.shape)
print("B shape:", B.shape)
print("A @ B:")
print(A @ B) # Matrix multiplication (dot product)

# 3. Slicing
M = np.arange(1, 17).reshape(4, 4)

print("M:")
print(M)

print("first row:", M[0, :])
print("first column:", M[:, 0])
print("top-left 2x2:")
print(M[:2, :2])

# 4. Broadcasting
v = np.array([1, 2, 3, 4])

print("M + v:")
print(M + v)

# 5. Manual mean and variance
data = np.array([2, 4, 6, 8, 10])

manual_mean = np.sum(data) / len(data)
manual_variance = np.sum((data - manual_mean) ** 2) / len(data)

print("manual mean:", manual_mean)
print("numpy mean:", np.mean(data))

print("manual variance:", manual_variance)
print("numpy variance:", np.var(data))


##############
I = np.eye(3)
print("Identity matrix I:")
print(I)


print("P_vec = I @ v[:3]:")
P_vec = I @ v[:3]
print(P_vec)

print("P = I + v[:3]:")
P = I + v[:3]
print(P)

print("Transpose of P:")
print(P.T)

print("Mean of the first row of P:")
print(np.mean(P[0, :]))

print("Mean of the first col of P:")
print(np.mean(P[:, 0]))

# Collapse into a column vector of row means
row_means = np.mean(P, axis=1, keepdims=True)
print("Row means of P (as a column vector):")
print(row_means)    

# Collapse into a row vector of column means
col_means = np.mean(P, axis=0, keepdims=True)
print("Column means of P (as a row vector):")
print(col_means)