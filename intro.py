import pathlib

# why does the tutorial not work: f is the variable name, r is the mode which an be a bunch of things read, write or both r+
# with open('openfile.txt', 'r') as f: 
#   contents = f.read()
#   print(contents)

# # I want to print everything in the openfile.txt file. if you only want to read the first line change it to f.radlines vs. line 
# #copy the contents and print it should show the second line 
# with open(pathlib.Path(__file__).parent / 'openfile.txt') as f:
#     contents = f.read()
#     print(contents)
   
# print("\n") 
# #I want to create a new file and write to it. But where does it get added 
# with open(pathlib.Path(__file__).parent / 'openfile.txt' , 'r+') as z:
#     z.write('type anything here zooo')
#     how_many_characters_to_read = 2
#     #if you add how_many_characters_to_read variable in the paranthesis of read, it will read only those number of characters
#     zcopyread = z.read(how_many_characters_to_read)
#     print(zcopyread)
  




with open(pathlib.Path(__file__).parent / 'testingtesting.txt' , 'w+') as z:
    z.write('i want to check if a folder is created and if thix text is added to the folder')
    #how_many_characters_to_read = 2
    #if you add how_many_characters_to_read variable in the paranthesis of read, it will read only those number of characters
    zcopyread = z.read()
    print(zcopyread)

# how to comment out multiple lines of code: command + k + C
# how to uncomment mulitple lines of code: command + k + u