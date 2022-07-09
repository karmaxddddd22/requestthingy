import requests
r = requests.get(input("what website?: "))
#you can edit the get part to whatever type of request you want
print(r.text)
