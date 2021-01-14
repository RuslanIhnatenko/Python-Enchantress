class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def about_me(self):
        print(f"Hello , I am animal and me {self.age} years")


class Raccoon(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def about_me(self):
        print(f"Hello , I am animal and me {self.age} years")

    def weight_raccoon(self):
        if self.weight > 5:
            print("I am not heavy , it is all fur")
        else:
            print("Racoon is never too much")


class Otter(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def about_me(self):
        print(f"Hello , I am animal and me {self.age} years")

    def destroy(self):
        print(f"My name is {self.name} and I am very nice otter, and I can destroy all your house)")


class Owl(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def about_me(self):
        print(f"Hello , I am animal and me {self.age} years")

    def sleep(self):
        print("I really want to sleep ,5 more minutes")


class RedPanda(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def about_me(self):
        print(f"Hello , I am animal and me {self.age} years")

    def active(self):
        print("I am the most active animal on the planet, you cant not stop me")


class Puma(Animal):
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
        super().__init__(age, weight)

    def big_cat(self):
        print("I am very a  big cat,and now this house is mine")

