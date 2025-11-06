# Aithmetic operators
a=10
b=5
print(a*b)
print(a+b)
print(a-b)
print(a/b)
print(a%b)
# Logical operators
age=40
if(age>=35 and age>18):
    print("The person is adult")
else:
    print("Not adult")
if(age>=18 or age<18):
    print("Aggible to vote")
else:
    print("not egible to vote")

x=False
y=True
print(not x)
print(not y)    

#Relational Operators
name="Neha"
if(name=="Neha"):
    print('Hello Neha')
else:
    print("Hello Shashwat")

a="apple"
b="banana"
c="apple"
print(a==b)
print(a==a)
print(a!=b)
print(a!=c)
print(a==c)
print(a<b)
print(b>a)

#Ternary Operator
marks = 30
status = "Pass" if marks >= 24 else "Fail"
print(status)

#Bitwise Operators
a = 10   # (binary: 1010)
b = 4    # (binary: 0100)

print("a & b =", a & b)   # AND  → 0b1010 & 0b0100 = 0b0000 → 0
print("a | b =", a | b)   # OR   → 0b1010 | 0b0100 = 0b1110 → 14
print("a ^ b =", a ^ b)   # XOR  → 0b1010 ^ 0b0100 = 0b1110 → 14
print("~a =", ~a)         # NOT  → inverts all bits → -11
print("a << 1 =", a << 1) # Left shift → 1010 → 10100 → 20
print("a >> 1 =", a >> 1) # Right shift → 1010 → 0101 → 5


 

