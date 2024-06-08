'''
Q: "Imagine you have a Python program that performs a specific task, and you want to measure its execution time.
 How would you go about doing this? Can you provide a step-by-step explanation of the process, 
 including any relevant code snippets or modules you might use?"
'''

# Import the time module to work with time-related functions
from time import time

# Start the timer
start_time = time()
print(start_time)
# Perform the specific task: creating acronyms
word = "Artificial Intelligence"
text = word.split()
acronym = " "
for i in text:
    acronym = acronym + str(i[0]).upper()
print(acronym)

# Stop the timer
end_time = time()
print(end_time)
# Calculate the total execution time
total_time = end_time - start_time

# Print the total execution time
print(total_time)

# Print a formatted string indicating the total execution time
print(f"The total execution time is {total_time}")
