import tensorflow as tf


def create_conv_net(input_shape=(32, 32, 3)):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=input_shape))
    model.add(tf.keras.layers.Conv2D(filters=10, kernel_size=8, strides=(1, 1), padding='valid'))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=10, activation=tf.keras.activations.softmax))
    return model


