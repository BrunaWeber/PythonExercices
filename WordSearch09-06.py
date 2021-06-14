#Open a File:
file = open("C:/Users/bruna/source/repos/PythonExercices/PythonText.txt", "r")#open file

def wordSearch (searchTerm):
    text = file.read()#read a file
    print(text)
    text_list = text.split()#make the text as a list
    #print(text_list)

    searchTerm = input(str("Enter a word that you would like to Search: "))
    count = text_list.count(searchTerm)

    if searchTerm in text_list:
        print(f"{searchTerm} is present in the text {count} times.") 
            
    else:
        print(f"This text does not contain the word {searchTerm}. \n Try enter another term: ")        
        #return 

wordSearch(input)



    
