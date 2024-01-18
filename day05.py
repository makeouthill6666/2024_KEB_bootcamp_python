# #dict comprehension
# univ = 'inha'
# counts_alpahbet = {letter: univ.count(letter) for letter in univ}
# print(counts_alpahbet)
#
# #basic
# univ = 'inha'
# counts_alpahbet = dict()
# for letter in univ:
#     counts_alpahbet[letter] = univ.count(letter)
# print(counts_alpahbet)


# drinks = {'martini': {'vodka', 'vermouth'},'black russian': {'vodka', 'kahlua'},'white russian': {'cream', 'kahlua', 'vodka'},'manhattan': {'rye', 'vermouth', 'bitters'},'screwdriver': {'orange juice', 'vodka'}}
# print(not drinks['screwdriver']&{'vermouth', 'cream'})

# for name, contents in drinks.items():
#     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
#     print(name)

# thing = None
# if thing is None :
#     print('nothing')
# else :
#     print('Something')

# None!=False

# ?

# a(7)
# a(7, 11)
#
# def a(n):
#     if n is None:
#         print(f'{n}'is None)
#     elif n:
#         print(f'{n} is True')
#     else :
#         print(f'{n}is False')
# a([])
# a([0])
# a(0)
# a(None)
# a('')

# def squares(*n) -> list:
#     """
#     넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
#     :param n: tuple
#     :return: list
#     """
#     return [pow(i, 2) for i in n]
#     #return n * n
#
#
# def run_function(f, *number) -> list:
#     return f(*number)
#
# print(squares(7, 5, 2))
# print(run_function(squares, 9, 10))


# #inner function
# def out_func(nout):
#     def inner_func(nin):
#         return nin *nin
#     return inner_func(nout)
#
# print(out_func(5))
#
# #closure
# def out_func(nout):
#     def inner_func():
#         return nout *nout
#     return inner_func
#
# x=out_func(9)
# print(x)
# print(type(x))
# print(x())
# # x() -> inner_func()

# numbers = ["7", "-11", "3"]
# plus = 0
# for i in numbers :
#     plus = plus + int(i)
# print(plus)
#
# print(sum(map(int, numbers))) #????


# def squares(n):
#     return n*n
#
# even_numbers =[i for i in range(51) if i % 2 == 0]
# print(even_numbers)
#
# print(tuple(map(squares, even_numbers)))
# print(tuple(map(lambda x : x**2, even_numbers)))
# z = lambda x: pow(x, 2)
# print(tuple(map(z, even_numbers)))
#
#
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
# stairs = ['thud','meow','thud','hiss']
# def enliven(word) :
#     return word.capitalize()
#
# edit_story(stairs, enliven)
#
# edit_story(stairs, lambda word : word.capitalize())
#
# #generator
# range()

# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number= number+step
#
# print(type(my_range))
# print(my_range())
#
# r=my_range(1,5)
# print(r, type(r))
#
# for x in r:
#     print(x)
#제너레이터는 한번만 순회할 수 있다!!!!!!!

#generator comprehension
# genobj = (pair for pair in zip(['a','b'],['1','2']))
# print(genobj)
# for thing in genobj:
#     print(thing)

def description(f):
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r=f(*args)
        return r
    return inner
@description
def squares(a):
    """
    제곱함수
    """
    return a * a

result = squares(6)
print(result)