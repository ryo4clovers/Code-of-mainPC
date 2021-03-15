# -*- coding: utf-8 -*-
"""
    EEG.py
        For the study
        EEG spectrum analysis program
        input  : EEG data by Labchart (.txt)
        output : MPF / α / β / θ / δ (.csv)

        研究用
        脳波スペクトル解析プログラム
        読込：Labchartデータをtxtデータに変換したデータ
        出力：MPF，α・β・θ・δ波比率データをcsvデータに出力
"""
"""
Import - インポート -
"""
import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import openpyxl

"""
Function - 関数 -
"""
#def Func_read():

"""
Class - クラス -
"""


"""
Main - メイン関数 -
"""
if __name__ == "__main__":
    #Func_read()    # File reading  # ファイル読み込み
    folder_path = 'D:/iriwa/デスクトップ/Code/Project_Python/'
    file_name = 'test_input'
    input_data = pd.read_table(folder_path + file_name + '.txt', \
                                header=None, skiprows=6, \
                                names=('time[s]','O1[V]','O2[V]'))
    print(input_data)
    output_data = []

    N  = 1024   # Sampling size # サンプリングサイズ(FFTサイズ)
    dt = 0.001  # Sampling period[s]        # サンプリング周期[s]
    fs = 1/dt   # Sampling rate[Hz]         # サンプリング周波数[Hz]

    #Func_filter()  # Filtering(bandpass)   # フィルタリング(バンドパス)
    filter1 = signal.firwin(numtaps=16, cutoff=[1,30], \
                            pass_zero=False, fs=1/dt)
    filter_data = []    # EEG filtered  # フィルタ適用データ

    wf = signal.hamming(N)  # Window functoin(hamming)  # 窓関数(ハミング窓)

    #Func_cutting() # Data cutting  # データ整形
    for n in range(2):
        filter_data = signal.lfilter(filter1, 1, input_data.iloc[:, n+1])   # Filtering(bandpass)   # フィルタリング(バンドパス)
        cut_data    = []    #cutting for FFT   # FFT用に整形されたデータ
        window_data = []    #apply window function # 窓関数適用データ
        time  = []
        MPF   = []
        alpha = []
        beta  = []
        theta = []
        delta = []

        for i in range(int(len(filter_data)/fs)):
            for j in range(N):
                cut_data.insert(j, filter_data[j+i*int(fs)])  # Formatted to 1s(1000+24data)  # 1秒(1000+24個)を切り取り

            #Func_window()  # Window function(hamming)  # 窓関数(ハミング)
            for k in range(N):
                window_data.insert(k, cut_data[k]*wf[k])    # Apply window function    # 窓関数適用

            #Func_FFT() #FFT    #高速フーリエ変換
            F = np.fft.fft(window_data)
            amplitude = np.abs(F/(N/2))   # Amplitude     # 振幅スペクトル
            power = amplitude ** 2        # Power         # パワースペクトル
            density = power/(1000/N)     # Power Density # パワースペクトル密度
            freq = np.fft.fftfreq(N, d=dt)

            #Func_cal
            sum_alpha = 0
            sum_beta = 0
            sum_theta = 0
            sum_delta = 0
            total_fp = 0
            total_power = 0

            for l in range(len(freq)):
                if freq[l] <= 30: 
                    total_power = total_power + density[l]
                    total_fp = total_fp + density[l] * freq[l]
                    if freq[l] >= 8.0 and freq[l] <= 13.0:
                        sum_alpha = sum_alpha + density[l]
                    if freq[l] >= 13.0 and freq[l] <= 30.0:
                        sum_beta = sum_beta + density[l]
                    if freq[l] >= 4.0 and freq[l] <= 8.0:
                        sum_theta = sum_theta + density[l]
                    if freq[l] >= 1.0 and freq[l] <= 4.0:
                        sum_delta = sum_delta + density[l]
            time.insert(i, i)
            MPF.insert(i, total_fp / total_power)
            alpha.insert(i, sum_alpha / total_power)
            beta.insert(i, sum_beta / total_power)
            theta.insert(i, sum_theta / total_power)
            delta.insert(i, sum_delta / total_power)
            print(i)
            
        output_data.append(MPF)
        output_data.append(alpha)
        output_data.append(beta)
        output_data.append(theta)
        output_data.append(delta)

    df = pd.DataFrame(output_data, index=['O1_MPF', 'O1_alpha', 'O1_beta', 'O1_theta', 'O1_delta',\
                                            'O2_MPF', 'O2_alpha', 'O2_beta', 'O2_theta', 'O2_delta']).T
    s = pd.Series(time, name='t[s]')
    output = pd.concat([s, df], axis=1)
    output.to_excel(folder_path + file_name+'_analyze.xlsx', index=False)
