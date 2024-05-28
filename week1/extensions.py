def main():
    document = input("File name: ").lower().strip()
    converted(document)


def converted(x):
    if x.find(".gif") != -1:
        print("image/gif")
    elif x.find(".jpg") != -1:
        print("image/jpeg")
    elif x.find(".jpeg") != -1:
        print("image/jpeg")
    elif x.find(".png") != -1:
        print("image/png")
    elif x.find(".pdf") != -1:
        print("application/pdf")
    elif x.find(".txt") != -1:
        print("text/plain")
    elif x.find(".zip") != -1:
        print("application/zip")
    else:
        print("application/octet-stream")


main()