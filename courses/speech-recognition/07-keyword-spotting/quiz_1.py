import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras import layers, models

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)

train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(
    directory='dataset',
    batch_size=64,
    validation_split=0.3,
    seed=seed,
    output_sequence_length=16000,
    subset='both'
)

label = np.array(train_ds.class_names)
print(label)

def squeeze(audio, label):
    audio = tf.squeeze(audio, axis=-1)
    return audio, label

def get_spectogram(waveform):
    spectogram = tf.signal.stft(waveform, frame_length=255, frame_step=128)
    spectogram = tf.abs(spectogram)
    spectogram = spectogram[..., tf.newaxis]
    return spectogram

def make_spectogram_ds(ds):
    return ds.map(
        map_func=lambda audio, label: (get_spectogram(audio), label),
        num_parallel_calls=tf.data.AUTOTUNE
    )

train_ds = train_ds.map(squeeze, tf.data.AUTOTUNE)
val_ds = val_ds.map(squeeze, tf.data.AUTOTUNE)

test_ds = val_ds.shard(num_shards=2, index=0)
val_ds = val_ds.shard(num_shards=2, index=1)

train_spectogram_ds = make_spectogram_ds(train_ds)
val_spectogram_ds = make_spectogram_ds(val_ds)
test_spectogram_ds = make_spectogram_ds(test_ds)

for example_spectogram, example_spectogram_label, in train_spectogram_ds.take(1):
    break

input_shape = example_spectogram.shape[1:]
num_label = len(label)

norm_layer = layers.Normalization()
norm_layer.adapt(
    data=train_spectogram_ds.map(
        map_func=lambda spec, label:spec
    )
)

model = models.Sequential([
    layers.Input(shape=input_shape),
    layers.Resizing(32, 32),
    norm_layer,
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(128, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.5),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_label)
])

model.summary()

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

history = model.fit(
    train_spectogram_ds,
    validation_data=val_spectogram_ds,
    epochs=8,
    callbacks=tf.keras.callbacks.EarlyStopping(verbose=1, patience=2)
)

for i, (spectogram_batch, label_batch) in enumerate(test_spectogram_ds):
    prediction = model.predict(spectogram_batch)

    for j in range(len(label_batch)):
        true_index = label_batch[j].numpy()
        predicted_index = np.argmax(prediction[j])

        print(f'Batch {i}, Data {j}: Original Label -> {label[true_index]}, Prediction -> {label[predicted_index]}')

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epoch_range = range(len(acc))
plt.figure(figsize=(16, 9))
plt.plot(epoch_range, acc, label='Training Accuracy')
plt.plot(epoch_range, val_acc, label='Prediction Accuracy')
plt.title('Training and validation accuracy over epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()