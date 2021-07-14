import tensorflow as tf
from tensorflow import keras
import  matplotlib.pyplot as plt
data = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = data.load_data()
y_train = tf.one_hot(y_train, depth=1)

# Flatten 将一个二维的数据拉伸成一个一维
# 第一个原因，神经元的数量太少，神经元的数量增加
# 第二个可能是因为欠拟合
# 第三个数据表示的方式可能有问题one-hot(只有0和1)
# 线性空间
# 0000 0000 01 -0
# 0000 0000 10 -1
# print(y_train)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128),
    keras.layers.Dense(32),
    keras.layers.Dense(10, activation='softmax')
])
optimizer = keras.optimizers.Adam(lr=0.001)
loss = keras.losses.sparse_categorical_crossentropy
model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, steps_per_epoch=32)
