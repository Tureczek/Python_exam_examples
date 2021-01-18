class Person:
    def __init__(self, *args):
        self.__name = args[0]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Grandmom(Person):

    def __init__(self, *args):
        super().__init__(*args)
        self.__cook = "Delicious food coming up!"

    def cook(self):
        print(f'{self.name}: "{self.__cook}"')


class Granddad(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.__tell_bad_joke = "Telling the same old bad joke.. Again!"

    def tell_bad_joke(self):
        print(f'{self.name}: "{self.__tell_bad_joke}"')


class Mom(Grandmom):

    def __init__(self, *args):
        super().__init__(*args)
        self.__cook_vegan = "Im gonna make delicious vegan food..."

    def cook_vegan(self):
        print(f'{self.name}: "{self.__cook_vegan}"')


class Dad(Granddad):

    def __init__(self, *args):
        super().__init__(*args)
        self.__sound_wise = "...so you see, that's why im very wise..."

    def sound_wise(self):
        print(f'{self.name}: "{self.__sound_wise}"')


class Kid(Mom, Dad):
    def __init__(self, *args):
        super().__init__(*args)
        self.__make_annoying_sounds = "MEEEEEEEEEEEEEEEEEEEEEEEEIIIIIIIIIIIIIOOOOOOOOOUUUUUUU"

    def make_annoying_sounds(self):
        print(f'{self.name}: "{self.__make_annoying_sounds}"')


gm = Grandmom('Marge')

d = Dad('Peter')

k = Kid('Jason')

k.cook()
k.cook_vegan()
k.sound_wise()
k.make_annoying_sounds()
k.tell_bad_joke()
