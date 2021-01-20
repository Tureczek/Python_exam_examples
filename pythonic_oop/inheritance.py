from generators_decorators_context_manager.decorators import *


class Person:
    def __init__(self, *args):
        self.__name = args[0]
        self.__surname = "Henriksen"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

class Grandmom(Person):

    def __init__(self, *args):
        super().__init__(*args)
        self.__cook = "Delicious food coming up!"

    @time_stamp
    def cook(self):
        return (f'{self.name} {self.surname}: "{self.__cook}"')


class Granddad(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.__tell_bad_joke = "Telling the same old bad joke.. Again!"

    @time_stamp
    def tell_bad_joke(self):
        return (f'{self.name} {self.surname}: "{self.__tell_bad_joke}"')

    @time_stamp
    def fart_loudly(self):
        return (f'{self.name} {self.surname} makes a loud fart!')


class Mom(Grandmom):

    def __init__(self, *args):
        super().__init__(*args)
        self.__cook_vegan = "Im gonna make delicious vegan food..."

    @time_stamp
    def cook_vegan(self):
        return (f'{self.name} {self.surname}: "{self.__cook_vegan}"')


class Dad(Granddad):

    def __init__(self, *args):
        super().__init__(*args)
        self.__sound_wise = "...so you see, that's why im very wise..."

    @time_stamp
    def sound_wise(self):
        return (f'{self.name} {self.surname}: "{self.__sound_wise}"')


class Kid(Mom, Dad):
    def __init__(self, *args):
        super().__init__(*args)
        self.__make_annoying_sounds = "MEEEEEEEEEEEEEEEEEEEEEEEEIIIIIIIIIIIIIOOOOOOOOOUUUUUUU"

    @time_stamp
    def make_annoying_sounds(self):
        return (f'{self.name} {self.surname}: "{self.__make_annoying_sounds}"')


gm = Grandmom('Marge')
d = Dad('Peter')
k = Kid('Jason')

print(k.cook(), "\n")
print(k.cook_vegan(), "\n")
print(k.tell_bad_joke(), "\n")
print(k.sound_wise(), "\n")
print(k.make_annoying_sounds(), "\n")

# Showing which methods is available to a class (Kid):
print('Showing available methods:')
print([x for x in dir(Kid) if callable(getattr(Kid, x)) if not x.startswith('__')])
print([x for x in dir(Dad) if callable(getattr(Dad, x)) if not x.startswith('__')])
print([x for x in dir(Granddad) if callable(getattr(Granddad, x)) if not x.startswith('__')])
