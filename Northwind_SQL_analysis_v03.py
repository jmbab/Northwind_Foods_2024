# NORTHWIND EXERCISE v3
# GOAL: USE DATABASE WITH MYSQL CONNECTOR, ANALYSE DATA WITH PANDAS,
# VISUALIZE DATA WITH MATHPLOTLIB AS BAR CHARTS.
# INCLUDE USER FRIENDLY DIALOG BOX: SAVE GRAPH? ANOTHER SQL QUERY?
# EXAMPLE: perform an analysis to find the sales for each country.
# 25-10-2024 | Jean M. Babonneau


import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.font import Font

# MySQL connection configuration 
# (another option would be a script to read an external JSON file 
# with connection credentials: username + pass + host + database)
config = {
    'user': 'root',        # Replace with your MySQL username
    'password': 'Velkommen24',    # Replace with your MySQL password
    'host': 'localhost',            # Host where MySQL server is running
    'database': 'northwind'         # Database name
}

def connect_to_database():
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print("Successfully connected to the MySQL database.")
            return conn
    except Error as e:
        messagebox.showerror("Connection Error", f"Error connecting to MySQL: {e}")
    return None

def run_query(query, conn):
    try:
        data = pd.read_sql(query, conn)
        print("Data successfully retrieved from the database.")
        return data
    except pd.io.sql.DatabaseError as e:
        messagebox.showerror("Database Error", f"Database error during SQL query execution: {e}")
    except Error as e:
        messagebox.showerror("SQL Execution Error", f"MySQL error during SQL query execution: {e}")
    return None

def plot_data(data):
    try:
        # Set the first column as the index for plotting, assuming it's a label like 'ShipCountry'
        data.set_index(data.columns[0], inplace=True)

        # Plot the data as a bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        data.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title('Data Visualization')
        ax.set_xlabel(data.index.name)
        ax.set_ylabel('Values')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Display the plot
        plt.show()

        # Show save dialog after the graph window is closed
        save_graph(fig)

    except Exception as e:
        messagebox.showerror("Visualization Error", f"Unexpected error during visualization: {e}")

def save_graph(fig):
    answer = messagebox.askyesno("Save Graph", "Would you like to save this graph?")
    if answer:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            fig.savefig(save_path)
            messagebox.showinfo("File Saved", f"Graph saved successfully at {save_path}")

def main():
    # Set up tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window, only use dialogs

    # Connect to the database
    conn = connect_to_database()
    if not conn:
        return

    try:
        # Initial query
        query = '''
            SELECT o.ShipCountry, SUM(od.Quantity * od.UnitPrice) AS TotalSales
            FROM Orders o
            JOIN OrderDetails od ON o.OrderID = od.OrderID
            GROUP BY o.ShipCountry;
        '''
        data = run_query(query, conn)
        if data is not None:
            plot_data(data)

        while True:
            # Ask user if they want to enter a new query
            ask_new_query = messagebox.askyesno("New Query", "Would you like to enter a new SQL query?")
            if not ask_new_query:
                break  # Exit if user chooses "No"

            # Display dialog to enter a new SQL query with a larger multi-line input box
            new_query = open_multiline_input_dialog(root)
            if new_query:
                # Execute new query and plot data if valid
                data = run_query(new_query, conn)
                if data is not None:
                    plot_data(data)
            else:
                messagebox.showwarning("Input Required", "SQL query cannot be empty.")

    finally:
        # Close the database connection when done
        if conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

def open_multiline_input_dialog(root):
    """
    Opens a larger dialog box with a 5-line Text widget for multiline input
    and returns the entered SQL query.
    """
    dialog = tk.Toplevel(root)
    dialog.title("Enter SQL Query")
    
    # Label
    tk.Label(dialog, text="Please enter a new SQL query:").pack(pady=5)
    
    # Text input field
    # Set larger font for better readability
    font = Font(family="Helvetica", size=12)
    query_text = tk.Text(dialog, height=5, width=60, font=font)
    query_text.pack(padx=10, pady=10)

    # Variable to store the query and close the dialog
    query = tk.StringVar()

    def submit_query():
        query.set(query_text.get("1.0", "end-1c"))
        dialog.destroy()

    # Submit button
    tk.Button(dialog, text="Submit", command=submit_query).pack(pady=5)
    
    # Wait for the dialog to be closed before continuing
    dialog.grab_set()
    root.wait_window(dialog)
    
    return query.get()

if __name__ == "__main__":
    main()