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

class Pokemon():
    pass
    # def __init__(self, name):
    #     print(f"포켓몬 {name} 생성")
# pikachu = Pokemon("피카츄")
# squirtle = Pokemon("꼬부기")

# print(pikachu)
# print(squirtle)

pikachu = Pokemon()
squirtle = Pokemon()
pikachu.name = "피카츄"
pikachu.nemesis = squirtle
print(pikachu.name)

squirtle.name = "꼬부기"
print(pikachu.nemesis.name)

class Pokemon:
    def __init__(self):
        pass

class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f'포켓몬 {name} 생성')

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격했다!!!')


charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
charizard.attack(squirtle)


# print(pikachu.name)
# print(squirtle.name)