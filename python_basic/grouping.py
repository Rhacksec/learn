import re

#pattern = r"(\w+)-\1"
pattern = r"(\b\w)\w"
string = "this' !is. ?n1ce,"
match=re.findall(pattern, string)
print(match)
#duplicates = re.findall(pattern, string)
#print(duplicates)
