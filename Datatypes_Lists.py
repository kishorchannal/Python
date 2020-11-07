"""
Data Types
5. Lists
    1.  Properties
         ordered, can be heterogeneous 
    2.  Creation of List:(1)
        [], list() constructor, list comprehension => elegant way of creating list based on existing list,
        muliti dimensional lists
    3.  extend() and append(): (2)
    4.  Indexing:(3)
         normal indexing and reverse indexing
    5.  Slicing:(4)
         reverse list using slice operator(5) 
    6.  Shallow copy vs Deep copy(6)
    7.  Iterate list(7)
         for in, enumerate(), range()
    8.  Adding elements to list:(8)
         =, insert()
    9.  Removing elements from list:(9)
         del, remove(), pop(), slice operator
    10. Searching in list:(10)
         in, index(), max() min()
    11. Sorting a list:(11)
         sort(), sorted(), 
    
"""
#1
teams = ["India","Germany","Norway",10,"14.4"] #Heterogeneous
print(teams)

colors = list() # empty list
print(len(colors))
colors = list(["red",["yellow","green"],0,1]) 
print(colors)

print()
print("using list comprehension")
human_letters = [element for element in "human"] #here "human" is a String, it can be tuple as well
print(human_letters, type(human_letters))

list_of_countries = ["India","USA","Germany","Brazil"]
first_letters_of_country = [element[0] for element in list_of_countries]
print(first_letters_of_country)

print([x+y for x in 'abc' for y in 'xyz'])
print([x+y for x in 'abc' for y in 'xyz' if x!='a'])

print()
print("multi dimesnional lists")

simple_2D_list = [["a","b","c"],[1,2,3],[12.1,23.2,34.3]]
print(simple_2D_list)

for i in range(len(simple_2D_list)):
    for j in range(len(simple_2D_list[i])):
        print(simple_2D_list[i][j], end=" ")

simple_2D_list[0][0] = 'X'
print("\n",simple_2D_list)


#2
print("\n extending and appending list")
l1 = [10,20,30]
l2 = ['a','b','c']
l3 = l1 + l2
print(l3)

la1 = ['a','b']
la2 = [10,20]
la2.extend(la1) #adds elements of lists to calling list
print(la2)

la3 = [14.2,13,9]
la3.append(la2) #adds list itself as a element of calling list
print(la3)


#
print("\n Indexing")

lb1 = ['a','e','i','o','u']
print("first element of list:{0} is {1}".format(lb1,lb1[0]))

lb2 = ['b','c','d','f','g']
lb3 = [lb1,lb2]
print("lb3",lb3)
print(lb3[0][0])
print(lb3[1][3])

print(lb3[-1][0])
print("0th index to last",lb1[:len(lb1)])
print("start index to last",lb1[:]) #or use simply []

#5
print("\n reversing list using slice operator")
lc1 = [1,2,3,4,5]
print("reverse and hop by 1",lc1[::-1])
print("reverse and hop by 2",lc1[::-2])

#6
import copy
print()
ld1 = [1,2,[3,4,5],6,7] #here only 2nd element is subscriptable
print(ld1,id(ld1))
ld2 = ld1 # by default shallow copy happens
print(ld2,id(ld1))

print(ld2[2][0])
ld2[2][0] = 10

print(id(ld2)) #same as ld1 even after changing

print(ld1[2][0]) # prints 10

ld3 = copy.deepcopy(ld1)
ld3[2][0] = 20
print(ld1[2][0], id(ld3)) # remains 10 as ld3 is different object with same values of ld1


#7
print("\n Iterating over list")
le1 = [10,23,18.4,"Brazil"]

for element in le1:
    print(element,end=" ")

for index,element in enumerate(le1):
    print(index,element)

print()
for index in range(len(le1)):
    print(index,le1[index])

    
#8
lf1 = [23,"Black",14,3,21,8,5,6.2,[13,13]]
print(lf1)
lf1[0] = 32
print(lf1)
lf1[1:5] = ["Green",41,22,4,10] #inserting multiple items
print(lf1)

lf1.insert(0,43)
print(lf1)


#9
print("\n Deleting items from list")
lg1 = [10,23,18,9,[16,8]]
print("list is",lg1)

del lg1[0]
print(lg1)
del lg1[1:2]
print(lg1)
del lg1 # deletes entier list
#print(lg1)

lg2 = [10,20,30,40]
lg2.remove(10) #takes object as parameter
print(lg2)

lg3 = ['a','e','i','o','u']
print("list",lg3)
lg3.pop() #takes index as parameter and if not given pops out last element
print(lg3)

lg4 = [15,25,"Thirty five",45,0.5]
lg4[:] = [] #removes range of elements
print(lg4) 

#10
lh1 = [500,1024,1500,2024]

print(500 in lh1)

print(lh1.index(2024))

print("minimum:{0} maximum:{1}".format(min(lh1),max(lh1)))

#11.
li1 = [43,9,7,3,9,5,9,42,4]

li1.sort()
print(li1)

li1.sort(reverse=True)
print(li1)

li2 = sorted(li1)
print("list1",li1,id(li1))
print("list2",li2,id(li2))
