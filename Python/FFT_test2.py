from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 100, 10000, endpoint=False)
sig = np.cos(2 * np.pi * 4 * t)+np.cos(2 * np.pi * 8 * t) + \
    np.cos(2 * np.pi * 15 * t)  # *np.exp(-0.1*t) *5
plt.plot(t, sig)
plt.axis([0, 5, -5, 5])
plt.show()

freq = fft(sig, 1024)
Pyy = np.abs(freq)/1025  # freq*freq.conj(freq)/1025
f = np.arange(1024)
plt.plot(f, Pyy)
plt.axis([0, 200, 0, 1])
plt.show()

t1 = np.linspace(0, 10, 1024, endpoint=False)
sig1 = ifft(freq)
plt.plot(t1, sig1)
plt.axis([0, 5, -5, 5])
plt.show()
