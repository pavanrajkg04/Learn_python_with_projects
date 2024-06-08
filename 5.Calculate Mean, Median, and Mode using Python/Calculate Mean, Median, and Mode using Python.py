'''
Q : "Could you please explain how you would calculate the mean, median, and mode 
of a given list in Python, specifically for the list list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20], 
without utilizing any external libraries or modules?"

'''
def m_m_m(list1):
    # Calculate the sum of all numbers in the list
    sums = 0
    
    # Get the length of the list
    length = len(list1)
    
    # Loop through each element in the list and calculate the sum
    for i in range(0, length):
        sums = sums + list1[i]

    # Sort the list in ascending order
    s_list = sorted(list1)
    
    # Initialize an empty dictionary to store each number and its frequency
    m_list = {}
    
    # Loop through each element in the sorted list
    for i in range(0, length):
        # If the current number is not in the dictionary, add it with a frequency of 1
        if s_list[i] not in m_list:
            m_list[s_list[i]] = 1
        else:
            # If the current number is already in the dictionary, increment its frequency by 1
            m_list[s_list[i]] += 1
            
    # Calculate the mean by dividing the sum by the length of the list
    mean = sums / length
    print(mean)
    
    # Calculate the median by finding the middle element in the sorted list
    median = s_list[round(length / 2)]
    print(median)
    
    # Find the maximum frequency in the dictionary
    max_freq = max(m_list.values())
    
    # Find the number(s) with the maximum frequency (mode)
    mode = [key for key, values in m_list.items() if values == max_freq]
    print(mode)
    
    # Print the calculated mean, median, and mode along with their descriptions
    print(f"the mean is {mean} and the median is {median} and the mode is {mode} with a freqn of {max_freq}")

# Define the input list
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

# Call the function to calculate mean, median, and mode
m_m_m(list1)
