from Classes.Notifications.Subject import Subject


class MedDEPO(Subject):
    """Singleton pattern to ensure single instance\
    Observer Pattern to notify NotificationGenerator and UnreadManager"""

    class _SingletonMedDEPO:
        def __init__(self):
            self.a = 1
            self.b = -8
            self.c  = 0

        def setA(self,a):
            self.a = a
        def setC(self,c):
            self.c = c
        def getC(self):
            print(str(self.c))

        def foo(self):
            print("HI")

    instance = None
    def __new__(cls):  # __new__ always a classmethod
        if not MedDEPO.instance:
            MedDEPO.instance = MedDEPO._SingletonMedDEPO()
        return MedDEPO.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)



m = MedDEPO()
print(m.a)
print(m.b)
m.setA(90)
m.b = 100
m.getC()
m.setC(5)
m.foo()
m2 = MedDEPO()
print(m2.a)
print(m2.b)
m2.getC()

# class OnlyOne(object):
#     class __OnlyOne:
#         def __init__(self):
#             self.val = None
#         def __str__(self):
#             return `self` + self.val
#     instance = None
#     def __new__(cls): # __new__ always a classmethod
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__OnlyOne()
#         return OnlyOne.instance
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#     def __setattr__(self, name):
#         return setattr(self.instance, name)
#
# x = OnlyOne()
# x.val = 'sausage'
# print(x)
# y = OnlyOne()
# y.val = 'eggs'
# print(y)
# z = OnlyOne()
# z.val = 'spam'
# print(z)
# print(x)
# print(y)