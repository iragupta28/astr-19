# Write a Python program that declares a class describing your favorite animal. Have the data members of the class represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of the class is created. Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.

class Animal():
    def __init__(self, arms: float, legs: float, eyes: int, tail: bool, furry: bool):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
        
    print("My favorite animal is an orangutan.")

    def details(self):
        print(
            f"Length of the arms: {self.arms} inches.\n"
            f"Length of the legs: {self.legs} inches.\n"
            f"Number of eyes: {self.eyes}.\n"
            f"Does it have a tail? {'Yes' if self.tail else 'No'}.\n"
            f"Is it furry? {'Yes' if self.furry else 'No'}.\n"
        )
        
my_animal = Animal(36.0, 31.0, 2, False, True)

my_animal.details()
