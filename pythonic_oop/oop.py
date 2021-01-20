import random


class Park:

    def __init__(self):
        self.animals = []

    def __str__(self):
        representation = 'Printing list of animals in park:\n'
        for x in self.animals:
            representation += f'{x}\n'
        return representation


class Dinosaur:

    # Make the class initialisable.
    def __init__(self, *args):
        self.dinosaur_name = args[0]
        self.dinosaur_type = args[1]
        self.sound = args[2]
        self.food_type = args[3]
        self.gender = args[4]

    # Make the Dinosaur class callable.
    def __call__(self):
        return f'Name: {self.__dinosaur_name}, Type: {self.__dinosaur_type}, Sound: {self.__sound}, ' \
               f'Food type: {self.__food_type}, Gender: {self.__gender} '

    # Make the Dinosaur class addable.
    def __add__(self, other):
        if self.__gender == other.__gender:
            return 'No new dinosaur was made!'
        name = self.__dinosaur_name[:int(len(self.__dinosaur_name) / 2)] + \
               other.__dinosaur_name[-int(len(other.__dinosaur_name) / 2):]
        type = self.__dinosaur_type[:int(len(self.__dinosaur_type) / 2)] + \
               other.__dinosaur_type[-int(len(other.__dinosaur_type) / 2):]
        sound = self.__sound[:int(len(self.__sound) / 2)] + other.__sound[-int(len(other.__sound) / 2):]
        if random.uniform(0, 1) == 0:
            gender = 'female'
        else:
            gender = 'male'
        if self.__food_type == other.__food_type:
            return f'{self.__dinosaur_name} & {other.__dinosaur_name} made a new dinosaur: \n' \
                   f'\u001b[31mName:\u001b[0m {name}, \u001b[32mType:\u001b[0m {type}, \u001b[33mSound:\u001b[0m ' \
                   f'{sound}, \u001b[35mFood type:\u001b[0m {self.__food_type}, \u001b[36mGender:\u001b[0m {gender}'
        if self.__food_type != other.__food_type:
            return f'{self.__dinosaur_name} & {other.__dinosaur_name} made a new dinosaur: \n' \
                   f'\u001b[31mName:\u001b[0m {name}, \u001b[32mType:\u001b[0m {type}, \u001b[33mSound:\u001b[0m ' \
                   f'{sound}, \u001b[35mFood type:\u001b[0m Omnivore, \u001b[36mGender:\u001b[0m {gender}'

    # Make a string representation of the dinosaur.
    def __str__(self):
        return f'\u001b[31mName:\u001b[0m {self.__dinosaur_name}, \u001b[32mType:\u001b[0m {self.__dinosaur_type}, ' \
               f'\u001b[33mSound:\u001b[0m {self.__sound}, \u001b[35mFood type:\u001b[0m {self.__food_type}, ' \
               f'\u001b[36mGender:\u001b[0m {self.__gender} '

    ###################################################################################################################

    # Dinosaur Name getters and setters.
    @property
    def dinosaur_name(self):
        return self.__dinosaur_name

    @dinosaur_name.setter
    def dinosaur_name(self, dinosaur_name):
        self.__dinosaur_name = dinosaur_name

    # Dinosaur Type getters and setters.
    @property
    def dinosaur_type(self):
        return self.__dinosaur_type

    @dinosaur_type.setter
    def dinosaur_type(self, dinosaur_type):
        self.__dinosaur_type = dinosaur_type

    # Sound getters and setters.
    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, sound):
        self.__sound = sound

    # Food type getters and setters.
    @property
    def food_type(self):
        return self.__food_type

    @food_type.setter
    def food_type(self, food_type):
        self.__food_type = food_type

    # Gender getters and setters.
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender


#######################################################################################################################

# Creating a park for dinosaurs.
park = Park()

# Creating a couple of dinosaurs.
raptor = Dinosaur('Raptuella', 'Raptor', 'Rhaaarr', 'Carnivore', 'Male')
brachiosaurus = Dinosaur('Brandon', 'Brachiosaurus', 'Mhhuuurrrh', 'Herbivore', 'Female')
coloradisaurus = Dinosaur('Conrad', 'Coloradisaurus', 'Mvih Mvah', 'Omnivore', 'Female')

# Putting dinosaurs in park
park.animals.append(raptor)
park.animals.append(brachiosaurus)
park.animals.append(coloradisaurus)

# Using __str__ function for Park.
#print(park)

# Using __call__ function.
# print(raptor())

# Using __str__ function.
# print(raptor)

# Using __add__ function. (To make new types of dinosaurs)
print(brachiosaurus + raptor)
#print(coloradisaurus + raptor)
#print(raptor + coloradisaurus)
#print(raptor + brachiosaurus)
#print(coloradisaurus + brachiosaurus)

