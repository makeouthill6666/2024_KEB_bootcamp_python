# def change_and_print_global():
#     print('inside change_and_print_global: ', animal)
#     animal='wombat'
#     print('after the change:', animal)
#
#     print(change_and_print_global())

# def change_local():
#     animal ='cat'
#     print('inside change_local:', animal, id(animal))
#
# print (change_local())
#
#
# def change_local():
#     animal ='cat'
#     print('inside change_local:', animal, id(animal))
#
#     print(animal)
#
# def change_local():
#     animal ='cat'
#     print('inside change_local:', animal, id(animal))
#
#     print(id(animal))

# def factorial_repetition(n) -> int:
#     """
#     반복문을 이용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: 팩토리얼값, int
#     """
#     result = 1
#     for i in range (2, n+1):
#         result = result *i
#     return result
#
# def factorial_recursion(n):
#     '''
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: function, int
#     '''
#     if n ==1:
#         return n
#     else :
#         return n * factorial_recursion((n-1))
#
# number = (int(input("number : ")))
#
# print(factorial_repetition(number))
#
# print(factorial_recursion(number)
#
# list=[1,2,3]
# a = 5
# # list[a]
#
# try :
#     list[a]
# except:
#     print(f'{a}, {len(list)-1}, but got {a}')

# import random
#
# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
# print(numbers)
#
#
# numbers=[random.randint(1,100) for i in range(10)]
# print(numbers)
# try :
#     pick = int(input(f"Input index : (0~{len(numbers)-1}) : "))
#     print(numbers[pick])
# except IndexError as err :
#     print(f'out of range \n{err}')
# except ValueError as err:
#     print(f'enter an integer\n{err}')
# except ZeroDivisionError as err:
#     print(f"dominator cannot be 0.\n{err}")
# # except Exception: #맨 밑에 와야함 여기서 끝나기 싫으면
# #     print("error occurs")

# def desc(f) :
#     def wrapper():
#         print('study')
#         f()
#     return wrapper#()
#
# @desc
# def something():
#     print("do something")
# something()
# s = desc(something)
# s()

# class Pokemon():
#     pass
#     # def __init__(self, name):
#     #     print(f"포켓몬 {name} 생성")
# # pikachu = Pokemon("피카츄")
# # squirtle = Pokemon("꼬부기")
#
# # print(pikachu)
# # print(squirtle)
#
# pikachu = Pokemon()
# squirtle = Pokemon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
#
# squirtle.name = "꼬부기"
# print(pikachu.nemesis.name)
#
# class Pokemon:
#     def __init__(self):
#         pass
#
# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#         print(f'포켓몬 {name} 생성')
#
#     def attack(self, target):
#         print(f'{self.name}이(가) {target.name}을(를) 공격했다!!!')
#
#
# charizard = Pokemon("리자몽")
# pikachu = Pokemon("피카츄")
# squirtle = Pokemon("꼬부기")
# charizard.attack(squirtle)


# print(pikachu.name)
# print(squirtle.name)

# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#
#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) 공격했다.")
#
# #class Pikachu:
#
# class Pikachu(Pokemon) :
#     def __init__(self, name, type):
#         super().__init__(name) #부모에게 도움받기....!!!!
#         self.type=type
#         print(f'{type} 속성이라 효과가 미미하다!')
#
#     def attack(self, target):
#         print(f"상대 {self.name}의 전광석화!!!")
#
#         # def
#
# class Squirtle(Pokemon):  # is-a
#     def __init__(self, name):
#         self.name = name
#
#     def attack(self, target):
#         print(f"상대 {self.name}의 물대포!!!")
#
# p1 = Pikachu("피카츄", "전기")
# p2 = Squirtle("꼬부기")
# # p1.electric_info
# print(p1.name, p1.type)
# p1.attack(p2)
# p2.attack(p1)
#
#
# print(issubclass(Pikachu, Pokemon))
# # print(issubclass(Agumon, Pokemon))
#
# class Animal:
#     def says(self):
#         return 'I speak!'
#
# class Horse(Animal):
#     def says(self):
#         return '말소리'
#
# class Donkey(Animal):
#     def says(self):
#         return '당나귀 소리'
#
# class Mule(Donkey, Horse):
#     def says(self):
#         return '노새 소리'
#
# class Hinny(Horse, Donkey) :
#     def says(self):
#         return '버새 소리'
# m1 = Mule()
# h1 = Hinny()
# print(Hinny.__mro__)
# print(Mule.__mro__)
# print(h1.says())
# print(m1.says())


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

class Charizrad(Pokemon, FlyingMixin) :
    pass

class Gyarados(Pokemon, SwimingMixin) :
    pass

g1 = Gyarados("갸라도스")
c1 = Charizrad("리자몽")
print(c1.fly())
print(g1.swim())

c1.attack()
Charizrad.attack(c1)
#c1을 넣지 않으면 오류발생

# print(g1.name)
# g1.name = "잉어킹"
# print(g1.name)

# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.set.name())

# # property
# print(g1.name)
# g1.hidden_name = "잉어킹"
# print(g1.hidden_name)
# print(g1.__name) #AttributeError: 'Gyarados' object has no attribute '__name'. Did you mean: 'name'?
print(g1.name) #이거는 됨
print(g1._Pokemon__name) #이거는 또 됨

g1.__name = "잉어킹"
print(g1.__name)
# g1._Pokemon__name = "잉어킹"
# print(g1.__name)