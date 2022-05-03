# 📖 Presentation
`receive_sms` is a library which allows to receive SMS in python free and unlimited.
# ⚙️ Installation
You can download the file or use [PyPi](https://pypi.org/project/receive-sms/) :
```
pip install receive-sms
```
For getting informations, you can use : 
```
pip show receive-sms
```
# ⌨️ Use
```python3
receive_sms.get_messages(phone_number='12018577757')
```
Returns the last 100 messages sent to `phone_number` (newest to oldest). [How do I know which `phone_number` to put?](https://github.com/Emilien-B/receive-sms#the-phone-numbers-you-can-use)


Messages are returned as a `message` class, here are its attributes:
```python3
message.text
```
Returns the content of message (`str`)
```python3
message.from_number
```
Returns the phone number you originally chose (`str`)
```python3
message.to_number
```
Returns the phone number that sent the message (`str`)
```python3
message.date
```
Returns the date of the message, imprecise (`datetime`)
# 💾 Example
```python3
import receive_sms # Import the library

data = receive_sms.get_messages(phone_number = '12018577757') # Get messages sent to 12018577757

# Print informations of each message
for msg in data:
    print(msg.text) # The content of the message
    print('from '+msg.from_number) # The number from which the message originated
    print('to '+msg.to_number) # Your number, in this case it's 12018577757
    print('the '+msg.date.strftime("%m/%d/%Y, %H:%M")) # The date
    print('\n') # Line break
```
This file is [here](/test.py).
# ℹ️ To know
• Phone numbers are public, everyone can see received messages.

• Messages longer than 150 characters are split.

• The library uses [sms-online.co](https://sms-online.co/). 

### The phone numbers you can use

`+1 201-857-7757` - 🇺🇸 United States

`+1 787-337-5275` - 🇵🇷 Puerto Rico

`+60 11-1700 0917` - 🇲🇾 Malaysia

`+44 7520 635797` - 🇬🇧 United Kingdom

`+46 76 943 62 66` - 🇸🇪 Sweden
