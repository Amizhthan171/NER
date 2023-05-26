from collections import defaultdict

pages = {
    "1": {"loan_number": "12345", "doc_id": "1"},
    "2": {"loan_number": "12345", "doc_id": "3"},
    "3": {"loan_number": "12346", "doc_id": "2"},
    "4": {"loan_number": "12346", "doc_id": "2"},
    "5": {"loan_number": "12345", "doc_id": "2"}
}

grouped_pages = defaultdict(list)
for page_num, page_data in pages.items():
    key = (page_data["loan_number"], page_data["doc_id"])
    grouped_pages[key].append(page_num)

grouped_pages = dict(grouped_pages)
print(grouped_pages)
