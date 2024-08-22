import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

# Environment variable set by GitHub Actions workflow
service_account_file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Google Sheet details
SAMPLE_SPREADSHEET_ID_input = '17XAB3XE2ibM2D-oxmSH0VSGh0FoAx9iQ3RlrZDJlRtk'
SAMPLE_RANGE_NAME = 'SampleHour!A1'  # Update the cell reference as needed

def update_sheet():
    # Authenticate with the service account
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )

    # Build the service
    service = build('sheets', 'v4', credentials=credentials)

    # Get the current date and time
    now = datetime.now()  # Current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # Specify the data to write
    values = [
        [date_time]  # Writes the current date and time to the first cell
    ]
    body = {
        'values': values
    }
    # Call the Sheets API to update the cell
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
        range=SAMPLE_RANGE_NAME,
        valueInputOption='USER_ENTERED',
        body=body
    ).execute()

    print(f"Updated {result.get('updatedCells')} cells.")

if __name__ == '__main__':
    update_sheet()