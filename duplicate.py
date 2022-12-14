
lis = [1, 2, 1, 2, 9]
 

uniqueList = []

duplicateList = []
 

for i in lis:

    if i not in uniqueList:

        uniqueList.append(i)

    elif i not in duplicateList:

        duplicateList.append(i)
 

print(duplicateList)
