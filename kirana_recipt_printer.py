# keep adding a stream of numbers inputed by the user.the adding stops as soon as user presses q key on the keyboard.
itemList = []
itemPrice = []
sum = 0
while True: 
    itemName = input("enter the item or press 'q' to quit:: \n ")
    if itemName!= 'q':
        userInput = input("enter the item price \n")
        sum = sum + int(userInput)
        itemList.append(itemName)
        itemPrice.append(userInput)
        print(f"order total so far {sum}")

    else:
        
        for i in range (100):
            print(f" {i}.  {itemList[i]}   -->    {itemPrice[i]}")
            
        print(f" your bill total is {sum}")
        print(f"Thanks for shopping with us !! \n ")

        break
