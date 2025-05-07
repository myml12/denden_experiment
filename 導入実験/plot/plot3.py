import matplotlib.pyplot as plt

# 日本語フォントを設定（macOS用）
plt.rcParams['font.family'] = 'Hiragino Sans'  # または 'AppleGothic', 'Osaka'

# IN1のデータ
freq_in1 = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
theoretical_in1 = [117, 235, 467, 694, 914, 1123, 1322, 1509, 1684, 1845, 1995, 2934, 3573, 3703, 3738, 3748, 3750, 3750, 3750, 3750, 3750]
measured_in1 = [160, 320, 480, 720, 960, 1120, 1360, 1440, 1600, 1760, 1920, 2720, 3280, 3440, 3520, 3520, 3520, 3750, 3600, 2960, 1800]

# IN2のデータ
freq_in2 = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
theoretical_in2 = [3750] * len(freq_in2)
measured_in2 = [4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 3200, 2000]

# IN1のグラフ
plt.figure(figsize=(10, 6))
plt.plot(freq_in1, theoretical_in1, label="理論値 (IN1)", marker='o')
plt.plot(freq_in1, measured_in1, label="実測値 (IN1)", marker='x')
plt.xscale('log')
plt.xlabel("周波数 [Hz]")
plt.ylabel("出力電圧 [mVpp]")
plt.title("IN1 の周波数特性")
plt.legend()
plt.grid(True)
plt.show()

# IN2のグラフ
plt.figure(figsize=(10, 6))
plt.plot(freq_in2, theoretical_in2, label="理論値 (IN2)", marker='o')
plt.plot(freq_in2, measured_in2, label="実測値 (IN2)", marker='x')
plt.xscale('log')
plt.xlabel("周波数 [Hz]")
plt.ylabel("出力電圧 [mVpp]")
plt.title("IN2 の周波数特性")
plt.legend()
plt.grid(True)
plt.show()
