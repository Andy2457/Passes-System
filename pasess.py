import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tkinter as tk
from tkinter import messagebox

# Set up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your main Google Sheet (e.g., Student_data)
main_sheet = client.open("Student_data").sheet1  # The first sheet for ID validation

# Open a second Google Sheet (within the same document) for storing checked IDs
checked_sheet = client.open("Student_data").worksheet("checked_strings")  # Sheet to store checked strings

# Initialize global variable for serial number
serial_number = None

def is_string_already_checked(input_string):
    try:
        # Fetch all checked strings from the "checked_strings" sheet
        checked_strings = checked_sheet.col_values(2)  # Second column for checked admission numbers
        return input_string in checked_strings
    except Exception as e:
        print(f"Error checking string: {str(e)}")

        return False

def save_checked_string(input_string, serial_number, name):
    try:
        # Append the serial number, checked string (admission number), and name to the "checked_strings" sheet
        checked_sheet.append_row([serial_number, input_string, name])  # Save serial number, ID, and name
        print(f"ID saved: {input_string} with Serial No: {serial_number} and Name: {name}")
    except Exception as e:
        print(f"Error saving checked string: {str(e)}")

def check_string_exists(input_string):
    try:
        # Fetch all records (rows) from the main Google Sheet (Student_data)
        records = main_sheet.get_all_records()
        for record in records:
            if input_string == str(record['ID_no.']).upper():
                name = record['Name']  # Get the name associated with the ID number
                global serial_number
                save_checked_string(input_string, serial_number, name)  # Save ID, serial number, and name
                serial_number += 1  # Auto increment serial number for the next entry
                serial_entry.delete(0, tk.END)  # Clear the serial number entry
                serial_entry.insert(0, str(serial_number))  # Update it with the new incremented value
                return f"The ID no. '{input_string}' is present in the Google Sheet.\n\nName: {name}\nRow Data: {record}"
        return f"The ID no. '{input_string}' is not present in the Google Sheet."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def on_submit(event=None):
    input_string = entry.get().upper()
    serial_input = serial_entry.get()

    if input_string and serial_input.isdigit():
        if is_string_already_checked(input_string):
            messagebox.showwarning("Duplicate Entry", f"The string '{input_string}' has already been checked.")
        else:
            global serial_number
            serial_number = int(serial_input) if serial_number is None else serial_number  # Set initial serial number
            result = check_string_exists(input_string)
            result_label.config(text=result, fg="black")
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Input Error", "Please enter a valid string and serial number.")

# Tkinter GUI setup
app = tk.Tk()
app.title("Entry Verification")
app.geometry("600x500")

# Admission number label and entry
label = tk.Label(app, text="Scan/Enter the ID no. to check:")
label.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=10)
entry.bind('<Return>', on_submit)  # Bind Enter key to trigger the submit action

# Serial number label and entry
serial_label = tk.Label(app, text="Enter Serial Number:")
serial_label.pack(pady=10)

serial_entry = tk.Entry(app, width=40)
serial_entry.pack(pady=10)
serial_entry.bind('<Return>', on_submit)  # Bind Enter key to trigger the submit action

# Submit button
submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Result label to show the results
result_label = tk.Label(app, text="", wraplength=350, justify="left")
result_label.pack(pady=10)

# Run the Tkinter application
app.mainloop()
