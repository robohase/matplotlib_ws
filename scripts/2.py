# 2.py ->　折れ線グラフの表示
# 参考: https://aiacademy.jp/media/?p=154

import matplotlib.pyplot as plt

data = [2, 4, 6, 3, 5, 8, 4, 5]

# データのプロット
plt.plot(data)

# 表示
plt.show()

# r--は赤の点線 b--は青の点線 g-- は緑の点線
plt.plot([1,2,3,4],[1,5,10,15],"r--") # 引数にオプションを渡さずに 色 に -- をつけると色 + 点線で表現できます
plt.show()