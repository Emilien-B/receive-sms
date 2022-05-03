# 📖 Presentation
`receive_sms` is a library which allows to receive SMS in python.

# Use
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

# To know
• Phone numbers are public, everyone can see received messages.

• Messages longer than 150 characters are split.

• The library uses [sms-online.co](https://sms-online.co/). 

### The phone numbers you can use

`+1 201-857-7757` - 🇺🇸 United States

`+1 787-337-5275` - 🇵🇷 Puerto Rico

`+60 11-1700 0917` - 🇲🇾 Malaysia

`+44 7520 635797` - 🇬🇧 United Kingdom

`+46 76 943 62 66` - 🇸🇪 Sweden
