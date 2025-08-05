# class Animal:
#     def __init__(self,name) :
#        self.name= name

#     def speak(self):
#         print(f'{self.name} makes a sound.')

# class Dog(Animal):
#     def speak(self):
#         print(f'{self.name} barks.')

# animal = Animal('Generic Animal')
# animal.speak()

# dog = Dog('Buddy')
# dog.speak()


class Animal:
    def __init__(self):
        self.name="Buddy"

    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f'{self.name} barks. It is a {self.breed}')

dog = Dog('Husky')
dog.speak()