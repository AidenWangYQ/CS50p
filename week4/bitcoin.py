# check command-line argument, if len(sys.agv) != 2 or float, sys.exit
# if no comman-line argument, prompt
# get json data of bitcoin price using get method in request module, capturing any exceptions
# go through data and find usd price
# calculate price and display
# in json data, under value of "bpi" key, under value of "USD" key, under value of "rate" key, is the data we want
import requests
import sys


def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        try:
            request = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = data["bpi"]["USD"]["rate"]
        price_without_comma = price.replace(",", "")
        total_price = float(price_without_comma) * float(sys.argv[1])
        print(f"${total_price:,.4f}")
    except request.RequestException:
        sys.exit()


main()