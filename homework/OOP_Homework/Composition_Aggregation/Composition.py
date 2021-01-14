class Laptop:
    def __init__(self):
        cpu = "info about CPU. "
        graphics_card = "Info about Graphics Card. "
        sdd = "Info about SDD. "
        self.all_details = [sdd, graphics_card, cpu]

    def show_info(self):
        return self.all_details


class Details:
    def __init__(self):
        self.all_details = None

    def info(self):
        print(self.all_details)


Asus = Laptop()
Asus.show_info()


class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def play(self):
        print(f'Playing on guitar with {self.strings.string_tension} tension strings.')


class Strings:
    def __init__(self, string_tension):
        self.string_tension = string_tension


strings = Strings('high')
yamaha = Guitar(strings)
yamaha.play()

strings_tension = strings.string_tension
print(strings_tension)
