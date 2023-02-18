import requests

data= requests.get("https://swapi.dev/")
print(data.text)

if data.status_code == 200:
    print("sucessfull!")

else:
    print("unsucessfull!")