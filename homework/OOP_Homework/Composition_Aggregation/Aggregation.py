class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def play(self):
        print(f'I  play  with {Strn.num_strings} strings')


class Strings:
    def __init__(self, num_strings):
        self.num_strings = num_strings


Strn = Strings("four")
Gibson = Guitar("Fzone")
Gibson.play()
num_strings = Strn.num_strings
