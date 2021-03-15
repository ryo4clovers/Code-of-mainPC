import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

from scipy import signal
import matplotlib.pyplot as plt
t = np.linspace(-1, 1, 200, endpoint=False)
sig = np.cos(2 * np.pi * 7 * t) + signal.gausspulse(t - 0.4, fc=2)

# **以下二行追加**
plt.plot(t, sig)
plt.pause(3)
# ******

widths = np.arange(1, 31)
cwtmatr = signal.cwt(sig, signal.ricker, widths)
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
           vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
plt.show()
