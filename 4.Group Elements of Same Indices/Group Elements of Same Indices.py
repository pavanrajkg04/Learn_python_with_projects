'''
Q: You are given a list of lists, where each inner list represents elements grouped by indices. 
Implement a Python function to group the elements of the same indices and return them as separate lists.

input_lists = [[10, 20, 30], [40, 50, 60], [70, 80, 90],[1]]
# After grouping elements:
# Group 0: [10, 40, 70]
# Group 1: [20, 50, 80]
# Group 2: [30, 60, 90]
'''

def group_indices(lists):
    group = {}  # Create an empty dictionary to store grouped elements
    
    # Loop through each inner list
    for i in lists:
        # Loop through each element in the inner list along with its index
        for j, element in enumerate(i):
            # Check if the index j already exists in the group dictionary
            if j not in group:
                # If not, create a new list with the element at index j
                group[j] = [element]
            else:
                # If yes, append the element to the existing list at index j
                group[j].append(element)
    
    # Print or return the grouped elements
    for index, elements in group.items():
        print(f"Group {index}: {elements}")

# Test the function
input_lists = [[10, 20, 30], [40, 50, 60], [70, 80, 90],[1]]
group_indices(input_lists)
