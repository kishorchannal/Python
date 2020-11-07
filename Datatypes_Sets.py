"""
Data Type
7. Set
    1.  Properties
         mutable but its elements are immutable,unique elements, unordered, heterogeneus
    2.  Creation of Set:(1) 
         {}, set(), set cannot have mutable objets such as List,Set,Dictionary
         Creating emoty Set (3)
    3.  Adding elements to Set:(4)
         update() add()
    4.  Remove elements from Set:(5)
         remove() discard() pop() this method is random as no ordering, clear() this method flush everything
    5.  Set Operations:(6)
         union        | combines two sets
         intersection & common elements
         difference   - setA elements not in setB
         compliment   ^ Only comman elemnts are removed
    6.  Iterate Set(7)
         for in, enumerate(), range() 
    7.  Searching:(8)
         in, index(), max(), min()
    8.  Frozen Set
         In this set we cannot add() or update()
"""
#1
sa1 = {2,4,6,6} #even though 6 is repeated, it does not reflect inside set
print(sa1,type(sa1))

sa2 = set([13,11,68,"xyz","xyz"])
print(sa2,type(sa2))

sa3 = {} # empty {} is dictionary and not Set
print(sa3,type(sa3)) 

sa4 = set()
print(sa4,type(sa4)) 


#4
print("\n Adding elements to the Set")
sb1 = {2,1,"Grey"}
print(sb1)

#print(sb1[0]) #as Set is unordered, throws error: 'set' object is not subscriptable

sb1.update([10,20,30]) # we know mutable objects cannot be part of set, here elements of list are getting added
print(sb1)

sb1.add(40) #with add() we can only add one element at a time
print(sb1)
    
#5
print("\n Removing elements from Set")
sc1 = {10,100,1000,20,200,2000}
print("set:",sc1)
sc1.discard(300) # dosent throw error
#sc1.remove(300) #throws error: KeyError

sc1.discard(100)
print("after discarding 100 from set:",sc1)
sc1.remove(200)
print("after removing 200 from set:",sc1)


sc2 = {1,11,111,2,22,222}
print("\n set:",sc2)
sc2.pop()
print("after removing random element from set:",sc2)

sc2.clear()
print("After clearing set:",sc2)

#6
setA = {10, 20, 30, 40, 50, 'g', 'h'}
setB = {10, 20, 'z', 40, 50, 'b', 't'}

print("union",setA|setB)
print("union again",setA.union(setB))


print("intersection",setA&setB)
print("intersection again",setA.intersection(setB))

print("difference",setA-setB)
print("difference again",setA.difference(setB))

print("symmetricdifference",setA^setB)
print("symmetric difference again",setA.symmetric_difference(setB))

#7
print("\n Iterate Sets")
se1 = {42,11,"Free","pin",22.22}
print("set",se1)

for element in se1:
    print(element,end=" ")

for index,element in enumerate(se1):
    print(index,element)

for index in range(len(se1)):
    print(index) #since Set is unordered we cannot use se1[index]
    
#8
print("\n searching in Set")
sf1 = {10,12,14,16,18}

print(16 in sf1)

#print(sf1.index(18)) # throws error as Set is unordered

print("min ",min(sf1),"max ",max(sf1))

#8
sg1 = frozenset(['I','am','Batman'])
#sg1[2].add("Hero") #throws error
#sg1[2].update("Hero") #throws error
