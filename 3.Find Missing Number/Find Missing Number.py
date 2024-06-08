'''
Q: You are given an array containing a range of numbers from 0 to 
𝑛
n with some missing numbers. Write a function in Python that takes this array as input and returns a list of all the missing numbers in the array.

Example:
Input: [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
Expected Output: [4, 12, 15]
Constraints:
The array can be unsorted.
The array contains only unique integers.
The range of numbers is from 0 to 𝑛

Follow-up Questions:
How would your approach change if the array contains duplicates?
Can you optimize the space complexity of your solution?
'''

def find_missing(Input):
    # Find the maximum number in the input list to identify the upper bound of the range
    max_number = max(Input)
    
    # Find the minimum number in the input list to identify the lower bound of the range
    min_number = min(Input)
    
    # Initialize an empty list to store the missing numbers
    result = []
    
    # Loop through each number in the range from min_number to max_number (inclusive)
    for i in range(min_number, max_number + 1):
        # Check if the current number 'i' is not present in the input list
        if i not in Input:
            # If 'i' is missing, append it to the result list
            result.append(i)
    
    # Return the list of missing numbers
    return result

# Define the input list
Input = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]

# Call the find_missing function with the input list and store the result
result = find_missing(Input)

# Print the result which is the list of missing numbers
print(result)  # Expected Output: [4, 12, 15]

