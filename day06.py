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

import random

numbers = list()
for i in range(5):
    numbers.append(random.randint(1, 100))
print(numbers)


numbers=[random.randint(1,100) for i in range(10)]
print(numbers)
try :
    pick = int(input(f"Input index : (0~{len(numbers)-1}) : "))
    print(numbers[pick])
except IndexError as err :
    print(f'out of range \n{err}')
except ValueError as err:
    print(f'enter an integer\n{err}')
except ZeroDivisionError as err:
    print(f"dominator cannot be 0.\n{err}")
# except Exception: #맨 밑에 와야함 여기서 끝나기 싫으면
#     print("error occurs")