class A:
    def _private(self):
        print("Это приватный метод")
class B:
    def __private(self):
        print("Это приватный метод")
a = A()
b = B()
a._private()
b._private()