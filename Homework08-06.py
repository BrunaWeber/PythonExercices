#Exercice 1 - Changing first letters:

def camel2Pascal(camelText):

    pascalText = camelText[0].upper() + camelText[1:]
    return pascalText

name_camel = "oneTwoThree"
name_pascal = camel2Pascal(name_camel)

print("Camel case = " + name_camel)
print("Pascal case = " + name_pascal)


#a-Convert pascal-case to camel case:


#b-Convert camel-case to pascal case:

#Exercice2:

iban="IE23AIBK22446612345678"

print("Iban = " + iban[:20])

print("Country = " + iban[:2])

print("CheckSum = " + iban[2:4])

print("BIC = " + iban[4:8])

print("Branch = " + iban[8:14])

print("ACNum = " + iban[14::])

































