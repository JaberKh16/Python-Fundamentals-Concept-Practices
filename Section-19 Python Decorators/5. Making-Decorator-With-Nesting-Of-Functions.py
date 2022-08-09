

def differentiate_max_min(func1, func2, num_list):
    def find_largest_num(num_list):
        max_num = 0
        for val in num_list:
            if val > max_num:
                max_num = val
            else:
                continue
        return max_num

    def find_smallest_num(num_list):
        smallest_num = 999
        for val in num_list:
            if val < smallest_num:
                smallest_num = val
            else:
                continue
        return smallest_num
    
    largest_num = find_largest_num(num_list)
    smallest_num = find_smallest_num(num_list)
    return (largest_num, smallest_num)


num_list = [10, 4, 1, 4, -10, -50, 32, 21, 0, -4, 53]

@differentiate_max_min
def getting_both_values(largest_num, smallest_num):
    return (largest_num, smallest_num)

getting_both_values(differentiate_max_min())