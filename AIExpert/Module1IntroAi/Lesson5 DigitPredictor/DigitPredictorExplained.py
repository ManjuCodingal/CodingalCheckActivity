# Basic handwritten digit predictor using TensorFlow and Keras
import tensorflow as tf # import tensorflow library. It is a popular open-source library for machine learning and deep learning developed by Google. It provides tools and resources for building and training machine learning models, including neural networks, and is widely used in both research and industry for various applications such as image recognition, natural language processing, and more.
from tensorflow.keras import layers, models # imports the layers and models modules from the Keras, which is TensorFlow's high-level neural networks API for building neural networks.
# The layers module provides various types of layers (e.g., Dense, Flatten) that can be used to build neural network architectures, while the models module allows you to create and manage the overall structure of your neural network model.
import matplotlib.pyplot as plt # matplotlib is a library in Python for plotting graph and visualisations. Here its used to display the MNIST images and predictions. The pyplot module (imported as plt) provides a simple interface for creating static, and interactive visualizations in Python. It is commonly used for plotting data, creating charts, and displaying images in a graphical format.

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# This loads the MNIST dataset, which is a collection of 70,000 handwritten digit images (28x28 pixels) and their corresponding labels (0-9). The dataset is split into a training set (x_train, y_train) and a test set (x_test, y_test). The training set is used to train the model, while the test set is used to evaluate its performance. Each image in the dataset is represented as a 2D array of pixel values, and the labels indicate which digit each image represents.
# x_train (Training image) 
# x_test (Test image)
# y_train (label for training image) corresponds to x_train
# y_test (label for test image corresponds to x_test

# x_train (Training image) and x_test (Test image) contain the pixel data for the images, while y_train (label for training image) and y_test (label for test image) contain the corresponding labels for those images. The pixel values are typically in the range of 0 to 255, representing the intensity of each pixel (0 for black and 255 for white).

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0 # This line normalizes the pixel values of the images in both the training and test sets by dividing each pixel value by 255.0. Normalization is a common preprocessing step in machine learning that helps to scale the input data to a range of [0, 1].
# To scale values into a range of 0 to 1, the code divides each pixel value by 255.
# This ensures that neural network learns more efficiently since data is scaled to a consistent range, scale between 0 and 1.
# x_train and x_test are updated with the normalized pixel values, which can help improve the performance of the model during training and evaluation.

# Build the model. This code defines a simple feedforward neural network model using Keras' Sequential model.  
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
# layers.Flatten is used to convert the 2D input images (28x28 pixels) into a 1D array of 784 pixels (28*28=784), which can be fed into the dense layers.
# layers.Dense(128, activation='relu') adds a fully connected layer with 128 neurons. The activation function used is ReLU (Rectified Linear Unit), which introduces non-linearity to the model and helps it learn complex patterns in the data.
# layers.Dense(10, activation='softmax') adds another fully connected layer with 10 neurons, which corresponds to the 10 possible digit classes (0-9). The activation function used here is softmax, which converts the output into a probability distribution over the 10 classes, allowing the model to make predictions about which digit is most likely represented by the input image.

# Compile the model. This step configures the model for training by specifying the optimizer, loss function, and evaluation metrics.
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])
# optimizer='adam' (Adaptive Moment Estimation) specifies that the Adam optimization algorithm will be used to update the model's weights during training. Adam is an efficient optimization algorithm.
# loss='sparse_categorical_crossentropy' specifies the loss function to be used during training. Sparse categorical crossentropy is used when the labels are provided as integers (as in this case, where the labels are 0-9). It measures the difference between the predicted probability distribution and the true label, and the model will try to minimize this loss during training.
# metrics=['accuracy'] specifies that the accuracy metric will be calculated and displayed during training and evaluation

# Train the model
model.fit(x_train, y_train, epochs=5)
# Train the model on training data (x_train and y_train) for 5 epochs. An epoch is one complete pass through the entire training dataset. During each epoch, the model will update its weights based on the loss calculated from the training data, and it will also compute the accuracy metric to monitor how well the model is learning over time.

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")
# Evaluates trained models performance on the test dataset (x_test and y_test). The evaluate method returns the loss value and the accuracy metric for the test data. The test accuracy is printed to the console, which indicates how well the model generalizes to unseen data.

# Make predictions
predictions = model.predict(x_test)
# Generates predictions for the test dataset (x_test) using the trained model. The predict method returns an array of predicted probabilities for each class (0-9) for each test image. Each element in the predictions array corresponds to a test image and contains the predicted probabilities.

# Display the first image and prediction
plt.imshow(x_test[0], cmap=plt.cm.binary) # This always shows the first test image.
# If the first image is 7 → it predicts 7.

# Displays the first image from the test dataset (x_test[0]) using Matplotlib's imshow function. The cmap=plt.cm.binary argument specifies that the image should be displayed in a binary color map (black and white), which is appropriate for the grayscale images in the MNIST dataset.
plt.title(f"Predicted: {predictions[0].argmax()}")
# Sets the title of the plot to show the predicted digit for the first test image. The predictions[0] contains the predicted probabilities for each class (0-9) for the first test image, and argmax() is used to find the index of the class with the highest predicted probability, which corresponds to the predicted digit.
plt.show() # Displays the plot with the first test image and its predicted label. This allows you to visually verify the model's prediction for that specific image.

# Overall, this code builds and trains a simple neural network to recognize handwritten digits from the MNIST dataset, evaluates its performance, and visualizes the prediction for the first test image.
 
# It predicts 7 because:
# plt.imshow(x_test[0])
# The first image in the MNIST test dataset (x_test[0]) is actually a handwritten 7.
# So model predicts 7 because the model has learned to recognize patterns in the training data and has identified the features of the first test image as corresponding to the digit 7. The model's prediction is based on the learned weights and patterns from the training data, which allows it to make an informed guess about the digit represented in the test image.