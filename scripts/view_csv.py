# view_csv.py -> csvのデータを表示するプログラム
# 参考: https://qiita.com/oizumi-yuta/items/a9fbef038887b2a95bf1

import matplotlib.pyplot as plt
# CSVデータの読み込みライブラリ
import pandas as pd

# CSVファイルの読み込み
input_csv = pd.read_csv('~/matplotlib_ws/data/vcgencmd_output.csv')

# Timestamp列の年月日部分を変更し、時間も含めてフォーマット
input_csv['Timestamp'] = pd.to_datetime(input_csv['Timestamp'])

# Timestamp列のデータを取得
timestamp_data = input_csv['Timestamp']

# Temperature列のデータを取得
temperature_data = input_csv['Temperature']

# グラフのx軸ラベルを設定
plt.xlabel('Timestamp')
# グラフのy軸ラベルを設定
plt.ylabel('Temperature')

# データの期間を取得
start_date = timestamp_data.min().strftime('%Y-%m-%d')
end_date = timestamp_data.max().strftime('%Y-%m-%d')

# グラフのタイトルを設定
plt.title(f'Temperature Data from {start_date} to {end_date}')

# 折れ線グラフをプロット（点と線のスタイルを設定）
plt.plot(timestamp_data.dt.strftime('%H:%M:%S'), temperature_data, linestyle='solid', marker='o')

# グラフを表示
plt.show()
