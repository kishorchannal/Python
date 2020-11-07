"""
1. Intserting (1): 
              Where python will allocate same memory address to variables in 2 cases
              1. String has no white spaces and <20 characters
              2. integers ranging between -5 and +255
              
2. Asigning new variable to existing variable (2): 
              Python assigns new variable to same memory location of existing variable

3. Multiline statement(3): 
              1. Explicit continuation using \
              2. Implicit continuation using () or {} or []
"""
#(1)
str1 = "string one"
print(id(str1))
str2 = "string two"
print(id(str2))

str3 = "fox"
print(id(str3))
str4 = "fox"
print(id(str4))

number1 = 100
print(id(number1))
number2 = 200
print(id(number2))

#(2)
variable1 = 100
print(id(variable1))
variable2 = variable1
print(id(variable2))


#(3)
factorial_3 = 3 * 2 \
              * 1
print(factorial_3)

factorial_5 = ( 5 * 4
               * 3 *
               2 * 1
)
print(factorial_5)
