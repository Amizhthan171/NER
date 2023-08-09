import re

def is_dollar_amount(text):
    pattern = r'^\$\d+(\.\d+)?$'
    return re.match(pattern, text) is not None

# Test cases
test_strings = ["$100", "$100.50", "Not a dollar amount", "$.50", "123"]

for test_string in test_strings:
    if is_dollar_amount(test_string):
        print(f"'{test_string}' is a dollar amount.")
    else:
        print(f"'{test_string}' is not a dollar amount.")