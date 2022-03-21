from locale import currency


with open ("currency_data.txt", "r") as f:
    lines = f.readlines()
# print(lines)
currencyDict={}
for line in lines:
    value = line.split("\t")
    # print(value)
    currencyDict[value[0]] = value[1]

amount = int(input("Enter amount: \n"))
print("Enter the name of the currency you want to convert this amount to? Available options: \n")
[print(item) for item in currencyDict.keys()]
currency = input(" please enter one of the option: \n")
print(f"{amount} INR is equal t0 {amount * float(currencyDict[currency])} {currency} ")







