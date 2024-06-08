'''
Q : Imagine you have a dataset stored in a list of dictionaries, where each dictionary represents a row of data. 
Each dictionary contains multiple attributes, but you are specifically interested in counting the number of words 
in a particular column named 'text'. Write a Python function that takes this dataset as input and returns the 
total number of words in the 'text' column.

data = [
    {'text': 'This is a sample sentence.'},
    {'text': 'Another example with more words in this sentence.'},
    {'text': 'Only a few words here.'}
]

expected output : Total words in the 'text' column: 17
'''
import pandas as pd  # Importing the pandas library for working with data frames

data = [  # Creating a list of dictionaries where each dictionary represents a row of data
    {'text': 'This is a sample sentence.'},  # First row with a 'text' attribute
    {'text': 'Another example with more words in this sentence.'},  # Second row with a 'text' attribute
    {'text': 'Only a few words here.'}  # Third row with a 'text' attribute
]

df = pd.DataFrame(data)  # Creating a pandas DataFrame from the list of dictionaries

column_count = len(data)  # Getting the number of rows in the data (number of dictionaries in the list)

for i in range(column_count):  # Iterating through each row in the DataFrame
    sentence = df["text"][i]  # Accessing the 'text' attribute of the current row
    word_count = len(sentence.split())  # Splitting the sentence into words and counting them
    print(sentence.split())  # Printing the list of words in the sentence
    print(word_count)  # Printing the count of words in the sentence
    df.at[i, "word_count"] = word_count  # Assigning the word count to the 'word_count' column of the DataFrame

print(df)  # Printing the DataFrame after all rows have been processed
