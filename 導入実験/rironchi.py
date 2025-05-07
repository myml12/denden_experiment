import numpy as np
import pandas as pd

# 定数定義
R3 = 1e3       # 1kΩ
R4 = 10000      # ここに配られた抵抗値
C = 1e-6       # 1μF
voltage = 1  # ここに電流値を入れる

# 周波数リスト（Hz）
frequencies = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
               200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]

# 結果を格納するリスト
results = []

# 各周波数に対して計算
for f in frequencies:
    impedance = np.sqrt(R3**2 + (1 / (2 * np.pi * f * C))**2)
    result = R4 / impedance
    result *= voltage
    results.append({"Frequency (Hz)": f, "Result": result*1000})

# データフレームとして表示
df = pd.DataFrame(results)
print(df.to_string(index=False))
