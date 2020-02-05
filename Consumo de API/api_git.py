import requests, json

response = requests.get("https://api.github.com/users/nadiaaoliverr")
json_response = response.json()

formatted_response = json.dumps(json_response, indent=2,ensure_ascii=False)

print(formatted_response))