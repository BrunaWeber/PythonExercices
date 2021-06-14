#Word counter (Advanced):

#stringText= "Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation"

#TextList = stringText.split()

#print(TextList)

#dict = {} #Creating an empty Dictionary
#################

def WordCounter(text):
    counts = dict()
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(WordCounter("Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. What is Python used for? Compared to many languages, Python is easy to learn and to use. Its functions can be carried out with simpler commands and less text than most competing languages. And this might explain why it’s soaring in popularity, with developers, coding students and tech companies.It’s not an exaggeration to say that Python plays a small part of all of our lives. It’s one of those invisible forces with a presence in our mobile devices, web searches and gaming (and beyond). So it was an obvious choice for inclusion in our full stack coding bootcamp. Here’s an introduction to the language itself, and some of the everyday but profound, things that Python is used for. Python was created in 1991 by Dutch programmer Guido Van Rossum. It is an interpreted language. This means that it has an interpreter to execute the programme directly, as opposed to depending more complicated machine languages. In fact, Van Rossum wants Python to eventually as understandable and clear as plain English. He has also made the language open source, which means that anyone can contribute to it, and he hopes that it will become as powerful as competing languages.“Readability” is a key factor in Python’s philosophy. As such, it aims to limit code blocks (blocks of source code text) and have white space instead, for a clearer, less busy appearance. It’s a versatile language that runs on many systems, which brings us to…"))
