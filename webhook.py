import requests

api_url = ''

headers = {
                    'accept' : 'application/json',
                'x-api-key'  : ''
                }
    
response = requests.get(api_url , headers=headers).json()