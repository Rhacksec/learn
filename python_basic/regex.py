import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

# [] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]

pattern = r"a[ab]+a"
string = "abaaba"
match_object = re.match(pattern, string)
all_inclusions = re.findall(pattern, string)
print(match_object, all_inclusions)

string = "abbc, a.c, aabc, a-c, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
