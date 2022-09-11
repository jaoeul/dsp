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

# Calculate avrage power using mean.
avg_pwr1 = np.mean(np.abs(tone)**2)

# Calculate avrage power using variance.
avg_pwr2 = np.var(tone)

print(avg_pwr1)
print(avg_pwr2)
