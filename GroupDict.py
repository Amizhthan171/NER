from exchangelib import Account, Credentials, EWSDateTime
import pytz
from datetime import timedelta

# Set up credentials
credentials = Credentials(username='your_username', password='your_password')

# Connect to the account
account = Account(primary_smtp_address='your_email@example.com', credentials=credentials, autodiscover=True)

# Calculate the date range for the last 7 days
end_date = EWSDateTime.now(pytz.utc)
start_date = end_date - timedelta(days=7)

# Iterate through folders
for folder in account.inbox.walk():
    # Fetch emails within the specified date range
    emails = folder.all().filter(datetime_received__range=(start_date, end_date))
    
    # Iterate through filtered emails
    for item in emails:
        # Do something with the filtered email, e.g., print subject
        print(item.subject)