import product

name = input("Enter your name : ")
email = input("Enter your mail : ")
phone = input("Enter your phone : ")

buy = True
total = 0
quantity_list = []
a = []
while(buy == True):
    print("The products we have")
    for ele in product.product:
        print(f"{ele[0]}.{ele[1]}    -   Rs {ele[2]}")
    pid = input("enter product id you want to buy : ")
    quantity = int(input("Enter quantity : "))
    a.append(pid)
    a.append(quantity)
    quantity_list.append(a)
    a = []
    for ele in product.product:
        if ele[0] == pid:
            unit_price = int(ele[2])
            break
    total = total + (quantity * unit_price)
    buy = True if input("Do you want to buy more : (Yes/no) : ").lower() == "yes"  else False
    print(buy)
count = 1
print("----------------------------------------------------------")
print("                      INVOICE                             ")
print("----------------------------------------------------------")

print(f"Name - {name}   , Email  - {email}   , Phone No - {phone}")
for ele in quantity_list:
    for ele1 in product.product:
        if ele[0] == ele1[0]:
            print(f"{count}. {ele1[1]}  {ele[1] * int(ele1[2])}")
    count+=1        
print("----------------------------------------------------------")

print(f"Total - {total}")            

       


