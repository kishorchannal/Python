"""
Data Types
1. Boolean:
        1. Have two values True/False
        2. These values are 1/0 or None or Empty data, we can see this during arithmetic operations(1)
        3. We can skip explicit comparison for boolean conditions(2)
2. Numbers:
        Types(3)
        1. integer: no size limit, 
        2. float: precesion upto 15 decimal points
        3. complex: 
3. Bytes:(4)
        1. machine readable form, hence no encoding is needed before storing on disk 
        2. immutable 
        3. range of bytes 0 to 255
        
"""
#1
x = True + 1
print(x)
y = False + 0
print(y)

a = 10
print(a==10)

#2 
photon = True
if photon == True:
    print("Electricity")
else:
    print("No Electricity")

if photon:
    print("Electricity")
else:
    print("No Electricity")

#3
num1 = 10
num2 = 3.4
num3 = 7+2j #or use complex(7,2)

print("number",num1,"is of class",type(num1),"instance of integer",isinstance(num1,int))
print("number",num2,"is of class",type(num2),"instance of float",isinstance(num2,float))
print("number",num3,"is of class",type(num3),"instance of complex",isinstance(num3,complex))


#4
empty_object = bytes(4)
print(type(empty_object),empty_object)
