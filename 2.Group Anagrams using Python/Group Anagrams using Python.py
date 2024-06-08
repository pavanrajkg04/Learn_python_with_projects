'''
Problem Statement:
You are given a list of strings, and you need to group the strings into anagrams. 
An anagram is a word formed by rearranging the letters of another, such as "cinema" and "iceman". 
Write a function in Python that takes a list of strings and returns a list of lists, 
where each inner list contains words that are anagrams of each other.
input = ["tea", "eat", "bat", "ate", "arc", "car"]
expected output = [['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']]
'''
def group_anagrams(words):
    # Initialize an empty dictionary to hold the anagrams groups
    anagrams = {}
    
    # Print the input list of words (for debugging purposes)
    print(words)
    
    # Iterate through each word in the input list
    for word in words:
        # Sort the letters of the word and join them back into a string
        sortedwords = "".join(sorted(word))
        
        # If the sorted string is already a key in the dictionary, append the word to the list
        if sortedwords in anagrams:
            anagrams[sortedwords].append(word)
        else:
            # If the sorted string is not a key, create a new entry with the word in a list
            anagrams[sortedwords] = [word]
    
    # Print the dictionary of anagrams groups (for debugging purposes)
    print(anagrams)
    
    # Return the list of anagrams groups
    return list(anagrams.values())

# Example usage
words = ["tea", "eat", "bat", "ate", "arc", "car"]

# Call the function and print the result
print(group_anagrams(words))
