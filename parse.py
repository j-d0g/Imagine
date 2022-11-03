import csv
file_ = open('file_name.csv', 'rt')
contents = []
for user in file_:
    substring = user.strip("\n")
    x = substring.split(',')
    contents.append(x)
file_.close()
contents.pop(0)
print(contents[0][3:12])
