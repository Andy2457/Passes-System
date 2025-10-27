Student Data Verification with Google Sheets API
A simple Python/Tkinter app for verifying student IDs and managing check-ins using Google Sheets as the backend.

Table of Contents
About
Setup Instructions
Obtaining API Credentials
Granting Access to Sheets
Installing Dependencies
Running the Project
Security
License
Contact


About
This project allows users to scan or input student IDs, verify them against a main Google Sheet, and store check-in/check-out information in another sheet tab. Designed to streamline attendance and data management using Python and Google Sheets API.


Setup Instructions
Prerequisites
Python 3.7 or higher.
Libraries: gspread, oauth2client, and built-in tkinter.
Access to a Google account.


Obtaining API Credentials
Go to Google Cloud Console.
Create/select your project.
Enable Google Sheets API and Google Drive API.
Under “APIs & Services”, go to “Credentials” → “Create Credentials” → “Service account”.
Create a service account, then go to “Keys” → “Add Key” → choose JSON.
Download and rename this file to credentials.json.
Important: Place the file in your project root, but never upload it to GitHub.

Granting Access to Sheets
Open your Google Sheet.
Click “Share” and add the service account’s email (from credentials.json) with Editor access.


Installing Dependencies
pip install gspread oauth2client


Running the Project
Place your credentials.json in the project directory.
Make sure your Google Sheet is named "Student_data" (or update the name in your script).
Run the script:
python passes.py


Contact
For questions or feature requests, feel free to open an issue or contact Aniket via aniketpawar2457@gmail.com.