import re

pattern = r"[a-zA-Z]+"
sequence = "1Cookie"
if re.match(pattern, sequence):
    print("Match!")
else: 
    print("Not a match!")