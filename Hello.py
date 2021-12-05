import os

myText = "Hello world, 하이 한글"

print(myText)
print(myText.upper())
print(len(myText))

# 아래 코드는 맥에서는 동작하지 않음
# def search(dirname) :
#     filenames = os.listdir(dirname)
#     for filename in filenames :
#         full_filename = os.path.join(dirname, filename)
#         print (full_filename)
# find("/Users/markb./")

print(os.getcwd())
print(os.listdir(os.getcwd()))