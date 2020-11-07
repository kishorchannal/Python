"""
Functions
    1. use def to create function(1)
    2. nested functions(2) or inner functions
    3. def within conditional statements(3)
    4. Polymorphism(4) -> its default as types are for values not variables
    5. Pass by value -> pass immutable, Pass by reference -> pass mutable(5)
        retain value of mutable object after passing them(6)
    6. Arguments(7)
        1.Keyword    (8)
        3.Default    (9)
        4.Arbitrary  (10) -> passing any number of arguments
    7. Scope of Variables:(11) LEGB rule(11), class enclosing is a exception(12)
    8. Return values:(13) returning multiple values act as 'call by reference'
    9. Functions are first class
"""

#1
def printSample():
    print("printing")
    
printSample()
#isElgible()

#2
def nestOne():
    """__"""
    print("This is nestOne")
    def nestTwo():
        print("This is nestTwo, but calling from nestOne")
    nestTwo()

nestOne()    

#3
def checkEvenOdd(number):
    if (number % 2 == 0):
        def message():
            print("number is Even")
    else:
        def message():
            print("number is Odd")
    message()

checkEvenOdd(21)    
    
#4
def printName(word):
    message = word + " Hello!"
    print(message)
    
printName("Drake")
#printName(50) #throws error


#5
print()
a = 10
b = ["apple",50]

print(a,id(a))
print(b, id(b))

def changeValue(arg1, arg2):
    print("inside function, before changing",arg1,id(arg1))
    print("inside function, before changing",arg2,id(arg2))
    
    arg1 = 20
    arg2[0] = "Mango"
    
    print("inside function, after changing",arg1,id(arg1))
    print("inside function, after changing",arg2,id(arg2))

changeValue(a,b)

print()
print(a,id(a))
print(b, id(b))

#6
print()
a = 10
b = [12,"star"]

def changeValues(agr1, arg2):
    arg1 = 20
    arg2[1] = "moon"

#changeValues(a,b) #this will change mutable object 
#print(a,b) 

changeValues(a,b[:]) #create a explicit copy of mutable object
print(a,b)

#7
print()
a = 10
b = 20

def printValue(val1, val2):
    print(val1, val2)

printValue(a,b)

#8
print()
a = 70
b = 30

def sub(valueOne,valueTwo):
    print(valueOne - valueTwo)
    
sub(a,b)
sub(valueOne=b, valueTwo=a) #using functions parameters to pass arguments

#9
print()
color1 = "Blue"
color2 = "Purple"

def printColors(c1,c2="No color"):
    print(c1,c2)

printColors(color1, color2)
printColors(color1)

#10
print()

def manyValues(*value):
    print("manyValues")
    print(type(value))
    for v in value:
        print(v, end=" ")
        
manyValues(10,20,30,40,"car")
   
#11
print()
 
a = "globalA"
b = "globalB"
c = "globalC"
def samp():
    a = "enclosingA"
    def samp2():
        b = "localB"
        print(a + b+ c)
    samp2()

print(a)
samp()


#12
#to be done


#13
a = 'a'
b = 'b'
def returnSample(par1, par2):
    par1 = "c"
    par2 = "d"
    
    return par1,par2

print("before calling",a,type(a),b,type(b))
a,b = returnSample(a,b)
print("after calling",a,type(a),b,type(b))

    
    