from keras.datasets import boston_housing
from keras import  models, layers, optimizers
import numpy as np
import matplotlib.pyplot as plt

def smooth_curve(points, factor = 0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points

def build_models():
    model = models.Sequential()
    model.add(layers.Dense(256, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss = 'mse', metrics=['mae'])
    return  model

(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

mean = train_data.mean(axis=0)
std = train_data.std(axis = 0)
train_data -= mean
train_data /= std
test_data -=  mean
test_data /= std
k = 4
num_val_samples = len(train_data) // k
num_epochs = 80
print(num_epochs)
all_mae_histories = []
for i in range(k):
    print('processing fold №', i)
    val_data = train_data[i * num_val_samples : (i + 1) * num_val_samples]
    val_labels = train_labels[i * num_val_samples : (i + 1) * num_val_samples]

    partial_train_data = np.concatenate([train_data[ : i * num_val_samples], train_data[(i + 1) * num_val_samples : ]], axis = 0)
    partial_train_labels = np.concatenate([train_labels[ : i * num_val_samples], train_labels[(i + 1) * num_val_samples :]], axis = 0)
    model = build_models()
    history = model.fit(partial_train_data, partial_train_labels, validation_data=(val_data, val_labels), epochs = num_epochs, batch_size = 1, verbose = 0)
    mae_history = history.history['val_mae']
    all_mae_histories.append(mae_history)

average_mae_history = [np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]
smooth_mae_history = smooth_curve(average_mae_history[10 : ])
plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history)
plt.xlabel('Эпохи')
plt.ylabel('оценка МАЕ')
plt.show()
print(np.mean(all_mae_histories))
