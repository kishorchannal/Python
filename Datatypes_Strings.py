"""
Data Types
4. Strings:
        1.  single quotes or double quotes can be used to declare String or triple quotes for multi line String(1)
        2.  immutable(2)
        3.  Python 3 string are Unicode
        4.  Iterating: (7)
             Normal with in keyword and using [start:end:step]
             Using range()
             Using enumerate object
             Using reversed()
         
        5.  Slicing [] (3)
        6.  .replace() replace word in string (4)
        7.  del() (5)
        8.  String Operations (6):
             Concatenation + 
             Repitition *
             Membership in and not in
            Raw string with \r and Escape characters with \""
        9.  Format characters (8) using .format() and %()
        10. Built in Functions:(9)
             capitalize() lower() upper() swapcase() title() 
             count(substring,start,end): count the frequency of substring in range
        11. Comparison Functions(10)
             islower() isupper() isdecimal() isnumeric() isdigit() isalpha() isalnum()
        12. Padding Functions(11):
             rjust() ljust() center() zfill(width) 
        13. Search Functions(12):
             find() index() rfind() count() 
        14. Substitution Functions:(13)
             replace() split() join()
             
            
"""

#1
multi_line_string = """This is 
a multi line
String
"""
print(multi_line_string)

#2
str = "John"
print(id(str))
#str[0] = "K" throws are as we are trying to change the state of String after creating it i.e they are immutable
print(str[0])

#3
print()
name = "neymar"
print("full name:",name)
print("First 3 characters of name:",name[0:3]) #Here 3 is not included
print("Substring from 3 to 5:",name[2:5])
print("Substing from 3 to end:",name[2:])
print("last character",name[-1])
print("last three characters",name[-3:])
print("two characters before last",name[-3:-1])


#4
print()
line = "This is beautiful"
print(line,"location:",id(line))

line = line.replace("beautiful","ugly") 
print(line,"location:",id(line)) #this creates a new object and there replacement is happening

#5
print()
sample_str = "Python Scripting"
# del sample_str[0] cannot be done as Strings are immutable 

del sample_str
#print(sample_str) # throws error as the object no longer exists 

#6
print()
word1 = "Hello"
word2 = " there"
word3 = word1+word2
print("after concatination:",word3) 

print()
print("repetition: ",word1*3)

print()
string_membership = "abc"
print("Is x present in abc:", 'x' in string_membership)
print("Is x not present in abc:", 'x' not in string_membership)

print() # here raw string ignore all escape characters in the string and \ is used to ignore same in paticular word
print(" this is \"not\"  \n new line")
print(r"this is not  \n new line")


#7
print()
str_itr = "sky is blue"

for element in str_itr:
    print(element,end=' ') # end parameter is by default \n

print()
for element in str_itr[0:len(str_itr):2]: #stepping on every 2nd element only
    print(element, end=' ')

print()
for element in range(0, len(str_itr)):
    print(str_itr[element])

print()
for v,i in enumerate(str_itr): #here v is enumerate object and i is string element
    print(i,v)
    
print()
for element in reversed(range(0, len(str_itr))):
    print(str_itr[element],end='')


#8
print()
employee_name = "Ashish"
employee_age = 25
print("Name {0} Age {1}".format(employee_name,employee_age))
print("%i %s cost %.2f rupees" %(6,"bananas",1.74))

#9 
print()
str_example = "welcome To Python Programming"
print(str_example.capitalize())
print(str_example.lower())
print(str_example.upper())
print(str_example.swapcase())
print(str_example.title())
substring = 'o'
print("string is:{0}, length of string:{1} and substring is:{2}".format(str_example,len(str_example), substring))
frequency = str_example.count(substring,0,len(str_example))
print("frequency of \'o\' is:",frequency)


#10
print()
print("Python".islower())
print("Python".isupper())
print(u'2016'.isdecimal()) #applies for unicode data only
print(u'2016'.isnumeric()) #applies for unicode data only
print("203".isdigit())
print("pyth0n".isalpha())
print("pyth0n".isalnum())

#11
print()
str2 = "Argentina"
print(str2, len(str2))

print(str2.rjust(10,'-'))
print(str2.ljust(10,'-'))
print(str2.center(11,'-'))
print(str2.zfill(10)) #pads with 0 on the left


#12
print()
str3 = "This is Python"
substring3 = "is"

#prints -1 if substring not present
print(str3.find(substring3)) #gives first starting index of substing, here 'is' is already found in 'This'
print(str3.find(substring3,4,len(str3)))

#raises 'ValueError' if substring not present
#print(str3.index("x"))

print(str3.rfind(substring3))

#count() is covered above

#13 
print()
str4 = "aaabcccdeee"
print(str4.replace('a','x')) #replaces all occurances of 'a' with 'x'
print(str4.replace('e','x',1)) # replaces count number of times from left

str5 = "this string:should, split"
print(str5)
print(str5.split()) #splits spaces
print(str5.split(','))
print(str5.split(':'))

seq = ("this", "is", "not", "string")
str_to_join_with = "="
print(str_to_join_with.join(seq)) #output is a String
print(str_to_join_with.join(seq)) #output is a String