qty = input("Enter quantity")
price = input("Enter price")
discrate = input("Enter discrate")

extprice = float('qty * price')
discamt = float('extprice * price')
discprice = float('extprice - discamt')

print("The quantity is  ", qty)
print("The price is  ", price)
print("The discamt is ", discamt)
print("The discprice is  ", discprice)