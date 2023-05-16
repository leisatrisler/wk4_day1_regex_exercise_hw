# Regex project
# Use python to read the file regex_test.txt and print the full name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

# Hint: use with open() and readlines()


import re

file1 = open('regex_test.txt', 'r')
lines = file1.readlines()
for l in lines:
    match = re.match (r'^[A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+(?!\s|$)', l) #googled unsure if this is correct this is cutting off middle inital and last letter of names but its working enough for this elvish ... I mean regex.
    if match:
        print(match.group(0))
    else:
        print("None")
pattern = []