policy_number_value = '123'
policy_bbox_values = [(1, 2, 3, 4)]
policy_page_number = 1

bbox_str = [str(coord) for bbox in policy_bbox_values for coord in bbox]

result_dict = {
    'policy number': [policy_number_value, policy_page_number, *bbox_str, 'NA']
}

print(result_dict)