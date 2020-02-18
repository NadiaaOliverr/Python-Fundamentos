import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get("https://api.github.com/users/nadiaaoliverr/repos")
# falar da importância de ver o que está nos retornando, se é um 404, um 200, um 201.. e por ai vai
print(response.status_code)

# print(response.json())

pass_times = response.json()['name']
jprint(pass_times)
