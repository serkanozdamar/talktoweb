import requests

#
# my_data_resp = requests.get("http://127.0.0.1:8000/weather-data")
#
# print(my_data_resp.status_code)
# if my_data_resp.status_code == 200:
#     print(my_data_resp.json())

my_url = "https://healthdata.gov/resource/879u-23sm.json"
my_res = requests.get(my_url)
if my_res.status_code == 200:
    my_data = my_res.json()
    for my_dict in my_data:
        for k,v in my_dict.items():
            print(k,v)
        break
    print("")