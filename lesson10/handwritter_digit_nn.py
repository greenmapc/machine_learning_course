import tensorflow as tf

# библиотека с тренировочнымми и тестовыми данными
mnist = tf.keras.datasets.mnist
# # *_train - тренировочные данные
# # *_test - тестовые данные
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# нормализация данных в диапазоне [0;1]
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# создаем модель - которая является стеком слоёв (Sequential)
model = tf.keras.models.Sequential()
# аналог reshape
model.add(tf.keras.layers.Flatten())

# добавляем в модель два слоя - hidden слой и один выходной

# первый hidden слой
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

# тестовый второй hidden слой (был исключен имперически)
# второй hidden слой
# model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

# выходной слой (10 возможных значений)
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# конфигурация функции обучения
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# тренировка модели на тренировочных данных
# выбрано 5 эпох
model.fit(x=x_train, y=y_train, epochs=5)
model.save('mnist.h5')

# с помощью тестовых данных, определяем точность обучения
test_loss, test_accuracy = model.evaluate(x=x_test, y=y_test)
print('\n')
print('Accuracy for test data:', test_accuracy)
