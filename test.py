import receive_sms # Import the library

print('version: '+receive_sms.version()) # Print the version

data = receive_sms.get_messages(number_phone = '12018577757') # Get messages sent to 12018577757

# Print informations of each message
for msg in data:
    print(msg.text) # The content of the message
    print('from '+msg.from_number) # The number from which the message originated
    print('to '+msg.to_number) # Your number, in this case it's 12018577757
    print('the '+msg.date.strftime("%m/%d/%Y, %H:%M")) # The date
    print('\n') # Line break