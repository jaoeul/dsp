import numpy as np
import matplotlib.pyplot as plt

# 1 MHz sample rate.
sample_rate = 1e6

# 50 kHz tone frequency.
freq = 50e3

# FFT size.
fft_size = 1024

# Genarate tone and noise.
t = np.arange(1024 * 1000) / sample_rate

# Pure sine.
tone = np.sin(2 * np.pi * freq * t)

# Add noise.
tone = tone + 0.2 * np.random.randn(len(t))

# Limit working set to the fft size.
working_set = tone[:fft_size]

# Calculate the power spectral density.
psd = (np.abs(np.fft.fft(working_set)) / fft_size) ** 2

# Convert to dB.
psd_log = 10.0 * np.log10(psd)

# Perform the fft shift.
psd_shift = np.fft.fftshift(psd_log)

# Frequency we tuned our SDR to.
center_freq = 2.4e9

# X-axis.
f = np.arange(freq / -2.0, freq / 2.0, freq / fft_size)

# Add the center freq.
f += center_freq

plt.plot(f, psd_shift)
plt.show()
