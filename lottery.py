import random

myRandom = random
myList = []
chkVal = 0

for i in range(0,6) :
    myList.append(myRandom.randint(0,45))

print(myList)
myList.sort()

print("==================================")
#myList = [1,1,1,2,2,2]

i = 0
while i < len(myList) :
    if i > 0 and chkVal == myList[i] :
        myList.append(myRandom.randint(myList[i],45))
        myList.pop(i)
        myList.sort()
        i = 0

    chkVal = myList[i]
    i = i+1

print(myList)
