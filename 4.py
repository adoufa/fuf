class Example():
    a = 4
    b = 5
    def __init__(self, t, r):
        self.t = t
        self.r = r
    def f1(self):
        self.c = 5
        print(self.c)
    def f2(self):
        return self.a + self.b
    def f3(self):
        return self.t**self.r