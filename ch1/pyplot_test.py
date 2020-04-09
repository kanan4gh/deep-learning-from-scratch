# Akiko Ishihara

import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
y1 = np.sin(x)
y2 = np.cos(x)

# グラフの描画
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")
plt.xlabel("x") # x軸ラベル
plt.ylabel("y") # y軸ラベル
plt.title('sin & cos') # タイトル
plt.legend()
plt.show()
