import numpy as np
import matplotlib.pyplot as plt

Fs = 1 # Hz
N = 100

t = np.arange(N)
sig = np.sin(0.15 * 2 * np.pi * t)

fft = np.fft.fft(sig)
fft_shift = np.fft.fftshift(fft)

fft_mag = np.abs(fft_shift)
fft_phase = np.angle(fft_shift)

f = np.arange(Fs / -2, Fs / 2, Fs / N)

plt.figure(0)
plt.plot(f, fft_mag, '.-')

plt.figure(1)
plt.plot(f, fft_phase, '.-')

hamming = fft_shift * np.hamming(N)

plt.figure(2)
plt.plot(t, hamming, '.-')


plt.show()
