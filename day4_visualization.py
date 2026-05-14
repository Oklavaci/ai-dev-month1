import numpy as np
import matplotlib.pyplot as plt

# 1. Time axis
fs1 = 1000
fs2 = 200
t1 = np.linspace(0, 1, fs1)
t2 = np.linspace(0, 1, fs2)

# 2. Pure signal
f1 = 5
f2 = 120
signal1 = np.sin(2 * np.pi * f1 * t1)
signal2 = np.sin(2 * np.pi * f2 * t2)
signal3 = np.sign(np.sin(2 * np.pi * f1 * t1)) + signal1

# 3. Noise
noise1 = 0.3 * np.random.randn(len(t1))
noise2 = 0.3 * np.random.randn(len(t2))
noisy_signal1 = signal1 + noise1
noisy_signal2 = signal2 + noise2
noisy_signal4 = signal2 + 3 * noise2
noisy_signal3 = signal3 + noise1

# 4. FFT
fft_vals = np.fft.fft(noisy_signal2)
fft_freq = np.fft.fftfreq(len(t2), d=1/fs2)
magnitude = np.abs(fft_vals)

# 5. Plot time domain
plt.figure(figsize=(10,5))

plt.plot(t1, noisy_signal1)
plt.plot(t2, noisy_signal2)
plt.plot(t1, noisy_signal3)
plt.plot(t2, noisy_signal4)


plt.title("Noisy Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()


# 6. Plot frequency domain
plt.figure(figsize=(10,5))

plt.plot(fft_freq[:fs2//2], magnitude[:fs2//2])

plt.title("FFT Magnitude Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)

plt.show()

# 7. Histogram
plt.figure(figsize=(8,5))

plt.hist(noise2, bins=30)

plt.title("Noise Distribution")
plt.xlabel("Value")
plt.ylabel("Count")

plt.show()