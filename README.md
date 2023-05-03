Disease-Prediction-Chatbot

The disease prediction chatbot is a Python-based project that utilizes machine learning algorithms to predict the disease based on the symptoms entered by the user. The model is trained on a dataset containing information about various diseases and their corresponding symptoms. The chatbot prompts the user to enter their symptoms, processes the input, and returns the predicted disease along with some general information about it.

The project begins by importing the necessary libraries and loading the dataset. After pre-processing the data, a decision tree classifier is trained on the data using scikit-learn. Once the model is trained, it is saved to a file for future use.

The chatbot is built using the Flask web framework, which provides a simple way to create a web application. The user enters their symptoms into a text box and submits the form. The input is then processed by the model, and the predicted disease is returned to the user along with some basic information about it. The chatbot also provides some general advice on what precautions to take in case the user is diagnosed with the disease.

Overall, the disease prediction chatbot is a useful tool for people who are concerned about their health and want to quickly get an idea of what disease they might have based on their symptoms.
