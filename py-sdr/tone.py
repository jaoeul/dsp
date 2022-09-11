import numpy as np
import matplotlib.pyplot as plt

# 1 MHz sample rate.
sample_rate = 1e6

# 50 kHz tone frequency.
freq = 50e3

# Genarate tone and noise.
t = np.arange(1024 * 1000) / sample_rate

# Pure sine.
tone = np.sin(2 * np.pi * freq * t)

# Add noise.
tone = tone + 0.2 * np.random.randn(len(t))

plt.figure(0)
plt.plot(t[:200], tone[:200])
plt.show()
