class Animal:
    def move(self):
        pass  # Abstract method to override


class Dog(Animal):
    def move(self):
        print("Running")


class Fish(Animal):
    def move(self):
        print("Swimming")


class Bird(Animal):
    def move(self):
        print("Flying")


# Create objects
dog = Dog()
fish = Fish()
bird = Bird()

# Polymorphism in action
for animal in (dog, fish, bird):
    animal.move()
