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
# t10 = 1, 21
# print(t9==t10)
# print(t9<=t10)
# print(t9>t10)

# # tuple은 list처럼 sequence를 가지고 있다
# # tuple은 immutable 새로 만들어서 수정해야함
# t11 = 4.43,
# t12 = 3.97, 4.1, 3.27
# print(t11+t12)
# print(id(t11))
# #1974994883088
# t11 = t11 +t12
# print(t11)
# print(id(t11))
# # 1974995080096
# # 결과값은 같지만 두개가 달라 '튜플을 수정하는척 하지만 새로운 값을 만든것'
#
# list() -> []
# list('cat') -> ['c', 'a', 't']
# list(a_tuple)->
#
# # tuple - immutable / list - mutable 성적 마감돼도 바꿀수있다

splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

# list.reverse
subjects  = ["c++", "java", "python","java", "5", "9", "안녕"]


# subjects[::-1]
# print (subjects)
# subjects.remove(("java")) #앞의 항목을 삭제
# print (subjects)
# del subjects[-1] #뒤에서 첫번째 지정하여 삭제
# print(subjects)
# subjects.pop() #아무값도 지정하지 않으면 가장 뒤의 항목 삭제
# print(subjects)
# subjects.clear()
# print(subjects)
subjects.sort()
print(subjects)
# 숫자, 영어, 한글 순

subjects.sort(reverse=True) #역순
print(subjects)

copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects)


# ['c++', 'java', 'python']

# subjects.reverse()
# # revere함수에서는 자체의 값을 바꾼다 =이 내장
# print(subjects)
# # ['python', 'java', 'c++']
#
# list.append() 맨뒤에 추가
# list.insert() 원하는 곳에 추가
# list.extend() 리스트를 병합 += 이걸로도 똑같다
#
# list.append()로 병합하면 list 안에 list 생성
# [a,b,c,[other list]]

