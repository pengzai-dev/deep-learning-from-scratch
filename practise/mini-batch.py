# 小批量
# 读取小批量数据
from dataset.mnist import load_mnist
import numpy as np
import sys
import os
sys.path.append("..")  # 親ディレクトリのファイルをインポートするための設定
# 读取数据
(x_train, t_train), (x_test, t_test) = load_mnist(
    normalize=True, one_hot_label=False)
print(x_train.shape)  # (60000, 784)
print(t_train.shape)  # (60000, 10)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)  # 从60000个数据中随机选10个
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
print(x_batch.shape)  # (10, 784)
print(t_batch.shape)  # (10, 10)

print(t_train[0])
y = np.array([[0.1, 0, 0.1, 0.2, 0.1, 0.5, 0, 0, 0, 0], [
             0.1, 0, 0.1, 0.2, 0.1, 0.1, 0.5, 0, 0, 0]])
print(np.arange(2))
print(t_train[0:2])
print(y[np.arange(2), np.array([5, 6])])
