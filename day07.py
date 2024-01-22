class FlyingMixin:
    def fly(self):
        return f"{self.name}은(는) 비전머신 02 공중날기를 배울 수 있다..."

class SwimingMixin:
    def swim(self):
        return f"{self.name}은(는) 비전머신 03 파도타기를 배울 수 있다..."
class Pokemon:
    def __init__(self, name):
        self.__name = name
    def attack(self):
        print (f"{self.name}은(는) 싸운다")

    @property
    def name(self):
        # print("inside getter")
        return self.__name
    @name.setter
    def set_name(self, new_name):
        print("inside setter")
        self.__name = new_name

    # name = property (get_name,set_name)
    def __str__(self):
        return self.__name + "입니다"

    def __add__(self, target):
        return self.__name + " + " + target.__name
class Charizrad(Pokemon, FlyingMixin) :
    pass

class Gyarados(Pokemon, SwimingMixin) :
    pass

g1 = Gyarados("갸라도스")
c1 = Charizrad("리자몽")
print(c1)
print(g1)
print(g1+c1)
#  ???  +는 add를 사용해야됨

