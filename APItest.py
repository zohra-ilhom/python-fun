import requests
import pprint

# command k to clear terminal 


number = input("type out a number between 0-2")
number = int(number)

r = requests.get('https://api.dailysmarty.com/posts')
r.json()

pprint.pprint(r.json()['posts'][number]) 

