# -*- coding: utf-8 -*-
"""
    EEG_analyzer.py
        For the study
        EEG spectrum analysis program
        input  : EEG data by Labchart (.txt)
        output : MPF / α / β / θ / δ (.csv)

        研究用
        脳波スペクトル解析プログラム
        読込：Labchartデータをtxtデータに変換したデータ
        出力：MPF，α・β・θ・δ波比率データをcsvデータに出力
        処理速度優先のため読みにくいかも
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


"""
Class - クラス -
"""


"""
Main - メイン関数 -
"""
if __name__ == "__main__":
    #Func_read()    # File reading  # ファイル読み込み
    folder_path = 'D:/iriwa/デスクトップ/進捗/長時間実験/'
    file_name = 'tanaka'

    input_data = pd.read_table(folder_path + file_name + '.txt', \
                                header=None, skiprows=6, \
                                names=('time[s]','O1[V]','O2[V]'))
    input_data = input_data.interpolate()   # 欠損値補間
    print(input_data)

    output_data = []
   
    N  = 1024   # Sampling size # サンプリングサイズ(FFTサイズ)
    dt = 0.001  # Sampling period[s]        # サンプリング周期[s]
    fs = 1/dt   # Sampling rate[Hz]         # サンプリング周波数[Hz]
    TIME = int(len(input_data)/fs)  # Data time[s]  #データ時間[s]
    print('%d秒分のデータ'%TIME)
    time = [i for i in range(TIME)] #　Time axis    # 時間軸

    #Func_filter()  # Filtering(bandpass)   # フィルタリング(バンドパス)
    filter1 = signal.firwin(numtaps=16, cutoff=[1,30], \
                            pass_zero=False, fs=1/dt)
    #filter_data = []    # EEG filtered  # フィルタ適用データ

    wf = signal.hamming(N)  # Window functoin(hamming)  # 窓関数(ハミング窓)



    #Func_cutting(TIME) # Data cutting  # データ整形
    for n in range(2):
        filter_data = signal.lfilter(filter1, 1, input_data.iloc[:, n+1])   # Filtering(bandpass)   # フィルタリング(バンドパス)
        # cut_data    = []    #cutting for FFT   # FFT用に整形されたデータ
        # window_data = []    #apply window function # 窓関数適用データ
       
        MPF   = [np.nan for i in range(TIME)]
        alpha = [np.nan for i in range(TIME)]
        beta  = [np.nan for i in range(TIME)]
        theta = [np.nan for i in range(TIME)]
        delta = [np.nan for i in range(TIME)]

        for i in range(TIME):
            # Formatted to 1s(1000+24data) & Apply window function  # 1秒(1000+24個)を切り取り & 窓関数適用
            Format_data = [filter_data[j+i*int(fs)] * wf[j] for j in range(N)]  # Formatted to 1s(1000+24data)  # 1秒(1000+24個)を切り取り

            #Func_FFT() #FFT    #高速フーリエ変換
            F = np.fft.fft(Format_data)
            amplitude = np.abs(F)   # Amplitude     # 振幅スペクトル(F/N/2)
            power = amplitude ** 2        # Power         # パワースペクトル
            density = power/(fs/N)     # Power Density # パワースペクトル密度
            freq = np.fft.fftfreq(N, d=dt)
            f_l = int(len(freq)/2)
            
            #Func_cal
            sum_alpha = 0
            sum_beta = 0
            sum_theta = 0
            sum_delta = 0
            total_fp = 0
            total_power = 0

            for l in range(f_l):
                if freq[l] >= 1.0 and freq[l] <= 30: 
                    total_power += amplitude[l]
                    total_fp = total_fp + (amplitude[l] * freq[l])
                    if freq[l] >= 1.0  and freq[l] <= 4.0:
                        sum_delta += amplitude[l]
                    if freq[l] >= 4.0  and freq[l] <= 8.0:
                        sum_theta += amplitude[l]
                    if freq[l] >= 8.0  and freq[l] <= 13.0:
                        sum_alpha += amplitude[l]
                    if freq[l] >= 13.0 and freq[l] <= 30.0:
                        sum_beta  += amplitude[l]

            MPF[i]   = total_fp  / total_power
            alpha[i] = sum_alpha / total_power 
            beta[i]  = sum_beta  / total_power
            theta[i] = sum_theta / total_power
            delta[i] = sum_delta / total_power
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