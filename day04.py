# t1 = () #empty_tuple
# t2 = 5,
# t3 = (5,)
# t4 = (5,7)
# t5 = 5,7
# print(type(t1), type(t2),type(t3),type(t4), type(t5))
# t6 = "py", "k" # packing
# print(type(t6), t6[1])
# sub, prof = t6 # unpacking 개수가 맞아야 한다
# print(prof)
# # a,b,c=t6
#
# # n1, n2 = n2, n1 # packing & unpacking
# t7=()
# print(type(t7))

# a='gr',
# b=('gr',)
# print(type(a), type(b))
# print(type('gr',))
# print(type(('gr',)))
#
# tuple()
#
# # tuple은 + * 비교연산 모두 가능
# t9 = 1, 2, 3
# t10 = 1, 2
# print(t9==t10)
# print(t9>=t10)

# tuple은 list처럼 sequence를 가지고 있다
# tuple은 immutable 새로 만들어서 수정해야함
t11 = 4.43,
t12 = 3.97, 4.1, 3.27
print(t11+t12)
print(id(t11))
#1974994883088
t11 = t11 +t12
print(t11)
print(id(t11))
# 1974995080096
# 결과값은 같지만 두개가 달라 '튜플을 수정하는척 하지만 새로운 값을 만든것'


