'''a=int(input("Enter first number: "))
if a==100:
    print("a is 100")
else:
    print("a is not 100")

    b=int(input("Enter second number: "))
   "' if b>100:
        print("b is greater than 100")
    elif: 
        print("b is equal to 100")'''
#Password and user checking
'''age=int(input("Enter your age: "))
if(age<12):
    print("The ticket is free")

elif (age>=12 and age<=60):
    user=input("Do you have membership? yes/no: ")  
    if(user=="yes"):
        print("The ticket price is 150")
    else:
        print("The ticket price is 200")
else:
         print("The ticket price is 100")'''

#A utility company charges different rates based on electricity usage
'''usage=int(input("Enter your electricity usage : "))
if(usage<=100):
    amount=usage*5
    #print("The rate is 5 per unit")
elif(usage>100 and usage<=300):
    use=usage-100
    amount=use*8+ 100*5
    #print("the total amount of bill is",amount)
else:
    billuse=usage-300
    amount=100*5 + 200*8 + billuse*10
    #print("Your bill amount is ",amount)
print(f"The rate for {usage} units is :{amount} ")
'''
#Electricity bill Generator
'''print("**********Electricity Bill**********")
unit_consumed=int(input("Enter the units consumed: "))
if(unit_consumed<=100):
    bill_amount=unit_consumed*5
elif(unit_consumed>100 and unit_consumed<=200):
    bill_amount=100*5 + (unit_consumed-100)*8
elif(unit_consumed>200):
    bill_amount=100*5 + 100*8 + (unit_consumed-200)*10

#Checking for memebership discount
membership=input("Do you have a membership? yes/no: ")
if(membership=="yes"):
    discount=bill_amount*0.1
    bill_amount=bill_amount-discount
    print(f"Original Bill Amount: {bill_amount + discount}")
    print(f" Bill after Discount Applied: {discount}")
    print(f"Total Bill Amount: {bill_amount}")
else:
    print(f"Total Bill Amount: {bill_amount}")'''
 
#Resturant Bill with Discount
total_bill=int(input("Enter the ordered amount: ")) 
if(total_bill>1000):
    premium_member=input("Are you a premium member? yes/no: ")
    if(premium_member=="yes"):
        discount=total_bill*0.15
        final_bill=total_bill-discount
    else:
         discount=total_bill*0.1
         final_bill=total_bill-discount
    #print(f"Original Bill Amount: {total_bill}")
   # print(f"Discount Applied: {discount}")
   # print(f"Total Bill Amount: {final_bill}") 
else:
    if(total_bill>2000):
        premium_member=input("Are you a premium member? yes/no: ")
        if(premium_member=="yes"):
            discount=total_bill*0.2
            final_bill=total_bill-discount
        else:
         discount=total_bill*0.15
         final_bill=total_bill-discount
         print(f"original Bill Amount: {total_bill}, Discount Applied: {discount}, Total Bill Amount: {final_bill}")

#Movie Ticket Pricing
age=int(input("enter your age:"))
if(age<12):
    print("The ticket is free")
elif(age>=12 and age<=60):
    membership=input("Do you have membership? yes/no:")
    if(membership=="yes"):
        print("The ticket price is 150")
    else:
        print("The ticket price is 200")
else:
    print("The ticket price is 100")

#online shopping discount System
purchase_amount=int(input("Enter your purchase amount: "))
if(purchase_amount>5000):
    prime_member=input("Are you a prime member? yes/no: ")
    if(prime_member=="yes"):
        discount=purchase_amount*0.2
        final_amount=purchase_amount-discount
    else:
        discount=purchase_amount*0.1
        final_amount=purchase_amount-discount
    print(f"Original Purchase Amount: {purchase_amount}")
    print(f"Discount Applied: {discount}")
    print(f"Total Amount to be Paid: {final_amount}")    
else:
    if(purchase_amount>=2000 and purchase_amount<=5000):
        prime_member=input("Are you a prime member? yes/no: ")
        if(prime_member=="yes"):
            discount=purchase_amount*0.110
            final_amount=purchase_amount-discount
        else:
            discount=purchase_amount*0.05
            final_amount=purchase_amount-discount
        print(f"Original Purchase Amount: {purchase_amount}")
        print(f"Discount Applied: {discount}")
        print(f"Total Amount to be Paid: {final_amount}")

        #Grading System With Bonus
        marks=int(input("Enter the marks: "))
        extra_projectwork=int(input("Enter extra credit points if extra work done? yes/no: "))
        if(extra_projectwork=="yes"):
            marks+=5
            print("5 bonus marks added in final marks:",marks)
        else:
            print("No bonus marks added in final marks:",marks)
        if(marks>=90):
            grade="A"
        elif(marks>=75 and marks<90):
            grade="B"
        elif(marks>=60 and marks<75):
            grade="C"
        else:
            grade="Fail"
        print(f"Final Marks: {marks}, Grade: {grade}")

        #Hotel Room Booking System
        room_type=input("Enter room type (Standard/Delux): ")
        nights=int(input("Enter number of nights: "))
        if(room_type=="Standard " and nights==1):
            base_rate_per_night=3000
            if(nights>5):
                discount=base_rate_per_night*0.1
                base_rate_per_night-=discount
            else:
                 base_rate_per_night=3000
            total_amount=base_rate_per_night*nights
            print(f"Total amount for {nights} nights in Standard room: {total_amount}")
        elif(room_type=="Delux"and nights==1):
            base_rate_per_night=5000
            if(nights>5):
                discount=base_rate_per_night*0.15
                base_rate_per_night-=discount
            else:
                 base_rate_per_night=5000
            total_amount=base_rate_per_night*nights
            print(f"Total amount for {nights} nights in Delux room: {total_amount}")     
#   Vechicale Insurance Premium Calculator 
vehcile_type=input("Enter vehicle type (Bike/car): ")
span_time=int(input("Enter the span time in years: "))
if(vehcile_type=="Bike"):
    base_price=2000
elif(vehcile_type=="car"):
    base_price=4000
else:
    print("Invalid vehicle type")
if(span_time>5):
    premium= base_price +base_price*0.1
    print(f"The insurance premium for your {vehcile_type} is: {premium}")
    no_claim_bonus=input("Do you have no claim bonus? yes/no: ")
    if(no_claim_bonus=="yes"):
        premium= premium-(premium*0.20)
        print("20% no claim bonus applied")
    else:
        print("No no-claim bonus applied")
    print(f"The final insurance premium for your {vehcile_type} is: {premium}")

#Income Tax Calculator
income=int(input("Enter your annual income: "))
age=int(input("Enter your age: "))
if(income<=250000):
    tax=0
elif(income>250000 and income<=500000):
    tax=(income-250000)*0.05
elif(income>500000 and income<=1000000):
    tax=(income-250000)*0.05 + (income-500000)*0.2
else:
    tax=(income-250000)*0.05 + (income-500000)*0.2 + (income-1000000)*0.3
if(age>60):
    tax=tax-(tax*0.1)
print(f"The total income tax to be paid is: {tax}")

#Mobile Recharge Offer System
recharge_amount=int(input("Enter recharge amount: "))
vip_user=input("Are you a VIP user? yes/no: ")
if(recharge_amount>=1000):
    #vip_user=input("Are you a VIP user? yes/no: ")
    if(vip_user=="yes"):
        extra=recharge_amount + (recharge_amount*0.2)
    else:
        extra=recharge_amount + ( recharge_amount*0.1)
else:
    if(vip_user=="yes"):
        extra=recharge_amount + (recharge_amount*0.5) 
    else:     
        print("You are not eligible for any extra talktime") 
print(f"Total talktime available: {extra}") 
    