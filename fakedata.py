from faker import Faker
import pandas as pd 
import random as rand
import csv

fake = Faker()
# generate 1000 profiles 
data = []
data = [[fake.name()] for i in range(5)]
print(data)
#max score for all attributes are 8
#max points for personality is 40 abd max point for bg is 32
for count in range(0, 5):
   average = 4
   personalityList = {"prob_solving": 0, "communication": 0, "teamwork": 0, "creativity": 0, "leadership": 0, "artistic": 0, "academic":0, "prioritisation": 0, "interpersonal":0, "handle-pressure":0}
   i = 0
   while i < 10:
      integer = rand.randint(0,8)
      #print("int", integer)
      newInteger = (average-integer) + average
      key = list(personalityList)[i]
      personalityList[key] = integer
      personalityList[list(personalityList)[i+1]] = newInteger
      i += 2
   data[count].append(personalityList)
   backgroundScore = {"cultural":0, "gender":0, "financial":0, "location":0, "education":0, "disability":0, "domestic":0, "lgbtq":0}

   i = 0
   while i < 8:
      integer = rand.randint(0,8)
      newInteger = (average-integer) + average
      #print("int", newInteger )
      key = list(backgroundScore)[i]
      backgroundScore[key] = integer
      backgroundScore[list(backgroundScore)[i+1]] = newInteger
      i += 2
   #print(backgroundScore) 
   data[count].append(backgroundScore)

# save profiles in pandas dataframe
df = pd.DataFrame(data)
print(df)

df.to_csv('file_name.csv')