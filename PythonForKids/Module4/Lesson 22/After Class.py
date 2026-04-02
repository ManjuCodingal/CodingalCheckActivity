tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

def find_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

print("Product of tup1:", find_product(tup1))
print("Product of tup2:", find_product(tup2))