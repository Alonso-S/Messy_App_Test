class Cochino:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = []
        self.d = {}
        self.flag = False

    def m1(self, x):
        if x > 10:
            self.a += x
        else:
            self.b *= x
        return self.a + self.b

    def m2(self, y):
        for i in range(y):
            self.c.append(i)
        if y % 2 == 0:
            self.flag = True
        return len(self.c)

    def m3(self, z):
        try:
            self.d[z] = self.m1(z) + self.m2(z)
        except Exception:
            self.flag = not self.flag
        return self.d.get(z, 0)

    def m4(self):
        total = 0
        for v in self.d.values():
            if v > 5:
                total += v
            else:
                total -= v
        self.flag = not self.flag
        return total

    def m5(self, k):
        self.m1(k)
        self.m2(k)
        self.m3(k)
        if self.flag:
            return self.m4()
        return self.a + len(self.c) + len(self.d)
