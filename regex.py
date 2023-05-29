import re

text = "dsjcnwoeichweoicjweiocfjw\nPOLICY NUMBER : AAA-BBBB-CCCC-DDDD\ndlkcnwkocn"

pattern = r"(?<=POLICY NUMBER : )([A-Z]{3}-[A-Z]{4}-[A-Z]{4}-[A-Z]{4})"
match = re.search(pattern, text)

if match:
    policy_number = match.group()
    print("Policy Number:", policy_number)
else:
    print("Policy number not found.")
