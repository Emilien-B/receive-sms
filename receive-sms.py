# https://sms-online.co/receive-free-sms/12018577757
# 150 max

import requests
import datetime


# Class for messages
class message():
    def __init__(self, text='', from_number='', to_number='', date=datetime.datetime.now()) -> None:
        self.text = text
        self.from_number = from_number
        self.to_number = to_number
        self.date = date


def help():
    return ' See documentation : '

def version():
    return 'jsp'

def get_messages(number_phone='12018577757'):
    number_phone = number_phone.replace('+','').replace('-','').replace(' ','')
    # Get data
    response_raw = requests.get(url='https://sms-online.co/receive-free-sms/'+number_phone)
    
    if response_raw.status_code == 404:
        print('ERROR 404 : Bad phone number ('+help()+')')
        return None

    # Format data
    response_raw = response_raw.text.split('<div class="list-item">')
    response = []
    for a in response_raw:
        # Is it an ad ?
        if not 'class="adsbygoogle"' in a:
            response.append(a)

    # Format data
    result = []
    for item in response:

        item = item.split('<div class="list-item-header"> <h3 class="list-item-title">')
        item = item[1].split('</h3> <span class="list-item-meta"> <span>')
        from_number = item[0].strip()
        item = item[1].split('</span> </span> </div> <div class="list-item-content break-word">')
        date = item[0].strip()
        item = item[1].split('</div> </div>')
        text = item[0].strip()

        # Format date
        date = date.split(' ')
        value = int(date[0])
        if 'second' in date[1]:
            pass
        elif 'minute' in date[1]:
            value *= 60
        elif 'hour' in date[1]:
            value *= 60*60
        elif 'day' in date[1]:
            value *= 60*60*24
        date = datetime.datetime.now() - datetime.timedelta(seconds=value)
        from_number = '+'+from_number

        # Create and return classes
        result.append(message(text=text,from_number=from_number,to_number=number_phone,date=date))
    return result

