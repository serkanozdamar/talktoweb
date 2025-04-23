import io
import json

with io.open('data/roster_data.json', 'r', encoding='utf-8') as f:
    my_lines = f.readlines()
    print(my_lines)

#     my_json = json.load(f)
#
# print(type(my_json))
# print(my_json)
#
# with io.open('my_json_key_value.json', 'r', encoding='utf-8') as f:
#     my_json = json.load(f)
#
# print(type(my_json))
# print(my_json)