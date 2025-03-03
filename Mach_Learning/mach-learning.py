# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create a simple dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 4, 2, 5, 6])

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions using the trained model
predictions = model.predict(X)

# Visualize the results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, predictions, color='red', label='Predicted line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
