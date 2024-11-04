
---

# Stock Price Prediction App 📈


![image](https://github.com/user-attachments/assets/f37d0cac-3b51-4f78-b9c0-71f6751bd028)


This Flask-based web application uses a trained LSTM model to predict stock prices for the next 12 days based on the previous 12 days' prices. Users can input stock prices for the last 12 days, and the app will forecast the next 12 days and display a visual representation of the predictions.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

---

## Demo
![Stock Price Prediction Demo](https://github.com/user-attachments/assets/022efa24-9291-46fd-9eef-cfbf8f2c0842)


## App prediction:

![image](https://github.com/user-attachments/assets/1c3981da-df1e-43b2-b03e-8587e7ff138d)



## Features
- Predict stock prices for the next 12 days using past data.
- Visualize predictions with an interactive plot.
- User-friendly and engaging front-end for an enhanced user experience.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/stock-price-prediction.git
    cd stock-price-prediction
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Add the model and scaler files:**
   - Ensure that `lstm_main_model.h5` and `scaler.pkl` are placed in the root directory. These files contain the trained LSTM model and the scaler object used for preprocessing input data.

5. **Run the application:**
    ```bash
    flask run
    ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. Open the app in your browser.
2. Enter the stock prices for the last 12 days in the input fields.
3. Click on the "Predict" button to generate predictions.
4. View the predicted stock prices and the interactive plot.

## File Structure

```
.
├── app.py                    # Main application file
├── lstm_main_model.h5        # Trained LSTM model file
├── scaler.pkl                # MinMaxScaler file for input scaling
├── templates
│   └── index.html            # Front-end HTML template
├── requirements.txt          # List of dependencies
└── README.md                 # Project README file
```

## Technologies Used
- **Flask**: For building the web framework.
- **Keras & TensorFlow**: For loading the trained LSTM model.
- **scikit-learn**: For data preprocessing and scaling.
- **Matplotlib**: For plotting and visualizing predictions.
- **Bootstrap**: For responsive and interactive front-end design.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contributing
Feel free to submit a pull request if you want to improve this project. Please ensure your contributions align with the project’s goal.

---

This README should provide a comprehensive overview for anyone interested in running, contributing to, or learning from your stock price prediction app!
