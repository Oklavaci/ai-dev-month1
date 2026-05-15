import numpy as np
import matplotlib.pyplot as plt

# 1. Loss function
def J(w):
    return w**2

# 2. Gradient
def grad_J(w):
    return 2*w

# 3. Gradient descent
learning_rate = 0.4

w = 8.0

trajectory = [w]
losses = [J(w)]

for step in range(25):

    w = w - learning_rate * grad_J(w)

    trajectory.append(w)
    losses.append(J(w))

    print(f"Step {step}: w={w:.5f}, loss={J(w):.5f}")


# 4. Plot loss surface
w_vals = np.linspace(-10, 10, 400)

J_vals = J(w_vals)

plt.figure(figsize=(8,5))

plt.plot(w_vals, J_vals)

plt.scatter(trajectory, [J(t) for t in trajectory])

plt.title("Gradient Descent on J(w)=w²")

plt.xlabel("w")
plt.ylabel("J(w)")

plt.grid(True)

plt.show()


# 5. Plot parameter trajectory
plt.figure(figsize=(8,5))

plt.plot(trajectory, marker='o')

plt.title("Parameter Evolution")

plt.xlabel("Iteration")
plt.ylabel("w")

plt.grid(True)

plt.show()

# 6. Plot loss evolution
plt.figure(figsize=(8,5))

plt.plot(losses, marker='o')

plt.title("Loss Evolution")

plt.xlabel("Iteration")
plt.ylabel("Loss")

plt.grid(True)

plt.show()