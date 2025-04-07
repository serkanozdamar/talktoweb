import json
import urllib.request

uh = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1972166.json")
data = uh.read()

data_json = json.loads(data)
comments = data_json['comments']

my_count = 0
for comment in comments:
    my_count += comment["count"]
print(f"""count : {my_count}""")