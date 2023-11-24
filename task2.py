import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel

# Corrected data with the same length for all arrays
data = {
    "Region": ["Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
               "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya", "Odisha",
               "Puducherry", "Punjab"],
    "Date": ["31-01-2020", "29-02-2020", "31-03-2020", "30-04-2020", "31-05-2020", "30-06-2020", "31-07-2020", "31-08-2020",
             "30-09-2020", "31-10-2020", "30-11-2020", "31-12-2020", "31-01-2021", "28-02-2021", "31-03-2021", "30-04-2021",
             "31-05-2021", "30-06-2021", "31-07-2021"],
    "Frequency": ["M"] * 19,
    "Estimated Unemployment Rate (%)": [5.48, 5.83, 5.79, 20.51, 17.43, 3.31, 8.34, 6.96, 6.4, 6.59, 5.8, 5.1, 4.8, 4.5, 4.2, 4.0, 3.8, 3.6, 3.4],
    "Estimated Employed": [16635535, 16545652, 15881197, 11336911, 12988845, 19805400, 15431615, 15251776, 15220312, 15157557,
                           15784327, 15987245, 16234109, 16478851, 16721542, 16962263, 17201018, 17437826, 17672716],
    "Estimated Labour Participation Rate (%)": [41.02, 40.9, 39.18, 33.1, 36.46, 47.41, 38.91, 37.83, 37.47, 37.34, 38.2, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0],
    "Region_longitude": [15.9129, 26.2006, 25.0961, 21.2787, 28.7041, 15.2993, 22.2587, 29.0588, 31.1048, 33.7782,
                         23.6102, 15.3173, 10.8505, 22.9734, 19.7515, 25.467, 20.9517, 11.9416, 31.1471],
    "Region_latitude": [79.74, 92.9376, 85.3131, 81.8661, 77.1025, 74.124, 71.1924, 76.0856, 77.1734, 76.5762,
                        85.2799, 75.7139, 76.2711, 78.6569, 75.7139, 91.3662, 85.0985, 79.8083, 75.3412]
}

df = pd.DataFrame(data)

# Create the GUI
class UnemploymentApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Unemployment Data")

        # Create a Treeview widget
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = tuple(df.columns)
        self.tree["show"] = "headings"

        # Add columns to the Treeview
        for column in df.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor="center", width=100)

        # Insert data into the Treeview
        for i in range(len(df)):
            self.tree.insert("", i, values=tuple(df.iloc[i]))

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Place components on the grid
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Adjust column weights so they expand proportionally
        for i in range(len(df.columns)):
            root.grid_columnconfigure(i, weight=1)

        # Create a PandasTable for detailed view
        self.create_pandas_table()

    def create_pandas_table(self):
        try:
            self.table = Table(self.root, dataframe=df, showtoolbar=True, showstatusbar=True)
            self.table.show()
        except AttributeError as e:
            print(f"Error creating PandasTable: {e}")

# Run the GUI
if _name_ == "_main_":
    root = tk.Tk()
    app = UnemploymentApp(root)
    root.mainloop()
