import os

currentPath = os.getcwd()
# get file name from user
name = input("Enter file name: ")
# read file from user
handle = open(currentPath,name)

# create a dict() to store data 
counts = dict()
# by using for loop reading all the lines
for line in handle:
    # split the line
    words = line.split()
    # looping through each word
    for word in words:
        # storing and counting the repeatative words
        counts[word] = counts.get(name, 0)+1

# count the bigword and bigcount
bigWord = None
bigCount = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigCount, bigWord)
