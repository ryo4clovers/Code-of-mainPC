from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y = fft(x)
xy = ifft(y)
s = np.allclose(ifft(fft(x)), x, atol=1e-15)  # within numerical accuracy.
print(x, xy, s)
