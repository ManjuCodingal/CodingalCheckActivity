class RomanConverter:

    def __init__(self, num):
        self.num = num

    def to_roman(self):
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        number = self.num
        roman = ""

        for i in range(len(values)):
            while number >= values[i]:
                roman += symbols[i]
                number -= values[i]

        return roman


num = int(input("Enter an integer: "))
obj = RomanConverter(num)
print("Roman numeral:", obj.to_roman())