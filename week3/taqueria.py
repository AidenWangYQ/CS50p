# include a dictionary
# set up infinite loop, terminated by clt-d
# every prompt requests for a key in dict, then adds the value of the key to a 'sum of values'
# inputs must be converted to titlecase
# print out 'sum of values' before each reprompt
# capture EOFError(terminate programme), KeyError(pass&reprompt)
# use get[key] to access value of key in dict

prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total_cost = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in prices:
                total_cost = total_cost + prices.get(item)
                print(f"Total: ${total_cost:.2f}")
        except EOFError:
            print("")
            break
        except KeyError:
            pass


main()