import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォントを設定（macOS用）
plt.rcParams['font.family'] = 'Hiragino Sans'  # または 'AppleGothic', 'Osaka'

# IN1 のデータ
in1_input_theoretical = [400, 500, 600, 700, 800, 900, 1000]
in1_output_calculated = [x * 2.24 for x in in1_input_theoretical]
print("IN1")
print(in1_output_calculated)
in1_input_measured = [408, 500, 600, 700, 800, 920, 1060]
in1_output_measured = [900, 1120, 1320, 1600, 1920, 2160, 2480]

# IN2 のデータ
in2_input_theoretical = [400, 500, 600, 700, 800, 900, 1000]
in2_output_calculated = [x * 7.5 for x in in2_input_theoretical]
print("IN2")
print(in2_output_calculated)
in2_input_measured = [404, 504, 604, 704, 800, 900, 1020]
in2_output_measured = [2860, 3640, 4380, 5080, 5920, 6640, 7460]

# IN1 グラフ
plt.figure(figsize=(7, 6))
plt.plot(in1_input_theoretical, in1_output_calculated, 'o-', label='出力電圧 (計算値)')
plt.plot(in1_input_measured, in1_output_measured, 's--', label='出力電圧 (実測値)')
plt.title('IN1 の電圧特性')
plt.xlabel('入力電圧 [mVpp]')
plt.ylabel('出力電圧 [mVpp]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# IN2 グラフ
plt.figure(figsize=(7, 6))
plt.plot(in2_input_theoretical, in2_output_calculated, 'o-', label='出力電圧 (計算値)')
plt.plot(in2_input_measured, in2_output_measured, 's--', label='出力電圧 (実測値)')
plt.title('IN2 の電圧特性')
plt.xlabel('入力電圧 [mVpp]')
plt.ylabel('出力電圧 [mVpp]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
