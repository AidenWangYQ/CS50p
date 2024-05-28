# requires 3 command-line arguments (old csv as input, new csv as output)
# read old csv file, reorganise them, write into new csv file

import csv
import sys


def main():
    check_input()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            updated_list = []
            for i, row in enumerate(reader):
                last, first = row["name"].split(",")
                row["first"] = first
                row["last"] = last
                del row["name"]
                row[i] = {
                    "first": first.strip(),
                    "last": last,
                    "house": row["house"]
                }
                updated_list.append(row[i])
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in updated_list:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def check_input():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


main()

# enumerate() function can be added to a iterable to change the elements of the iterable itself while in a loop, it assigns an index to each element
# to write to a file, remember to open a new file and address the new file as 'file' and not the file name
# writerow does not write headers, add in .writeheader() before all the writerow lines