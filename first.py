#print('hello world')

'''import keyword
print(keyword.kwlist)'''


'''print('My name is Neha Pandey')
print('I am a BCA student')
int a=25'''
'''print('apple')
print('orange')
print('watermelon')'''

'''name='neha'
num=123
print(num)
print(name)
number=[4,3,10,9,6,18,7]
largest=max(number)
print('The largest number in the list is' largest)'''
'''a=3
b=5
# and operator
print(a>2 and b>4) #true (both conditions are true)

# or operator
print(a>5 or b>2)  # True (second condition is true)

# not operator
print(not(a>b)) # True(because a>b is false)
'''
#Print even numbers between 1 and 20
for i in range(2,21,2): #start be 2, stop be 21 and step  be 2.
    print(i)
    #relational operator
age = 18
income = 50000

# Using relational operators
print(age > 16)          # True
print(income < 30000)    # False

# Using logical operators
print((age > 18) and (income > 30000))   # True
print((age < 18) or (income > 30000))    # True

# Sample list
numbers = [10, 20, 30, 40, 50]

# Method 1: Using sum() function
total = sum(numbers)
print("Sum of all elements:", total)

# Method 2: Using a for loop
total_loop = 0
for num in numbers:
    total_loop += num
print("Sum using loop:", total_loop)

# Sample list with duplicates
numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# Method 1: Using set (removes duplicates, order not guaranteed)
unique_numbers = list(set(numbers))
print("Unique elements (using set):", unique_numbers)

# Method 2: Using a loop (preserves original order)
unique_numbers_ordered = []
for num in numbers:
    if num not in unique_numbers_ordered:
        unique_numbers_ordered.append(num)
print("Unique elements (preserving order):", unique_numbers_ordered)

# Sample list
numbers = [10, 20, 4, 45, 99, 20]

# Method 1: Using sort
numbers.sort()  # Sorts the list in ascending order
second_largest = numbers[-2]  # Second last element
print("Second largest number (using sort):", second_largest)

# Method 2: Without sorting
largest = second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number (without sorting):", second_largest)

# Sample list
numbers = [1, 2, 3, 4, 5]

# Method 1: Using reverse() method (in-place)
numbers.reverse()
print("Reversed list (using reverse()):", numbers)

# Method 2: Using slicing (creates a new reversed list)
numbers = [1, 2, 3, 4, 5]  # original list
reversed_list = numbers[::-1]
print("Reversed list (using slicing):", reversed_list)

# Method 3: Using reversed() function (returns an iterator)
numbers = [1, 2, 3, 4, 5]
reversed_list2 = list(reversed(numbers))
print("Reversed list (using reversed()):", reversed_list2)

# Sample list
numbers = [5, 2, 9, 1, 7]

# Method 1: Using sort() method (in-place)
numbers.sort()
print("Sorted list (using sort()):", numbers)

# Method 2: Using sorted() function (returns a new sorted list)
numbers = [5, 2, 9, 1, 7]  # original list
sorted_list = sorted(numbers)
print("Sorted list (using sorted()):", sorted_list)

#set
data={10,20,20,30,40,40,40,30,"python"}
print(type(data))
print(data)
empty={}
print(type(empty))
#raw string
a=r"Python\nis a programming language."
print(a)
#list is immutable
data=[10,20,30]
fruits=['apple','banana','orange']
fruits[1]='mango'
print(fruits)
#tupple 


#range
rg=range(20,10,-4)
print( list(rg))
#Aithmetic Operation
a=21
b=10
if(a==b):
    print('a is equal to b')
else:
    print('a is not equal to b')

if(a!=b):
 print('a is not eqaul to b')
else:
 print("a is equal to b")
x=40
if(x>18 and x<35):
 print("person is adult")
else:
 print('person is not adult')
 #for OR operation
#  if (x>18 or x<35):
 #Not operator
 #Bitwise Operator
 p=20
 q=10
 print(p & q)
 print(p ^ q)
 print(p | q)
 print(p >> q)
 print(p << q)
 num_int=123
 num_str="123"
 num_float=245.66
 num_str=int(num_str)
 num_int=float(num_int)
 print("Data types of num_str after type casting",type(num_str) )
 print("Data type of num ")
 num_sum=num_int +num_str
 num_sum_float=num_int+num_float
 print("sum of the string and integer ", num_sum)
 print("Data type of the sum",type( num_sum))
 print("sum of the integer and float",num_sum_float)
 print("the data types of ",type(num_sum_float))

 #Task
 a="Softwarlca College"
 print(a.istitle())
 a="PYTHON"
 print(a.isupper())
 a="capital"
 print("A".isupper())
 a="capital"
 #print(a.capitalize("c"))  thah xaina kinna error aayo
 a="+Capital9"
 print(a.count("9"))
 a="+Cap9ital9"
 print(a.find("9"))
 a="+Cap9ital9"
 print(a.rfind("9"))
 a="Cap9ital9"
 #print(a.index("A"))  thah xain kinna error aayo
 a="python"
 print(a.swapcase())
 a="123abc"
 print(a.rjust(11,"#"))
 a="123abc"
 print(a.ljust(11,"#"))
 a="123abc"
 print(a.ljust(7,"#"))
 a="123abc"
 print(a.replace('w',"1"))

 a="123abc"
 b=a.count("1")
 print(b)

 a="123abc"
 b=a.maketrans("abc","abc")
 print(b)
 
 a="123abc"
 b=a.maketrans("Ab","Ab")
 print(b)

 a="123abc"
 print(a.replace('a',"1"))

 #task for the operators
 a=101
 print(~a)
 a=117
 print(~a)
 print(30 >> 2)

 #print("python",sep='/',"programming")

 a='pyt'' hon'
 print('pt'in a)

 a=20
 b=34
 a=a^b
 b=a^b
 a=a^b
 print(a,b)

 a=1,2,3
 print(type(a))
 b=2j
 #print(a.real,a.imag) error arrise

 a=10
 b=20
 print(f'{10*b}')
 
#print('{} {c} {}'.format(b,c=10,a)) error shown in this line

a=10
b=20
#print('{b}'.format(b,a)) error shown

a=10
b=20
#print('{0} {}'.format(b,a))   ValueError: cannot switch from manual field specification to automatic field numbering

a='Expression'
print(a[::2])
print(a[:])
print(a[-2:3:-1])
print(a[-3:4])
print(a[0:-1])
print(a[-3:-4:-1])
print(a[-3:7:-2])
print(a[1:-8])
print(a[9::-10])
print(a[9:-10:-1])
print(a[11::-6])
print(a[2:-15:-1])
print(a[-15::-2])
print(a[7:-1])
print(a[-1:0:])
print(a[:-1:])
print(a[::-1])
print(a[-1:7])
print(a[:-3:])
print(a[-1:0])
print(a[-1:0:-1])
range=(5,15)
print(10 not in range)
name="neha"
print(f"Hello, {name}!")
value=5
print(f"{value*value}")






 
 
    

          



