class Dog:
    def info(self):
        print("I am dog")
    def make_sound(self):
        print("Wow")
c = Cat()
d = Dog()
for animal in (c, d):
    animal.make_sound()
    animal.info()
    animal.make_sound()