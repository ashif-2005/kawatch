from twilio.rest import Client
import random

# Twilio account SID, auth token, and phone number
account_sid = 'AC4eb4231aadad14ce99b09e3a21803677'
auth_token = '54b5099ae786e3c61fb8d7fd94bb9408'
twilio_phone_number = '+13159225759'

# Generate a random OTP
otp = random.randint(100000, 999999)

# Destination phone number to send the OTP
destination_phone_number = '+919629158412'  # Replace with the recipient's phone number

print(otp)

# Create a Twilio client
client = Client(account_sid, auth_token)

# Compose and send the OTP message
message = client.messages.create(
    body=f'Your OTP is: {otp}',
    from_=twilio_phone_number,
    to=destination_phone_number
)

# Print the message SID as confirmation
print(f"OTP sent successfully. Message SID: {message.sid}")