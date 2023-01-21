
import requests
import argparse
import os

try:
    chat_id = os.environ['CHAT_ID']
    token = os.environ['TOKEN']
    message = os.environ['MESSAGE']
except:
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', required=True)
    parser.add_argument('-i', '--id', required=True)
    parser.add_argument('-m', '--message', required=True)
    args = parser.parse_args()
    chat_id = args.id
    token = args.token
    message = args.message
    
URL = 'https://api.telegram.org/bot'

data = {'disable_web_page_preview': 1, 'chat_id': chat_id, 'text': message, 'parse_mode': 'HTML'}

request = requests.post(URL + token + '/sendMessage', data=data, timeout=2)
print('TELEGRAM', request.status_code, request.reason, chat_id)