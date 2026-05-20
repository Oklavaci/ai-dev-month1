import numpy as np
import matplotlib.pyplot as plt

# 1. Generate data
np.random.seed(0)

x = np.linspace(0, 10, 100)

noise = np.random.randn(100) * 2

y = 3*x + 5 + noise


# 2. Design matrix
X = np.column_stack([x, np.ones_like(x)])
print("Design matrix X", X)

# 3. Parameters
theta = np.zeros((2,1))

y = y.reshape(-1,1)

# 4. Training settings
learning_rate = 0.01
epochs = 200

N = len(x)

loss_history = []

# 5. Gradient descent
for epoch in range(epochs):

    # prediction
    y_hat = X @ theta

    # error
    e = y - y_hat

    # loss
    loss = np.mean(e**2)

    loss_history.append(loss)

    # vectorized gradient
    grad = (-2/N) * X.T @ e

    # update
    theta = theta - learning_rate * grad

    if epoch % 20 == 0:
        print(f"Epoch {epoch}: loss={loss:.4f}")

# 6. Final parameters
w = theta[0,0]
b = theta[1,0]

print("\nLearned parameters:")
print("w =", w)
print("b =", b)

# 7. Plot
plt.figure(figsize=(8,5))

plt.scatter(x, y)

plt.plot(x, (X @ theta), linewidth=3)

plt.title("Vectorized Linear Regression")

plt.grid(True)

plt.show()

# 8. Loss curve
plt.figure(figsize=(8,5))

plt.plot(loss_history)

plt.title("Loss Curve")

plt.xlabel("Epoch")
plt.ylabel("MSE")

plt.grid(True)

plt.show()