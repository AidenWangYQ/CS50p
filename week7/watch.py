# input long url, output short url
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"', s)
    if matches is None:
        return None
    else:
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()

# check that matches is None first before matches.groups(1) is None
# without ^ at the start of the pattern, re.search will go through the string and find any resemblance of the pattern
# ^ and $ means re.search searches for patterns that explicitly start and end with the things between ^&$, so if you are searching from a long string, dont include them