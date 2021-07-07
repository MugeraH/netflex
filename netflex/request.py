from decouple import config
import requests 

api_key = config('API_KEY')

def get_currencies():
    '''
    Function that gets the json response to our url request
    '''
    get_currencies_url = f"https://free.currconv.com/api/v7/currencies?apiKey={api_key}"
    currency_data = requests.get(get_currencies_url).json()["results"]
    
    currencies = []
    for data in currency_data:
         currencies.append(data)
   

    return currencies
    