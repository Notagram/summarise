import re
from nltk import tokenize

with open("transcript.txt") as f:
    text = f.read()
    
sentences = tokenize.sent_tokenize(text)

chunks = []
max_length = 13000
curr = ""

for sent in sentences:
    curr += sent + " "
    if len(curr) >= max_length:
        chunks.append(curr)
        curr = ""

with open("output.txt", "w") as f:
    for chunk in chunks:
        f.write(chunk + "\n\n\n\n\n")

print("finished chunking")
#Summarise every point discussed in the above lecture transcript:

