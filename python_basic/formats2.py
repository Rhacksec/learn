import csv, re 
#
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    dic = {}
    for row in reader:
        if '2015' in row[2] : 
            if row[5] in dic:
                dic[row[5]] += 1
            else: dic[row[5]] = 1
#print (dic)
print(sorted(dic.items(), key=lambda x: x[1]))
'''
правильно
import csv
crimes = [row[5] for row in csv.reader(open("Crimes.csv"))]
print(max(set(crimes), key=lambda x: crimes.count(x)))

students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(students)
'''