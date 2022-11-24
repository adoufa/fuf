class Human:
    def breathe(self):
        print("человек дышит")
    def walk(self):
        print("человек ходит")
class Doctor(Human):
    def heal(self):
        print("доктор лечит")
d = Doctor()
d.walk()
d.breathe()
d.heal()