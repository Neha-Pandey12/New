'''name="neha"
for i in name:
    print(i)

for i in range(5,25,5):
    print(f"Hello World {i}")
print("Loop Ended")

a=[10,40,"Neha",50.5]
for item in a:
    print(item, end=" ",)

st="Python"
n=len(st)
for i in range(n):
    print(i, "=", st[i])
st="neha"
for i in st:
    print(i)
else:
    print("Loop Completed")

for i in range(2):
    print("oter loop",i)
    for j in range(3):
        #name="neha"
        name= input("Enter your name: ")
        print(f"inner loop print {name}",j)
print("Loop Ended")

i=0
while i<10:
    #print("Hello World")'''
#Nested loop
''''=1
while i<=3:
    print("Outer Loop",i)
    i=i+1
    j=1
    while j<=5:
        print("  Inner Loop",j)
        j+=1
    print("Inner Loop Ended")
print("Loop Ended")

num=int(input("Enter a number: "))
while num<50:
    print("the number is", num)
    num=num+5
    num=int(input("Enter the second number: "))
    while num>100:
        print("the number is", num)
        num=num-10
        num=int(input("Enter the third number: "))
'''
'''i=1
while i<=10:
    if i==9:
        break
    print(i)
    i+=1
print("Loop Ended")
'''
#multiplication table of 5

colors=["Red","Green","Blue","Yellow"]
for i in colors:
    print(i)

data=list(range(1,11))

data.append(11)
data.append("neha")
data.insert(3,"hello")
print(data)

mix_list=[]

data1=["a","b","c"]
data2=["neha","hello",29,50.5]
data2.extend(data1)
print(data2)
#mix_list=data1+data2


for i in range(10):
    print("Display software 10 times")
    print("Software")
i=0
while i<10:
    print("Display software 10 times")
    print("Software")
    i+=1
'''list1=[10,20,30,40,50]
length=len(list1)
Sum=0
for i in range(length):
    Sum=Sum+list1[i]
print("Sum is:",Sum)
'''
list2=[10,20,30,40,50]
len2=len(list2)
Sum2=0
i=0
while i<len2:
    Sum2=Sum2+list2[i]
    i+=1
print("Sum is:",Sum2)
character="neha"
for i in range(len(character)):
    print(i, "=", character[i])

char="python"
i=0
while i<len(char):
    print(i, "=", char[i])
    i+=1
given_list=[1,"a","c",2,3,4]
print("Only Integer values from the list:")
for i in given_list:
    if type(i)==int:
        print(i)
my_list=[1,"a","c",2,3,4]
i=0
print("Only Integer values from the list:")
while i<len(my_list):
    if type(my_list[i])==int:
        print(my_list[i])
    i+=1    
#multiplication of each value in the list
num_list=[4,5,3,2]
for i in num_list:
    print(f"Multiplication of {i} is: ", i*5)

num_list2=[4,5,3,2]
i=0
while i<len(num_list2):
    print(f"Multiplication of {num_list2[i]} is: ", num_list2[i]*5)
    i+=1
#Multiplication table of given number
num=int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(f"{num} x {i} = ", num*i)

num2=int(input("Enter a number to print its multiplication table: "))
i=1
while i<=10:
    print(f"{num2} x {i} = ", num2*i)
    i+=1
#reverse a list using for loop
original_list=[1,2,3,4,5]
reversed_list=[]
for i in range(len(original_list)-1,-1,-1):
    reversed_list.append(original_list[i])
print("Reversed List is:", reversed_list)

#For loop which print hello plus each name in the list
a=["neha","shashwat",1,2]
for i in a:
    print("Hello!",str(i))

#While loop which print hello plus each name in the list
a=["neha","shashwat",1,2]
i=0
while i<len(a):
    print("Hello!", str(a[i]))
    i+=1
#using a for loop & append method append each item with prefix Dr to the list
a=["neha","shashwat","ram","sita"]
b=[]
for i in a:
    b.append("Dr. "+i)
print(b)
#removal of bad characters from the given string
given_bad_chars=[';',':','!',"*"]
string="py;th*o:n!;py*t*h:o!n"
for i in given_bad_chars:
    string=string.replace(i,"")
print("Cleaned String is:", string)

#for loop to  print sum of even numbers from 1 to 100
Sum=0
for i in range(1,101):
    if i%2==0:
        Sum=Sum+i
print("Sum of even numbers from 1 to 100 is:", Sum)

sum=0
for i in range(2,102):
    if i%2==1:
        sum=sum+i
print("Sum of odd numbers from 1 to 100 is:", sum)

#program to check given number is palidrom or not
num=int(input("Enter a number: "))
reverse_num=0
temp=num
while temp>0:
    digit=temp%10
    reverse_num=reverse_num*10+digit
    temp=temp//10
if num==reverse_num:
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")

#program to check given number is armstrong or not
num=int(input("Enter a number: "))
sum=0
temp=num
n=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp=temp//10
if num==sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#for loop that removes all vowels from the given string
givenstring="This is a sample string with vowels you need to remove"
vowels="aeiouAEIOU"
result=""
for i in givenstring:
    if i not in vowels:
        result=result+char
print("String after removing vowels:", result)

#program to determine whether a given number is prime or not
num=int(input("Enter a number: "))
is_prime=True
if num>1:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

#find common elements between two lists
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_elements=[]
for i in list1:
    if i in list2:
        common_elements.append(i)
print("Common elements between two lists are:", common_elements)


