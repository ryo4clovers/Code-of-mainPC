# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from swan import pycwt
import matplotlib.pyplot as plt

# 読み込み(\→/ 変換推奨，ヘッダーなし，6行スキップ)
input_data = pd.read_table(
    "D:/iriwa/デスクトップ/Code/Project_Python/test.txt", header=None, skiprows=6)
print(input_data)

# 書き出しファイル名(\→/ 変換推奨)
#output_filename = "D:/iriwa/デスクトップ/Code/Project_Python/test.xlsx"

x = input_data.iloc[:, 0]
y = input_data.iloc[:, 1]

plt.plot(x, y)
plt.show()

Fs = 100
omega0 = 8
# Freqを指定してcwt
freqs = np.arange(0.1, 30, 0.025)
r = pycwt.cwt_f(y, freqs, Fs, pycwt.Morlet(omega0))
rr = np.abs(r)

plt.rcParams['figure.figsize'] = (20, 6)
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.75, 0.7, 0.2])
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.60], sharex=ax1)
ax3 = fig.add_axes([0.83, 0.1, 0.03, 0.6])

ax1.plot(x, y, 'k')

img = ax2.imshow(np.flipud(rr), extent=[0, 20, freqs[0], freqs[-1]],
                 aspect='auto', interpolation='nearest')

fig.colorbar(img, cax=ax3)

plt.show()

# 書き出し
#input_data.to_excel(output_filename, sheet_name="analyze")
