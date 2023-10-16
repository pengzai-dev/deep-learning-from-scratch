import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from loosefunctions import mean_squared_error, cross_entropy_error

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0,0.05,0.1,0,0.1,0,0]
# print("均方误差：")
# print(mean_squared_error(np.array(y),np.array(t)))

# print("交叉熵误差：")
# print(cross_entropy_error(np.array(y),np.array(t)))

# print(np.arange(10))