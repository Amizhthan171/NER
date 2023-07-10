policy_number_value = '123'
policy_bbox_values = [(1, 2, 3, 4)]
policy_page_number = 1

result_dict = {
    'policy number': [policy_number_value, policy_page_number, *policy_bbox_values[0], 'NA']
}

print(result_dict)