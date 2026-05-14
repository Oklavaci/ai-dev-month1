import numpy as np
import matplotlib.pyplot as plt

# 1. Generate synthetic data
np.random.seed(0)

x = np.linspace(0, 10, 100)

noise = np.random.randn(100) * 2

y = 3*x + 5 + noise

# 2. Initialize parameters
w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 100

N = len(x)

loss_history = []


# 3. Training loop
for epoch in range(epochs):

    # prediction
    y_hat = w*x + b

    # loss
    loss = np.mean((y - y_hat)**2)

    loss_history.append(loss)

    # gradients
    dw = (-2/N) * np.sum(x * (y - y_hat))
    db = (-2/N) * np.sum(y - y_hat)

    # parameter update
    w = w - learning_rate * dw
    b = b - learning_rate * db

    print(f"Epoch {epoch}: loss={loss:.3f}")


# 4. Final prediction
y_final = w*x + b

print("\nLearned parameters:")
print("w =", w)
print("b =", b)

# 5. Plot regression
plt.figure(figsize=(8,5))

plt.scatter(x, y, label="Data")

plt.plot(x, y_final, linewidth=3, label="Regression Line")

plt.xlabel("x")
plt.ylabel("y")

plt.title("Linear Regression")

plt.legend()
plt.grid(True)

plt.show()

# 6. Plot loss curve
plt.figure(figsize=(8,5))

plt.plot(loss_history)

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")

plt.title("Training Loss")

plt.grid(True)

plt.show()