import re

text = "dsjcnwoeichweoicjweiocfjw\nPOLICY NUMBER : ABC123-CDF567YH-HY1234\ndlkcnwkocn"

pattern = r"(?<=POLICY NUMBER : )([A-Z0-9\-]+)"
match = re.search(pattern, text)

if match:
    policy_number = match.group()
    print("Policy Number:", policy_number)
else:
    print("Policy number not found.")
