import requests

user = "srikanthpragada"
URL = f"https://api.github.com/users/{user}"

resp = requests.get(URL)
if resp.status_code != 200:
    print(f"Sorry! Could not get details of user : {user}")
    exit(1)

details = resp.json()  # Response text (JSON) to be converted to dict

print(details['name'])
print(details['company'])
print(details['location'])

