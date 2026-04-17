# Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes
class India:
    def capital(self):
        print("capital is New Delhi")
    def language(self):
        print("Hindi is main language")
    def type(self):
        print("developing country")

class USA:
    def capital(self):
        print("capital is Washington D.C.")
    def language(self):
        print("English is main language")
    def type(self):
        print("developed country")
obj_india=India()
obj_USA=USA()

for country in (obj_india,obj_USA):
    country.capital()
    country.language()
    country.type()