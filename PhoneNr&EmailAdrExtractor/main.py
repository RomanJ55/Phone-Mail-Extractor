import pyperclip
import re

# USA Format phone numbers
phone_regex_us = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # separator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension(group[8])
)''', re.VERBOSE)

# german & some international spelling(minimum false positives)
phone_regex = re.compile(
    r"(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))", re.VERBOSE)
email_regex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+      # username
 @                      # @ symbol
 [a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# We take the imput from the clipboard
# just Ctrl+a and Ctrl+c any text that you want to check
input = str(pyperclip.paste())

# takes regex re.compile(.....) objects, return an empty list
# if none given or no matches found


def get_matches(*args):
    matches = []
    for arg in args:
        for groups in arg.findall(input):
            matches.append(groups[0])
    if len(matches) == 0:
        print("No matches found!")
    return matches


matches = get_matches(email_regex, phone_regex, phone_regex_us)

matches_sting = "\n".join(matches)
print(matches_sting)
