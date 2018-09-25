import os

myText = "Hello world"

print(myText)
print(myText.upper())
print(len(myText))

def search(dirname) :
    filenames = os.listdir(dirname)
    for filename in filenames :
        full_filename = os.path.join(dirname, filename)
        print (full_filename)
        # print("Hello world")

search("c:/")
