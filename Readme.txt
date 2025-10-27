Setup Instructions for Using Google Sheets API
Prerequisites
Python 3.7 or higher must be installed.​

Required Python libraries: gspread, oauth2client, tkinter (standard library).​

Access to a Google account.

Obtaining API Credentials
Go to the Google Cloud Console.

Create a new project (or select an existing one).

Enable the Google Sheets API and Google Drive API for your project.​

In “APIs & Services”, open “Credentials” then click “Create Credentials” → “Service account”.​

Follow prompts to create a service account, then click your service account and go to “Keys”.

Add a new key: choose “JSON” and download the file.

Rename the downloaded file to credentials.json and place it in the root directory of your project (this file should not be pushed to GitHub and must be kept secret).​

Granting Access to Your Google Sheet
Open your target Google Sheet.

Under “Share”, add the Service Account’s email address found in the credentials.json file, and grant it “Editor” access.​

Installing Dependencies
Run the following command to install required packages:
pip install gspread oauth2client

Running the Project
Place your credentials.json file in your project directory.

Ensure the name of your Google Sheet matches what is set in the code (default: Student_data).

Run the script:
python passes.py