
myString="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
            with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

def myFind(text,string_list):
    myString_list = text.split()
    print(myString_list)
    print(string_list)

    global myString

    for i in range(len(string_list)):
        if (' ' in string_list[i]) == False:
            for j in range (len(myString_list)):
                    #print("No Spaces!!")
                    if string_list[i].lower() == myString_list[j].lower():
                        myString= myString.replace(string_list[i], '\033[44;33m{}\033[m'.format(string_list[i]))

        elif (' ' in string_list[i]) == True:
                # print(string_list[i])
                # print("Found Spaces!!")
                new_list = string_list[i].split()
                #print("New List : {}".format(new_list))
                for i in range(len(new_list)):
                     for j in range(len(myString_list)):
                         if new_list[i].lower() == myString_list[j].lower():
                             new_list_string=""
                             myString_list_string=""
                             new_list_string=new_list_string.join(new_list).lower()
                             myString_list_string=myString_list_string.join(myString_list[j:j+len(new_list)]).lower()
                             if new_list_string == myString_list_string:
                                print(new_list_string)
                                print(myString_list_string)
                                for i in range(len(new_list)):
                                    myString = myString.replace(new_list[i],'\033[44;33m{}\033[m'.format(new_list[i]))


    print(myString)

string_list=[]
string_list = input("Enter strings to be searched, comma seperated : ").split(',')
myFind(myString,string_list)

#mySearch(myString,string_list)
# print(string_list)