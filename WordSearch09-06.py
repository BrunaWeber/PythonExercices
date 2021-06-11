file = open('C:/Users/bruna/source/repos/PythonExercices/PythonText.txt', 'r')#open file

text = file.read()#read a file

text_list = text.split()#make the text as a list

print(text_list)#print list of words just to test


def wordSearch (text_list,searchTerm):
    
    searchTerm = input("Enter a word that you would like to Search: ")
    for searchTerm in text_list:
        if searchTerm in text_list:
            searchTerm += 1
            print(searchTerm)
        else :
            print("This text does not contain this word.Try search another one.")   



#print(index = file.find("python"))