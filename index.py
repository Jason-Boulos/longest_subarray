def longest_subarray(binary_list):
    max_length = 0
    n = len(binary_list)

    # Iterate over all possible starting points of subarrays
    for start in range(n):
        zero_count = 0
        one_count = 0

        # Check subarrays that start from the current index
        for end in range(start, n):
            # Count 0s and 1s in the current subarray
            if binary_list[end] == 0:
                zero_count += 1
            else:
                one_count += 1

            # If counts are equal, update the max length
            if zero_count == one_count:
                max_length = max(max_length, end - start + 1)

    return max_length

    

user_binary_input = input('please enter binary numbers and add spaces between them')
user_list = user_binary_input.split()
#validated list
valid_user_input = []


#  user input  validation
for item in user_list:
    if item.isdigit() and (item == '0' or item == '1'):  # lacks negative numbers
        valid_user_input.append(int(item))
    else:
        print(f"'{item}' is not a binary number integer.")
        
        
        
result = longest_subarray(valid_user_input)
print("The length of the longest subarray with equal numbers of 0's and 1's is:", result)
