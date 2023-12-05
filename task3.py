import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import ttk

# Corrected data
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 120.2, 8.6, 199.8, 66.1, 214.7, 23.8, 97.5, 204.1, 195.4, 67.8, 281.4, 69.2, 147.3, 218.4, 237.4, 13.2, 228.3, 62.3, 262.9, 142.9, 240.1, 248.8, 70.6, 292.9, 112.9, 97.2, 265.6, 95.7, 290.7, 266.9, 74.7, 43.1, 228.0, 202.5, 177.0, 293.6, 206.9, 25.1, 175.1, 89.7, 239.9, 227.2, 66.9, 199.8, 100.4, 216.4, 182.6, 262.7, 198.9, 7.3, 136.2, 210.8, 210.7, 53.5],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8, 48.9, 32.8, 19.6, 2.1, 2.6, 5.8, 24.0, 35.1, 7.6, 32.9, 47.7, 36.6, 39.6, 20.5, 23.9, 27.7, 5.1, 15.9, 16.9, 12.6, 3.5, 29.3, 16.7, 27.1, 16.0, 28.3, 17.4, 1.5, 20.0, 1.4, 4.1, 43.8, 49.4, 26.7, 37.7, 22.3, 33.4, 27.7, 8.4, 25.7, 22.5, 9.9, 41.5, 15.8, 11.7, 3.1, 9.6, 41.7, 46.2, 28.8, 49.4, 28.1, 19.2, 49.6, 29.5, 2.0],
    'Newspaper': [69.2, 45.1, 69.3, 58.5, 58.4, 75.0, 23.5, 11.6, 1.0, 21.2, 24.2, 4.0, 65.9, 7.2, 46.0, 52.9, 114.0, 55.8, 18.3, 19.1, 53.4, 23.5, 49.6, 26.2, 18.3, 19.5, 12.6, 22.9, 22.9, 40.8, 43.2, 38.6, 30.0, 0.3, 7.4, 8.5, 5.0, 45.7, 35.1, 32.0, 31.6, 38.7, 1.8, 26.4, 43.3, 31.5, 35.7, 18.5, 49.9, 36.8, 34.6, 3.6, 39.6, 58.7, 15.9, 60.0, 41.4, 16.6, 37.7, 9.3, 54.7, 27.3, 8.4, 28.9, 0.9, 2.2, 10.2, 11.0, 27.2, 38.7, 31.7, 19.3, 31.3, 13.1, 89.4, 20.7, 14.2, 9.4, 23.1, 22.3, 36.9, 32.5, 35.6, 33.8, 65.7, 16.0, 63.2, 73.4, 51.4, 9.3, 33.0, 59.0, 72.3, 10.9, 52.9, 5.9, 22.0, 17.9, 5.3],
    'Sales': [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 11.8, 13.2, 4.8, 10.6, 8.6, 17.4, 9.2, 9.7, 19.0, 22.4, 12.5, 24.4, 11.3, 14.6, 18.0, 12.5, 5.6, 15.5, 9.7, 12.0, 15.0, 15.9, 18.9, 10.5, 21.4, 11.9, 9.6, 17.4, 9.5, 12.8, 25.4, 14.7, 10.1, 21.5, 16.6, 17.1, 20.7, 12.9, 8.5, 14.9, 10.6, 23.2, 14.8, 9.7, 11.4, 10.7, 22.6, 21.2, 20.2, 23.7, 5.5, 13.2, 23.8, 18.4, 8.1, 24.2, 15.7, 14.0, 18.0, 19.2, 17.0, 15.2, 16.0, 16.7, 11.2, 7.3, 19.4, 22.2, 11.5, 16.9, 11.7, 15.5, 20.7, 19.2, 15.3, 10.1, 7.3, 15.9, 10.8, 9.5, 11.7, 15.6, 3.2, 15.3, 10.1, 7.3, 12.9, 13.4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Split the data into features (X) and target variable (y)
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# GUI for entering values and getting predictions
def predict_sales():
    try:
        tv_value = float(tv_entry.get())
        radio_value = float(radio_entry.get())
        newspaper_value = float(newspaper_entry.get())

        # Make a prediction
        prediction = model.predict([[tv_value, radio_value, newspaper_value]])

        # Update the result label
        result_label.config(text=f'Predicted Sales: {prediction[0]:.2f}')
    except ValueError:
        result_label.config(text='Please enter valid numeric values')

# Create a simple GUI
gui = tk.Tk()
gui.title('Sales Prediction')

# Create input labels and entry widgets
tv_label = ttk.Label(gui, text='TV:')
tv_label.grid(row=0, column=0, padx=10, pady=10)
tv_entry = ttk.Entry(gui)
tv_entry.grid(row=0, column=1, padx=10, pady=10)

radio_label = ttk.Label(gui, text='Radio:')
radio_label.grid(row=1, column=0, padx=10, pady=10)
radio_entry = ttk.Entry(gui)
radio_entry.grid(row=1, column=1, padx=10, pady=10)

newspaper_label = ttk.Label(gui, text='Newspaper:')
newspaper_label.grid(row=2, column=0, padx=10, pady=10)
newspaper_entry = ttk.Entry(gui)
newspaper_entry.grid(row=2, column=1, padx=10, pady=10)

predict_button = ttk.Button(gui, text='Predict Sales', command=predict_sales)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(gui, text='')
result_label.grid(row=4, column=0, columnspan=2, pady=10)

gui.mainloop()
