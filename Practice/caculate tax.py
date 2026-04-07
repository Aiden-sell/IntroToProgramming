item = input("What is your item? ")
price = input("What is the price of your item? ")
numfloat = float(price)
tax = 6.875
numfloat2 = float(tax)
def calculate_tax():
    total = numfloat * (1 + numfloat2 / 100)
    print(item)
    print("cost before tax $" + "{:.2f}".format(numfloat))
    print(f"{item} will cost a total of ${total:.2f} dollars")

calculate_tax()
