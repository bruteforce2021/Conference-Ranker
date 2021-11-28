from textblob.en import Spelling
import re

textToLower = ""

with open("train.txt", "r") as f1:           # Open our source file
    text = f1.read()                                  # Read the file

    textToLower = text.lower()

# Find all the words and place them into a list
words = re.findall("[a-z]+", textToLower)
# Join them into one string
oneString = " ".join(words)

# The path we want to store our stats file at
pathToFile = "result.txt"
# Connect the path to the Spelling object
spelling = Spelling(path=pathToFile)
spelling.train(oneString, pathToFile)
