import statistics

"""
def quicksort(num_list):
    if len(num_list) <= 1:
        return num_list
    else:
        median_value = statistics.median([  # extra brackets needed for position purpose
            num_list[0],
            num_list[len(num_list) // 2],
            num_list[-1]
        ])
        left_list = []
        middle_list = []
        right_list = []
        for i in num_list:
            if i < median_value:
                left_list.append(i)
            elif i > median_value:
                right_list.append(i)
            else:
                middle_list.append(i)
        return (quicksort(left_list) + middle_list + quicksort(right_list))


sorted_list = quicksort([31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28])
print(sorted_list)
"""