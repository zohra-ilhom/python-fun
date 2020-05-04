import requests
import pprint

number = input("type out a number between 0-100 >>")
number = int(number)

r = requests.get('https://api.dailysmarty.com/posts')
r.json()

pprint.pprint(r.json()['posts'][number]) 
pprint.pprint(r.json()['posts'][number]['id']) 
#pprint.pprint(r.json()['posts'][number]) 

# command k to clear terminal 