"""
Operators
    1. Arithmetic:(1)   + - * / // % **
    2. Comparison:(2)   > < == != >= <=
    3. Logical:(3)      and or -> return one of operands   not -> gives real boolean output 
    4. Bitwise:(4)      & | ~ ^ >> <<
    5. Assignment:(5)   = += -= *= /= %= **=    &= |= ^= >>= <<=  
    6. Identify:(6)     is, is not   -> should refer to same object
    7. Membership:(7)   in, no it 
    
    8. Operator Precedence(8): only ** gets evaluated right to left
        * / %     -->   +- 
    
"""
import copy
#1

print(2 + 7)
print(2 - 7)
print(2 * 7)
print(7 / 2)
print(7 // 2) #Floor division
print(7 % 2) 
print(7 ** 2) #Exponent operator

#2

print(3 > 10)
print(3 < 10)
print(10 >= 10)
print(3 <= 10)
print(3 != 10)

#3

print(13 and 4)
print(13 or 4)

a = True
b = not a
print(a,b)


#4
print()
print(3 & 2)
print(1 | 3)
print(~4) #
print(64 >> 2) #dividing number by 2**x x=bits mentioned
print(8 << 2) #multiplying number by 2**x x=bits mentioned


#5
print()
a = 10

a += 20
print(a)

a -= 20
print(a)

b = 7
b &=1
print(b)


#6
print
num1 = 20
print(num1,id(num1))

num2 = num1
print(num2,id(num2))
print(num1 is num2)

#7
print()
employee = {"name":"John", "age":24}
print("name" in employee) #here in searches key field

name = "Alex"
print("x" not in name)


#8
print()
print(4+2*6/2)



