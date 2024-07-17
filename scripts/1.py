# 1.py -> -5から5の範囲を0.1刻みづつのsin波をグラフ
# 参考: https://aiacademy.jp/media/?p=154

import numpy as np
import matplotlib.pyplot as plt

#-5から5まで0.1区切りで配列を作る
x = np.arange(-5, 5, 0.1)

#配列xの値に関してそれぞれsin(x)を求めてy軸の配列を生成
y = np.sin(x)

# データのプロット
# この場合のplot関数の第一引数xがx軸に対応、第二引数のyがy軸に対応。
plt.plot(x,y)

# 表示
plt.show()