# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from ast import Return
from importlib.resources import contents


def read_file_content(filename):
    # [assignment] Add your code here
    f = open(filename, 'r')
    content = f.readlines()
    return print(content)    
    



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}


read_file_content('story.txt')