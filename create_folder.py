# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:27:19 2024

@author: Administrator
"""

import os

# List of project names
project_names = [
    "Number Guessing Game", "Group Anagrams using Python", "Find Missing Number", 
    "Group Elements of Same Indices", "Calculate Mean, Median, and Mode using Python", 
    "Calculate Execution Time of a Python Program", "Count Number of words in a Column", 
    "Rock Paper Scissors Game using Python", "Print Emojis using Python", 
    "Correct Spellings using Python", "Scraping Github Profile using Python", 
    "Visualize Linear Relationships using Python", "Generate Text using Python", 
    "Scrape Table From a Website using Python", "Extract Text From PDF using Python", 
    "Reversing a String using Python", "Match Sequences using Python", 
    "QR Code using Python", "Decode a QR Code using Python", "Creating Dummy Data using Python", 
    "Remove Cuss Words using Python", "Find Duplicate Values using Python", 
    "Detect Questions using Python", "Voice Recorder using Python", 
    "Reading and Writing CSV Files using Python", "Box Plot using Python", 
    "Send Instagram Messages using Python", "Age Calculator using Python", 
    "LCM using Python", "Price Elasticity of Demand using Python", 
    "Find the Most Frequent Words in a File", "Find the Number of Capital Letters in a File", 
    "Index of Maximum Value in a Python List", "Index of Minimum Value in a Python List", 
    "Voice Recorder using Python", "Send Instagram Messages using Python", 
    "Animated Scatter Plot", "Create Font Art using Python", 
    "Collage Maker with Python", "Get Phone Number Details using Python", 
    "Display a Calendar using Python", "Internet Speed Test using Python", 
    "Text to Handwriting with Python", "Shutdown Computer using Python", 
    "Send Automatic Emails using Python", "Defang IP Address", 
    "Password Authentication using Python", "Web Scraping to create a dataset", 
    "Resume Scanner", "Merge Sort Algorithm", "Pick a Random card using Python", 
    "Quartile Deviation using Python", "Count Character Occurrences", 
    "Pyramid Pattern using Python", "Sequential Search", "Swap Variables using Python", 
    "Sorting NumPy Arrays", "Validate Anagrams", "Create Tables with Python", 
    "Recursive Binary Search", "Backward For Loop", "Dijkstra’s Algorithm using Python", 
    "Hash Tables using Python", "Queues using Python", "Validate a Binary Search Tree", 
    "Stacks using Python", "Check Palindrome Words", "Breadth-First Search Algorithm", 
    "Plot Annotations", "Real-Time Currency Converter", "FizzBuzz Algorithm", 
    "Extract Keywords with Python", "Read Data From Google Sheets with Python", 
    "Invoice Generator with Python", "Text-Based Adventure Game", "Mad Libs Game with Python", 
    "Create Acronyms using Python", "Alarm Clock with Python", "Email Slicer with Python", 
    "Story Generator with Python", "Generate Password with Python", 
    "Play Rock, Paper, and Scissors with Python", "Dice Roll Simulator", 
    "QR Code Generator", "Animal Quiz Game", "Print Coloured Text", 
    "BMI Calculator", "Fahrenheit to Celcius Converter", "Taking Multiple User Inputs", 
    "Convert Roman Numbers to Decimals", "Pearson Correlation", "Treemap using Python", 
    "Convert Image to an array", "Scrape IMDb with Python", "Python Projects for Resume", 
    "Python Project Ideas for Final Year", "Advance Python Projects", 
    "End to End Chatbot with Python", "Message Encryption using Python", 
    "Calculate Distance Between Two Locations", "Netflix Recommendation System", 
    "Time Series Graph using Python", "Get Stock Price Data using Python", 
    "Candlestick Chart using Python", "Word Cloud From a Pandas DataFrame", 
    "LeNet-5 Architecture using Python", "End-to-end Encryption using Python", 
    "Get Live Covid-19 Data using Python", "Violin Plot using Python", 
    "Sunburst Plot with Python", "Calculation of Accuracy using Python", 
    "Visualize a Neural Network using Python", "Bias and Variance using Python", 
    "Get Live Weather Updates using Python", "Count Objects in Image using Python", 
    "Scrape Trending News using Python", "Real-time Stock Price Data Visualization using Python", 
    "OTP Verification using Python", "Data Visualization on a map", 
    "Choropleth Map with Python", "Egg catcher game", "Extract Country Details", 
    "Convert Text to Numerical data", "AUC and ROC using Python", 
    "Interactive Language Translator", "Maximum Profit Finder", "Language Detection", 
    "Histogram and Density Plots with Python", "Radar Plot with Python", 
    "Create a Chatbot with Python", "Stopwords Removal", "Unicode Characters Removal", 
    "Grammar Correction with Python", "Caterpillar Game with Python", "Maze Solver", 
    "Encrypt and Decrypt Messages with Python", "Screen Pet Game with Python", 
    "Robot Builder with Python", "Generate Word Clouds", "Bitcoin Mining", 
    "Password Picker", "Typing Test Game GUI", "Contact Book with Python", 
    "Hangman Game with Python", "URL Shortner with Python", "Digital Clock GUI", 
    "Get Desktop Notifications with Python", "Use Your Phone Camera for Computer Vision", 
    "Music Player GUI", "Game of Life with Python", "Extract Text from videos", 
    "Fidget Spinner Game", "Spelling Correction with Python", "Create Amazing Graphics with Python", 
    "Monty Hall Simulator", "Video to Audio Converter", "Tic Tac Toe GUI", 
    "Calculator GUI", "Number Guessing Game", "Image Converter GUI", 
    "Weight Converter GUI", "Visualize a Chess Board with Python", 
    "Age and Gender Detection", "Bar Code and QR Code Reader", "Create Audiobook with Python", 
    "Face Detection", "Extract Text from PDF", "Card Game using DS and Algo", 
    "Web Scrapper with Python", "Create a Pencil Sketch using Python", 
    "Text Editor GUI", "Instagram Filters with Python", "Count Number of Rainy days in a year", 
    "Send Emails with Python", "Image Segmentation", "Quick Sort Algorithm", 
    "Deploy a Chatbot", "Create a Telegram Bot", "Scraping Twitter without API", 
    "Text to Speech Converter", "Keyword Research with Python", 
    "Next Word Prediction", "Scrape Wikipedia", "Lives Game", 
    "Web Scraping to create a CSV", "Scrape Instagram", "Image Filtering", 
    "Audio Processing", "Analog Clock with Python", "Create a Simple Chatbot", 
    "Clock APP with Python", "3D Graphs", "Calendar GUI", 
    "Get Real-time weather with Python"
]

# Create folders for each project name
for index, project in enumerate(project_names):
    name = str(index+1)+"." + project
    os.makedirs(name, exist_ok=True)
    print(f"Folder '{project}' created.")
    file_path = os.path.join(name, project + ".py")
    with open(file_path, 'w') as f:
        f.write("# This is a placeholder file for " + project)
    
    print(f"Folder '{name}' created with file '{file_path}'.")