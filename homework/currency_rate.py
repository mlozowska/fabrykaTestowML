'''
function to get the real-time currency exchange rate of GBP, where USD is the base currency
function to get the current date and time & response time
loop to run code every 15 sec & timeout exception
'''
import requests
import time
from datetime import datetime


while True:
    def get_currency_rate(api_key, to_currency):
        try:
            r = requests.get(url, timeout=6)
            result = r.json()
            print(f'Current Exchange Rate from USD to GBP: ', result['rates']['GBP'])
        except:
            print("Timeout error")


    def timestamp():
        # current date & time
        now = datetime.now()
        date_time = now.strftime('%m/%d/%Y, %H:%M:%S.%f')
        print(f'Date and time: ', date_time[:-4])

        # response time
        r = requests.post(url)
        print(f'Response time: ', r.elapsed.total_seconds(), 'sec')


    # Driver code
    if __name__ == '__main__':

        # store API key as a variable for easier access
        api_key = 'c514d9fa345f40258e71cbc4df2e22e2'

        # currency code
        to_currency = 'GBP'

        # main url
        url = 'https://api.currencyfreaks.com/latest?apikey=' + api_key + '&symbols=' + to_currency

    #functions calling
    get_currency_rate(api_key, to_currency)
    timestamp()
    time.sleep(15)
