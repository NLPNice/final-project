import json

with open('titles.json') as f:
    titles = json.load(f)

d = dict()
for title in titles:
    res = input(title + ' :')
    d[title] = res

with open('annotated.json', 'w') as f:
    json.dump(d, f)