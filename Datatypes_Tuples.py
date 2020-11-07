"""
Data Type
6. Tuple
    1.  Properties
         immutable (2), orderd, can hold heterogeneous elements
    2.  Creation of Tuple: (1)
         using (), without using (), tuple()
        Creating tuple of size 1 (3)
    3.  Indexing:(4)
    4.  SlicingL (5)
    5.  Change values of tuple:(6) by modifying tuples inside them
    6.  String Operations (7):
         Concatenation + 
         Repitition *
    7.  Removing elements from list:(8)
          delete list item inside tuple, del keyword to delete entire tuple
    8.  Searching:(9)
         in, index(), max(), min()
    7.  Iterate tuple(10)
         for in, enumerate(), range()
    8.  Tuple Assignment
    9.  Using tuples as functions return value
"""
#1
ta1 = () #blank tuple
print(ta1)

ta2 = 32, "green", 17.1
print("tuple:",ta2,type(ta2)) #by default data type of sequence elements is tuple

ta3 = 21, [8,4,2], "Black", ("yellow", 70)
print(ta3, type(ta3))

ta4 = tuple({100,8,4,2}) #creating tuple from set and set is unordered
print(ta4, type(ta4))

ta5 = tuple([100,8,4,2]) #creating tuple from list
print(ta5, type(ta5))

#2
tb1 = (10,20,"Sheep")
print(tb1[0])
#tb1[0] = 30 # throws error : 'tuple' object does not support item assignment



#3
tc1 = (10) #it is supposed to be of type tuple but its int
print(tc1,type(tc1))

tc2 = (10,) # after placing , it is recognozed as tuple
print(tc2,type(tc2))

tc3 = tuple({"single"}) # creating tuple of size 1 from set
print(tc3,type(tc3))

tc4 = tuple(["single"])  # creating tuple of size 1 from list
print(tc3,type(tc4))


#4
print("\n Indexing")
td1 = ('a','e','i','0','u')
print(td1)

print(td1[0])
print(td1[len(td1)-1:])

td2 = ((10,20,30),('a','b','c'))
print(td2)

print(td2[-1]) #reverse indexing

#5
te1 = ("H",'e',"60","42.8")
print(te1[0:-2]) #end is always excluded


#6
print("\n changing the elements of tuple")
tf1 = (10,20,30,["Green",17.1],50)
print("tuple",tf1)

tf1[3][0] = "Black" #since [3][0] is a list item, we can modify them
print("tuple after modufying",tf1)

#7
tg1 = (10,)
tg2 = ("Ship",)
tg3 = tg1 + tg2
print(tg3,type(tg3))

tg4 = tg1 * 4
print(tg4)

#8
print()
th1 = (14,[24,34],44)
#del th1([1][0]) not possible

del th1
#print(th1) #throws error

#9
ti1 = (10,100,20,200)
print(10 in ti1)

print(ti1.index(100))

print("max:",max(ti1),"min:",min(ti1))

#10
print("\n iterating tuple")
tj1 = ("11",11,"12",12,"twelve")

for element in tj1:
    print(element,end=" ")

for index,element in enumerate(tj1):
    print(index,element)
    
for index in range(3): #iterate over 3 elements
    print(tj1[index],end=" ")

#11
print()
emp_records = ('john', 'hr', 2010, 'robert', 'account', 2015, 'bill', 'mis', 2018)
(emp_name, emp_dept, emp_join_date) = emp_records[0:3]

print(emp_records,type(emp_records))
print(emp_name)
print(emp_dept)
print(emp_join_date)

#12
def squareOfTwo(n1, n2):
    return (n1*n1, n2*n2)

print(type(squareOfTwo(2,3)))