def main():

    # initialize values
    amount_due = 50
    total_coins_accepted = 0
    total_coins_submitted = 0

# prompt for first submission, updating total coins submitted as it is updated regardless of the coin type
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert coin: "))
    total_coins_submitted = total_coins_submitted + coin

# loop to continue requesting for coins as long as total submitted value is not >= 50
    while total_coins_submitted < 50:
        if coin == 25 or coin == 10 or coin == 5:
            total_coins_accepted = total_coins_accepted + coin
            amount_due = amount_due - coin
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")
        coin = int(input("Insert coin: "))
        total_coins_submitted = total_coins_submitted + coin

# procedure when submitted value = 50
    if total_coins_submitted == 50:
        print("Change Owed: 0")

# procedure when submitted value > 50
    if total_coins_submitted > 50:
        change_owed = coin - amount_due
        print(f"Change Owed: {change_owed}")


main()