import tensorflow as tf


def create_conv_net(input_shape=(32, 32, 3)):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=input_shape))
    model.add(tf.keras.layers.Conv2D(filters=10, kernel_size=8, strides=(1, 1), padding='valid'))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=10, activation=tf.keras.activations.softmax))
    return model


def create_keras_example_1(input_shape=(32, 32, 3), num_classes=10):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=input_shape))
    model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation=tf.keras.layers.ReLU(), input_shape=input_shape))
    model.add(tf.keras.layers.Conv2D(32, (3, 3), activation=tf.keras.layers.ReLU()))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation=tf.keras.layers.ReLU()))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation=tf.keras.layers.ReLU()))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation=tf.keras.layers.ReLU()))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(num_classes, activation=tf.keras.activations.softmax))

    return model
