from flask import Flask, request, render_template
import numpy as np
import pickle
import matplotlib.pyplot as plt
import io
import base64
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# Load the trained LSTM model and the saved scaler
model = load_model('lstm_main_model.h5')  # Path to your saved LSTM model
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract the stock prices for the last 12 days from the form
    form_values = request.form
    last_12_days = [float(form_values[f'day_{i}']) for i in range(1, 13)]

    # Convert the input features to a numpy array
    input_features = np.array(last_12_days).reshape(1, 12, 1)

    # Scale the features using the loaded scaler
    scaled_features = scaler.transform(input_features.reshape(-1, 1)).reshape(1, 12, 1)

    # Initialize a list to store the predictions
    predicted_prices = []

    # Generate predictions for the next 12 days
    for _ in range(12):
        # Predict the next day's price
        prediction = model.predict(scaled_features)
        # Inverse transform to get the actual predicted price
        next_day_price = scaler.inverse_transform(prediction).flatten()[0]
        predicted_prices.append(next_day_price)

        # Update the input features to include this prediction and remove the oldest day
        last_12_days.append(next_day_price)
        last_12_days.pop(0)
        scaled_features = scaler.transform(np.array(last_12_days).reshape(-1, 1)).reshape(1, 12, 1)

    # Prepare the output as a list of predicted prices, rounded for clarity
    output = [round(price, 2) for price in predicted_prices]

    # Create a combined dataset of the last 12 days + predicted next 12 days for plotting
    days = np.arange(1, 25)  # Total of 24 days (12 past, 12 future)
    last_12_days_copy = np.array([float(form_values[f'day_{i}']) for i in range(1, 13)])
    full_data = np.concatenate((last_12_days_copy, predicted_prices))  # Ensure the dimensions match

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(days[:12], last_12_days_copy, label='Last 12 Days Prices', color='blue')
    plt.plot(days[12:], predicted_prices, label='Next 12 Days Prediction', color='red', linestyle='--')
    plt.xlabel('Day')
    plt.ylabel('Stock Price')
    plt.title('Stock Price Prediction (Next 12 Days)')
    plt.legend()

    # Save the plot to a string in memory (to avoid saving a file)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # Render the prediction and chart in the front-end
    return render_template('index.html', prediction_text='Predicted prices for the next 12 days: {}'.format(output), plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
