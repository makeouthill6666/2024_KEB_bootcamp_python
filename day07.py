# # class FlyingMixin:
# #     def fly(self):
# #         return f"{self.name}은(는) 비전머신 02 공중날기를 배울 수 있다..."
#
# # class SwimingMixin:
# #     def swim(self):
# #         return f"{self.name}은(는) 비전머신 03 파도타기를 배울 수 있다..."
#
# class FlyingBehavior:
#     def fly(self):
#         return f"하늘을 난다"
#
# class Nofly(FlyingBehavior):
#     def fly(self):
#         return f"하늘을 못난다"
# class Flywithwings(FlyingBehavior):
#     def fly(self):
#         return f"날개로 난다"
#
# class Pokemon:
#     def __init__(self, name, hp, fly):
#         self.__name = name
#         self.hp = hp
#         self.fly_behavior = fly #aggregation (has-a)
#
#     def attack(self):
#         print (f"{self.name}은(는) 싸운다")
#
#     @property
#     def name(self):
#         # print("inside getter")
#         return self.__name
#     @name.setter
#     def set_name(self, new_name):
#         print("inside setter")
#         self.__name = new_name
#
#     # name = property (get_name,set_name)
#     def __str__(self):
#         return self.__name + "입니다"
#
#     def __add__(self, target):
#         # return self.__name + " + " + target.__name
#         return f"두 포켓몬스터 체력의 합은 {self.__hp + target.__hp}입니다."
# class Charizrad(Pokemon, FlyingBehavior) :
#     pass
#
# class Gyarados(Pokemon, FlyingBehavior) :
#     pass
#
# class JetPack(FlyingBehavior):
#     def
#
# nofly = Nofly
# g1 = Gyarados("갸라도스", 100, nofly)
# wings = Flywithwings()
# c1 = Charizrad("리자몽", 120, wings)
#
# print(g1.fly_behavior.fly())
# print(c1.fly_behavior.fly())
#
# print(c1)
# print(g1)
# print(g1+c1)
# #  ???  +는 add를 사용해야됨
#
#
#
# # s -> P <- FlyingMixin
# #
# # C -> P
# # G -> Pokemon
# # G->s XXXX
# # C->f xxxx

# class FlyingBehavior:
#     def fly(self):
#         return f"하늘을 훨훨 날아갑니다~"


# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"로켓추진기로 하늘을 날아갑니다!"
#
#
# class NoFly(FlyingBehavior):
#     def fly(self):
#         return f"하늘을 날 수 없습니다."
#
#
# class FlyWithWings(FlyingBehavior):
#     def fly(self):
#         return f"날개로 하늘을 훨훨 날아갑니다"


# class SwimmingBehavior:
#     def swim(self):
#         return f"{self.__name}이(가) 수영을 합니다."
#
# class Pokemon:
#     def __init__(self, name, hp, fly):
#         self.__name = name
#         self.hp = hp
#         self.fly_behavior = fly  # aggregation (has-a)
#
#     def set_fly_behavior(self, fly):
#         self.fly_behavior = fly
#
#
#     def attack(self):
#         print("공격~")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     # magic method
#     def __str__(self):
#         return self.__name + " 입니다"
#
#     def __add__(self, target):
#         #return self.__name + " + " + target.__name
#         return f"두 포켓몬스터 체력의 합은 {self.hp + target.hp}입니다."

# class FlyingBehavior:
#     def fly(self):
#         return f"하늘을 훨훨 날아갑니다~"
#
#
# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"로켓추진기로 하늘을 날아갑니다!"
#
#
# class Nofly(FlyingBehavior):
#     def fly(self):
#         return f"하늘을 날 수 없습니다."
#
#
# class FlyWithWings(FlyingBehavior):
#     def fly(self):
#         return f"날개로 하늘을 훨훨 날아갑니다"
#
# class Pikachu:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp
#         self.fly_behavior = Nofly()
#
#
# p1 = Pikachu("피카츄", 35)  # LSP
# print(p1.fly_behavior.fly())
# print(c1.fly_behavior.fly())
# # print(g1)
# # print(c1)
# # print(g1+c1)
#
# p1.set_fly_behavior(JetPack())
# print(p1.fly_behavior.fly())
# #print(g1+200)


import mymath

while True :
    Menu = input("1) Celsius to Fahrenheit 2)Fahrenheit to Celsius 3)Prime number checker 4)Prime number checker between two numbers 5) Quit : ")
    print()
    if Menu not in ['1', '2', '3', '4', '5'] :
        print("Please choose from the menu.")
    if Menu == '1' :
        pass
    elif Menu == '2' :
        pass
    elif Menu == '3' :
        try:
            n = int(input("Input an integer: "))
            if mymath.isprime(n):
                print(f'{n} is a prime number')
            else:
                print(f'{n} is not a prime number')
        except ValueError:
            print("Invalid input. Please enter an integer.")

    elif Menu == '4' :
        try:
            n1, n2 = map(int,input("Input two different numbers : ").split())
            n1, n2 = min(n1, n2), max(n1, n2)

            for n in range(n1, n2 + 1):
                if mymath.isprime(n):
                    print(n, end=' ')

        except ValueError:
            print("Invalid input. Please enter two different integers.")

    elif Menu == '5' :
        print('Terminating the program.')
        break
    print()