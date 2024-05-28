# open csv file, read the file and append them to 2 lists, table and header
# table is a list of lists of data, header is a list of headers
import csv
import sys
from tabulate import tabulate


def main():
    check_input()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = [row for row in reader]
            print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_input():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


main()