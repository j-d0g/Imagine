import csv
file2 = open('file_name.csv', 'rt')
contents = []
for item in file2:
    substring = item.strip("\n")
    x = substring.split(',')
    contents.append(x)
file2.close()
contents.pop(0)
print(contents)
