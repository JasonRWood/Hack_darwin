import seaborn as sns
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import json
import numpy as np

file = open("dump_darwin_values.txt", "r", encoding="utf-8")
mentions = []
values = {}
i = 0

for line in file:
    if i < 4000:
        line = line.strip('\n')
        fields = line.split(",")
        if not(fields[0] in stopwords.words()):
            mentions.append(int(fields[1]))
            values[fields[0]] = int(fields[1])
    i+=1
file.close()

test = dict((i, mentions.count(i)) for i in enumerate(values.keys()))
top = dict((i, values[i]) for cur, i in enumerate(values.keys()) if cur < 11)

sns.displot(test, bins=5)
plt.show()

fig, ax = plt.subplots()

ax.barh(list(top.keys()), list(top.values()), color="#44AA99")
ax.invert_yaxis()
ax.set_xlabel('Number of mentions')
ax.set_xticks(np.arange(0, max(list(top.values())) + 1, 50))

plt.show()

input_file = open('people.json')
json_array = json.load(input_file)
store_list = []
women_count = 0
male_count = 0
total_count = 0

occupations = {}

for item in json_array:
    occ = item["occupation"]
    if occ != "no common occupation":
        if not occ in occupations:
            occupations[occ] = 1
        else:
            occupations[occ] += 1
    if item["sex"] == "F":
        women_count +=1
    if item["sex"] == "M":
        male_count +=1
    total_count +=1

occupations = dict(sorted(occupations.items(), key=lambda item: item[1], reverse=True))
top = dict((i, occupations[i]) for cur, i in enumerate(occupations.keys()) if cur < 11)

fig, ax2 = plt.subplots()

print(top)

ax2.barh(list(top.keys()), list(top.values()),color="#44AA99")
ax2.invert_yaxis()
ax2.set_xlabel('Number of people written to with given occupation')
ax2.set_xticks(np.arange(0, max(list(top.values())) + 1, 50))

plt.show()

size_of_groups=[male_count, women_count, total_count-(women_count+male_count)]
size_of_groups2=size_of_groups[:-1]

# Create a pieplot
colors_test = ["#117733", "#CC6677", "#44AA99"]
plt.pie(size_of_groups,colors=colors_test)

# add a circle at the center to transform it in a donut chart
my_circle=plt.Circle((0,0), 0.7, color='white')

p=plt.gcf()
p.gca().add_artist(my_circle)
labels = ["male corresponder", "female corresponder", "sex unidentified"]
plt.legend(labels, loc="best")
plt.show()

plt.pie(size_of_groups2,colors=colors_test)
my_circle2 = plt.Circle((0,0),0.7,color='white')
plt.pie(size_of_groups2,colors=colors_test)

p2=plt.gcf()
p2.gca().add_artist(my_circle2)
labels = ["male corresponder", "female corresponder"]
plt.legend(labels, loc="best")

plt.show()

