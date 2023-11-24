import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def load_and_preprocess_data():
    # Load the dataset
    url = "D:\myyyy.csv"
    iris_df = pd.read_csv(url)

    # Encode the categorical labels
    le = LabelEncoder()
    iris_df['Species'] = le.fit_transform(iris_df['Species'])

    # Split the data into features (X) and target (y)
    X = iris_df.drop('Species', axis=1)
    y = iris_df['Species']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def train_and_evaluate_model(X_train, X_test, y_train, y_test, k_neighbors=3):
    # Train the k-nearest neighbors model
    knn_model = KNeighborsClassifier(n_neighbors=k_neighbors)
    knn_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn_model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy, classification_report(y_test, y_pred), confusion_matrix(y_test, y_pred)

def on_classify_button_click():
    try:
        k_neighbors = int(neighbor_entry.get())
        X_train, X_test, y_train, y_test = load_and_preprocess_data()
        accuracy, report, confusion = train_and_evaluate_model(X_train, X_test, y_train, y_test, k_neighbors)

        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Accuracy: {accuracy:.2f}\n\n")
        result_text.insert(tk.END, "Classification Report:\n")
        result_text.insert(tk.END, f"{report}\n")
        result_text.insert(tk.END, "Confusion Matrix:\n")
        result_text.insert(tk.END, f"{confusion}\n")
        result_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for k-neighbors.")

# Create the main window
root = tk.Tk()
root.title("Iris Flower Classification GUI")

# Create and place widgets
tk.Label(root, text="Enter the number of neighbors (k):").pack(pady=10)
neighbor_entry = ttk.Entry(root)
neighbor_entry.pack(pady=10)

classify_button = ttk.Button(root, text="Classify", command=on_classify_button_click)
classify_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=60, state=tk.DISABLED)
result_text.pack(pady=10)

# Run the GUI
root.mainloop()
