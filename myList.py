#코딩 문제 내면 좋을듯
#myList 숫자 중 어떤 값들이 남는가?
myList = [1,45,17,31,26,12]


print("==============================")

for i in range(0, len(myList)):
    print(str(i) + ":" + str((myList)))

    if i%2 == 0 :
        myList.sort()
    else :
        myList.reverse()

    myList.pop(len(myList)-1)

print("==============================")

iText = {'name':'Amadeus', 'number':'1406'}
print("my name is " + iText['name'])
print("my number is " + iText['number'])
