#Define the menu of resturant
menu={
    'Pizza':40,
    'Pasta':50,
    'French Fries':175,
    'Chowmin':160,
    'Steam momo':200
}
#print(menu)
#Great
print("Welcome To Chiku Resturant")
print("Pizza: 40\nPasta: 50\nFrench Fries: 175\nChowmin: 100\nSteam momo: 200")
# For the taking order from customer
order_total=0
# 40 + 50 =90

item_1=input("Enter the name of the item you want to order=")
if item_1 in menu:
    order_total +=  menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Your odered{item_1} is not available yet")

#If anything else ordered
another_order=input("Do you Want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2=input("Enter the name of the second item=")
    order_total += menu[item_2]
    print(f"Second item{item_2} has been added in order")
else:
    print(f"Ordered item{item_1} is not available")

print(f"The totaal amount is to pay{order_total}")