#!/usr/bin/python3

myList = ['Item0', 'Item1', 'Item2', 'Item4']

listLength = (len(myList))

print(listLength) #                                                 4

print(myList[-1]) #                                                 Item4

print (myList[listLength - 1]) # Likt som over                      Item4

# [startIndex:stopIndex] inclusive:exclusive

print(myList[2:]) # Fra index 2 til enden av listen                 ['Item2', 'Item4']
print(myList[:2]) # Fra starten av listen (index 0) til index 2     ['Item0', 'Item1']

# Adde item til slutten av liste - append
myList.append('Item5')

# Sette inn objekt i liste på en spesifikk index
myList.insert(3, 'Item3')

print (myList) #                                                    ['Item0', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5']

mySecondList = ['Value0', 'Value1']

#myList.insert(-1, mySecondList) #                                   
#print (myList) #                                                   ['Item0', 'Item1', 'Item2', 'Item3', 'Item4', ['Value0', 'Value1'], 'Item5']
listLength = (len(myList))
#myList.insert(listLength - 1, mySecondList) # Samme output som over
print (myList)
myList.insert(listLength, mySecondList)
print (myList) # Der ble det riktig                                 ['Item0', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5', ['Value0', 'Value1']]

# MyList index 5 er nå mySecondList

myList.remove(myList[listLength])
myList.extend(mySecondList)
print (myList) # Verdiene fra mySecondList lagt til myList          ['Item0', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Value0', 'Value1']
