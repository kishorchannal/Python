"""
Data Type
8. Dictionary
    1. Propery
        mutable,holds K:V, keys are unique, key must be always immutable type i.e number, string, tuple
        Uordered but dictionary elemnts are accessed by keys anyway
    2. Creation of Dictionary: #1
        {}, dict()
    3. Accessing elements:(2)
        [key], get()
    3.  Adding elements to Dictinary:(3)
         update()
    4.  Removing elements from Dictionary:(4)
         pop(key) random_item = d.popitem(), clear()
    5.  Iterate Dictionary(5)
         for in,
    6.  Dictionary Comprehension
    7.  Search
         
         
        
"""
#1
da1 = {}
print(da1, type(da1))

da2 = {1:"One",2:"Two"}
print(da2)

da3 = {"class":"senior secondary",1:[1,2,3,4]} #using differet data types for Keys and Values
print(da3)

da4 = dict({18:"modifed",9:"no modified"})
print(da4,type(da4))


#2
db1 = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print(db1['Student Name'])

#print(db1['Student Height']) #throws KeyError if key is not present in dictionary

print(db1.get('Student Name'))
print(db1.get('Student Height')) #dosent throw error, instead shows None


#3
dc1 = {"1" : "Python", "2" : "Java"}
print(dc1)
dc1["key"]="value" #appends new value to Dictionary
print("after appending",dc1)

dc1["1"]="c#" #it overwrites value of same key already present
print("after appending new item whose key was already present",dc1)


dc1.update({4:"JavaScript"})
print("After updating",dc1)

#4
dc2 = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}
dc2.pop(2)
print("after removing key:2",dc2)

print("random pair removed",dc2.popitem())
print(dc2)

dc2.clear()
print(dc2)

#5
print()
dd1 = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
for k in dd1:
    print(k,end=" ")

print()
for k,v in dd1.items():
    print(k,v)
    