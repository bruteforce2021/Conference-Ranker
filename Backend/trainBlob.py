from textblob.en import Spelling
import re

textToLower = ""

with open("train.txt", "r") as f1:           # Open our source file
    text = f1.read()                                  # Read the file

    textToLower = text.lower()

