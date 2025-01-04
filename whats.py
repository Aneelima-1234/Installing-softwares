
import os
import schedule
import time

# Function to send WhatsApp message
def send_whatsapp_notification():
    email_link = "https://mail.google.com"  # Link to your email
    message = f"Please check your email: {email_link}"  # Message with email link
    
    # Send the message using npx mudslide
    os.system(f"npx mudslide send +919391031619 '{message}'")  # Replace with your phone number

    print("Notification sent!")

# Schedule the notification every hour
schedule.every(1).hours.do(send_whatsapp_notification)

print("Scheduler started. Notifications will be sent every hour.")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)