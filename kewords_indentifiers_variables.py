"""
1. Keywords: 
             Reserved words
             >>>import keyword
             >>>keyword.iskeyword("None")
2. Identifier: 
               Cannot use special character
               Avoid using _ as leading or trailing character
               Use Capital letter when identifying class
3. Variables: 
              Entity whose value can be changed
              Label assigned to memory chunk
              When variable value changes, new memory chunk is alloted to it (1)
              Object has a type not variable (2)
"""
#(1)
#id() gives memory address
x = 10
print(id(x)) 

x = 11
print(id(x))


#(2)
y = 15.5
print(type(y))

y = "some string"
print(type(y))