'''
function to get the real-time currency exchange rate of GBP, where USD is the base currency
function to get the current date and time & response time
loop to run code every 15 sec & timeout exception
export data to CSV file
'''
import requests
import time
from datetime import datetime

while True:
    def get_currency_rate():
        try:
            return requests.get(url, timeout=3)
        except:
            print("Timeout error")


    def timestamp():
        r = requests.get(url)
        result = r.json()
        ex_rate = result['rates']['GBP']
        print(f'Current Exchange Rate from USD to GBP: ', ex_rate)

        # current date & time
        now = datetime.now()
        date_time = now.strftime('%m/%d/%Y %H:%M:%S.%f')
        print(f'Date and time: ', date_time[:-4])

        # response time
        r = requests.post(url)
        response_time = round(r.elapsed.total_seconds() * 1000)
        print(f'Response time: ', response_time, 'ms')
        print('--- --- --- --- ---')

        # export the data to CSV file
        f = open("./file.csv", "a")
        f.write("{},{} ms,{} gbp\n".format(date_time, response_time, ex_rate))
        f.close()


    # Driver code
    if __name__ == '__main__':
        # store API key as a variable for easier access
        api_key = '339d4e7197334541aeda4942d4e854ad'

        # currency code
        to_currency = 'GBP'

        # main url
        url = 'https://api.currencyfreaks.com/latest?apikey=' + api_key + '&symbols=' + to_currency

    # functions calling
    get_currency_rate()
    timestamp()
    time.sleep(15)
