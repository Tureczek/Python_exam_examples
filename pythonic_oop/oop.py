class Dinosaur:

    # Make the class initialisable.
    def __init__(self, *args):
        self.dinosaur_name = args[0]
        self.dinosaur_type = args[1]
        self.sound = args[2]
        self.food_type = args[3]

    # Make the Dinosaur class callable.
    def __call__(self):
        return f'Name: {self.__dinosaur_name}, Type: {self.__dinosaur_type}, Sound: {self.__sound}, ' \
               f'Food type: {self.__food_type} '

    # Make the Dinosaur class addable.
    def __add__(self, other):
        name = self.__dinosaur_name[:int(len(self.__dinosaur_name) / 2)] + \
               other.__dinosaur_name[-int(len(other.__dinosaur_name) / 2):]
        type = self.__dinosaur_type[:int(len(self.__dinosaur_type) / 2)] + \
               other.__dinosaur_type[-int(len(other.__dinosaur_type) / 2):]
        sound = self.__sound[:int(len(self.__sound) / 2)] + other.__sound[-int(len(other.__sound) / 2):]
        if self.__food_type == other.__food_type:
            return f'Name: {name}, Type: {type}, Sound: {sound}, Food type: {self.__food_type}'
        if self.__food_type != other.__food_type:
            return f'Name: {name}, Type: {type}, Sound: {sound}, Food type: Omnivore'

#######################################################################################################################

    # Dinosaur Name.
    @property
    def dinosaur_name(self):
        return self.__dinosaur_name

    @dinosaur_name.setter
    def dinosaur_name(self, dinosaur_name):
        self.__dinosaur_name = dinosaur_name

    # Dinosaur Type.
    @property
    def dinosaur_type(self):
        return self.__dinosaur_type

    @dinosaur_type.setter
    def dinosaur_type(self, dinosaur_type):
        self.__dinosaur_type = dinosaur_type

    # Sound.
    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, sound):
        self.__sound = sound

    # Food type.
    @property
    def food_type(self):
        return self.__food_type

    @food_type.setter
    def food_type(self, food_type):
        self.__food_type = food_type


#######################################################################################################################

# Creating a couple of dinosaurs.
raptor = Dinosaur('Raptuella', 'Raptor', 'Rhaaarr', 'Carnivore')
brachiosaurus = Dinosaur('Brandon', 'Brachiosaurus', 'Mhhuuurrrh', 'Herbivore')
coloradisaurus = Dinosaur('Conrad', 'Coloradisaurus', 'Mvih Mvah', 'Omnivore')

# Using __call__ function.
print(raptor())

# Using __add__ function. (To make new types of dinosaurs)
print(brachiosaurus + raptor)
print(coloradisaurus + raptor)
print(raptor + coloradisaurus)
print(raptor + brachiosaurus)

