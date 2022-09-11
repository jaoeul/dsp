import numpy as np
import matplotlib.pyplot as plt

# Sampling rate.
Fs = 300

# Sampling period.
Ts = 1 / Fs

# Numbers of samples to simulate.
N = 2048

# Time, steps size of sampling period.
t = Ts * np.arange(N)

# Simulated sinusoid at 50 Hz.
x = np.exp(1j * 2 * np.pi * 50 * t)

# Add complex noise wit unity power.
n = (np.random.randn(N) + 1j * np.random.randn(N)) / np.sqrt(2)
noise_power = 2
r = x + n * np.sqrt(noise_power)

psd = (np.abs(np.fft.fft(r)) / N) ** 2
psd_log = 10.0 * np.log10(psd)
psd_shift = np.fft.fftshift(psd_log)

f = np.arange(Fs / -2.0, Fs / 2.0, Fs / N)

plt.plot(f, psd_shift)
plt.xlabel("Freq, Hz")
plt.ylabel("Magnitude, dB")
plt.grid(True)
plt.show()
