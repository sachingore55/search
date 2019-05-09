import re

myString="""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
            with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

def mySearch(myString,string_list):
    for i in range(len(string_list)):
        for index in re.finditer(string_list[i].lower(), myString.lower()):
            print("Found {} at index {} ".format(string_list[i],index.start()))

string_list= input("Enter strings to be searched, comma seperated : ").split(',')
mySearch(myString,string_list)

