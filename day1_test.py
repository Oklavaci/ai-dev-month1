import torch
import numpy as np
import matplotlib.pyplot as plt

print("PyTorch version:", torch.__version__)

x = torch.tensor([1.0, 2.0, 3.0])
w = torch.tensor([2.0], requires_grad=True)

y = w * x
loss = y.mean()
loss.backward()

print("x:", x)
print("w gradient:", w.grad)

t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 10 * t)

plt.plot(t, signal)
plt.title("10 Hz Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()