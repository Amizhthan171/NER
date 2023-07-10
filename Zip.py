policy_number_value = '1234'
premium_value = '5678'
coverage_amount_value = '91'

policy_number_bbox = ('1', '2', '3')  # Example bounding box values for policy number
premium_bbox = ('4', '5', '6')  # Example bounding box values for premium
coverage_amount_bbox = ('7', '8', '9')  # Example bounding box values for coverage amount

policy_number_page = 1  # Example page number for policy number
premium_page = 1  # Example page number for premium
coverage_amount_page = 2  # Example page number for coverage amount

result_dict = {
    'policy number': [policy_number_value, policy_number_page, *policy_number_bbox, 'NA'],
    'premium': [premium_value, premium_page, *premium_bbox, 'NA'],
    'coverage amount': [coverage_amount_value, coverage_amount_page, *coverage_amount_bbox, 'NA']
}

print(result_dict)