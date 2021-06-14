#open file:
file = open("C:/Users/bruna/source/repos/PythonExercices/PythonText.txt", "r")#open file

#print(file.read())
text = file.read()

#Making list with text:
text_list = text.split()#make the text as a list
#print(text_list)

#variables to use to count:
word1 = input(str("Enter a word: "))

count = text_list.count(word1)
print (f"The word {word1} appears {count} time(s)")


#count = text_list.count(word2)
#print (f"The word {word2} appears {count} time(s)")

#count = text_list.count(word3)
#print (f"The word {word3} appears {count} time(s)")

#count = text_list.count(word4)
#print (f"The word {word4} appears {count} time(s)")

###########################################

#How to search words in a file: #TO DO



