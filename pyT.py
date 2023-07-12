from exchangelib import Account, Credentials

# Set up credentials
credentials = Credentials(username='your_username', password='your_password')

# Connect to the account
account = Account(primary_smtp_address='your_email@example.com', credentials=credentials, autodiscover=True)

# Define the list of sender email addresses to filter
sender_list = ['sender1@example.com', 'sender2@example.com', 'sender3@example.com']

# Create an empty list to store recipient addresses
recipient_list = []

# Traverse through the inbox and subfolders
for folder in account.inbox.walk():
    # Filter emails with sender addresses from the sender_list
    filtered_emails = folder.filter(sender__in=sender_list)

    # Traverse through the filtered emails
    for email in filtered_emails:
        # Extract recipient addresses and append to the recipient_list
        for recipient in email.to_recipients:
            recipient_list.append(recipient.email_address)

# Print the recipient_list
print(recipient_list)