from random import randint


class House:
    def __init__(self, area, price, sale, sum_sale):
        self.area = area
        self.price = price
        self.sale = sale
        self.sum_sale = sum_sale

    def info_about_house(self):
        print(f"House is {self.area} square metres and its price {self.price}.")

    def sale_for_home(self):
        self.sale = randint(1, 15)
        self.sum_sale = self.price / 100 * self.sale
        print(f"This is the discount amount : {self.sum_sale}")

    def price_ws(self):
        price_with_sale = self.price - self.sum_sale
        print(f"This is the amount of the house with a discount : {price_with_sale}")


class Human:
    def __init__(self, age, name, money, house_owning):
        self.age = age
        self.name = name
        self.money = money
        self.house_owning = house_owning

    def working(self):
        if self.money <= 0:
            print(self.money)
        else:
            if self.money >= 1:
                while self.money <= 1000000:
                    self.money *= 10
                    print(self.money)

    def bye_my_house(self):
        if B.price < self.money:
            self.house_owning = "have "
            print("Congratulations, you have bought your own house")
        else:
            return "Sorry , you don't have enough money"

    def say_about_me(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years. I {self.house_owning} house.")


B = House(50, 850000, 0, 0)
H = Human(30, "Ruslan", 1, "don't have")
B.info_about_house()
B.sale_for_home()
B.price_ws()
H.working()
H.bye_my_house()
H.say_about_me()