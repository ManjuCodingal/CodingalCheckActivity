#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
# costPrice=100
# SellingPrice=120
costPrice=float(input("Enter cost price : "))
SellingPrice=float(input("Enter selling price : "))
if SellingPrice>costPrice :
   print("The profit is",SellingPrice-costPrice)
else :
   print("The loss is ",costPrice-SellingPrice)