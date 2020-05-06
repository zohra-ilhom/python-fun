# testing out .gitignore functionality 
#!/usr/bin/python3
import pathlib


with open(pathlib.Path(__file__).parent / 'apikey.txt') as f:
 
    text = f.read()


print(text)
    