import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)

# Display the first image and prediction

# For image as 7, the 1st test image
# plt.imshow(x_test[0], cmap=plt.cm.binary)
# plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()

# For image as 4: replace index 0 (ie 7) with an image that is 4.
index = list(y_test).index(4)

plt.imshow(x_test[index], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[index].argmax()}")
plt.show()

# For image as 5, give index with an image that is 5.
# index = list(y_test).index(5)

# prediction = model.predict(x_test[index].reshape(1, 28, 28))

# plt.imshow(x_test[index], cmap=plt.cm.binary)
# plt.title(f"Predicted: {prediction.argmax()}  |  Actual: {y_test[index]}")
# plt.show()

