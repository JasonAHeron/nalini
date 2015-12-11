import requests
import json

def get_quote():
    response = requests.post('http://api.forismatic.com/api/1.0/', data={
        'method': 'getQuote',
        'format': 'json',
        'lang': 'en',
    })
    if response.status_code != 200:
        return 'Quote Server Unavailable', 'ERROR'
    try:
        quote_dict = json.loads(response.text)
    except json.JSONDecodeError:
        return "Quote Decode Error", 'ERROR'

    return quote_dict['quoteText'] or 'Quote Unavailable', quote_dict['quoteAuthor'] or 'Author Unavailable'
