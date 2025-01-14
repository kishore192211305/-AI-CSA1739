# Import the necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Sample data (XOR problem)
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Define a feedforward neural network model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(2, 4)  # Input layer with 2 features and a hidden layer with 4 neurons
        self.fc2 = nn.Linear(4, 1)  # Output layer with 1 neuron

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

model = NeuralNetwork()

# Define loss function and optimizer
criterion = nn.BCELoss()  # Binary Cross Entropy loss
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Training loop
for epoch in range(1000):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backpropagation and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Make predictions
predictions = (model(X) > 0.5).float()
print(predictions)
