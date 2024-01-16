#assignment (loop)
# while True :
#      menu = input("1.화씨->섭씨 2.섭씨->화씨 3.끝")
#      if menu == '1' :
#          화씨 = float(input('화씨'))
#          print(f'화씨:{화씨}F, 섭씨:{((화씨-32.0)*5/9):.4f}C')
#      elif menu == '2' :
#          섭씨 = float(input('섭씨'))
#          print(f'섭씨:{섭씨}C, 화씨:{((섭씨*9/5)+32):.4f}F')
#      else :
#          print ('끝')
#          break

# chr() 10진수->ASCII
# ord() ASCII->10진수
#
# print(f'{chr(63)}\n{chr(64)}')
# \n 줄바꿈

# raw string
# university = r"inha\nUniversity"
# print(university)
#
# university = "inha\nUnviersity"
# # print(university)
#
# slicing
# print(university[:4])
# print(university[:-11])
# print(len(university))
# print(university[0:len(university)])
# print(university[:15])
# print(university[::1])
# print(university[::2])

# concatenation
# number1=input("number1")
# number2=input("number2")
# print(number1+number2)
# 43
# print(number1*3) O
# print(number1+2) X

# name = 'Henny'
# print(name.replace('H', 'P'))
# print('P' + name[1:])
#
# numpy 행렬에서 slicing 활용
# [:] 전부
# [start:] start부터 끝까지
# [:end] 처음부터 end-1까지
# [start:end] start부터 end-1까지
# [::숫자] 숫자마다 건너뛰면서
# [start:end:숫자] start부터 end-1까지 숫자마다 건너뛰면서
# [start::숫자]start부터 끝까지 숫자마다 건너뛰면서
# [:end:숫자]처음부터 end까지 숫자마다 건너뛰면서

# split
# 리턴값은 list
# ['a','b','c']

# course="2024 KEB Bootcamp"
# print(course)
# # list_course = course.split()
# print(list_course)
# # ['2024', 'KEB', 'Bootcamp']
# 기본은 띄어쓰기로 분류
#
# list_course = course.split('B')
# print(list_course)
# ['2024 KE', ' ', 'ootcamp']
# 특정 값을 기준으로 분류

# numbers = input("first number second nubmer: ").split()
# # 하지만 넣을 때 숫자 두개를 띄어쓰기로 넣어야 함
# print(numbers[0]+numbers[1]) concatenation
# print(int(numbers[0])+int(numbers[1])) arithmetic operation

# csv = comma-separated values
# .split(,)

# .join()
# split반대개념 list를 문자열로
# subjects = ["python", 'c++', "database"]
# subjects_string = " / ".join(subjects)
# print(subjects_string)

# course="2024 KEB Bootcamp"
# print(course.replace('KEB','Inha'))
# print(course)
# course = course.replace('KEB','Inha')
# # 원본을 바꾸고 싶을땐 재할당
# print(course)

# course="KEB 2024 KEB .Bootcamp...!@#"
# course = course.replace('KEB','INHA',1)
# # .replace(old, new, count)
# print(course)
# print(course.strip(".!@#"))
# INHA 2024 KEB .Bootcamp
# 중간에 있는 문자는 제거할 수 없다
# print(course.find('KEB'))
# print(course.rfind('KEB'))
# print(course.index('KEB'))
# print(course.index('ㅋ'))

# .strip()
# 양측공백 제거
# .lstrip()
# 좌측공백 제거
# .rstrip()
# 우측공백 제거
# .strip('문자')
# 양측에 있는 단일문자 제거

# serach and select
# .startwith()
# .endswith()
# 문자의 시작과 끝을 검사
# True or False
#
# .find() 앞에서부터 몇번째인지
# .rfind() 뒤에서부터 몇번째인지
# 찾지 못하면 -1 반환
# .index() 동일 하지만 튜플, 리스트에서 주로
# .rindex()
# 찾지 못하면 예외처리
# ValueError: substring not found

# subjects = "python c++ database linux"
# subject = input("수강신청과목 입력 : ")
# if subjects.find(subject) != -1:
#     print(f"해당 과목은 존재합니다. 위치는 {subjects.find(subject)}번인덱스입니다.")
# else :
#     print('해당과목은 존재하지 않습니다')
#
#
#
# subjects = "python c++ database linux"
# subject = input("수강신청과목 입력 : ")
# if subjects.index(subject):
#     print(f"해당 과목은 존재합니다. 위치는 {subjects.index(subject)}번인덱스입니다.")
# else :
#     print('해당과목은 존재하지 않습니다')
#
#
#
# subjects = "python c++ database linux"
# subject = input("수강신청과목 입력 : ")
#     try:
#         print(f"해당 과목은 존재합니다. 위치는 {subjects.index(subject)}번인덱스입니다.")
#     except ValueError:
#         print('해당과목은 존재하지 않습니다')
# .isalnum()
# 모두 알파벳 or 숫자인가
# is -> True/False

# # Case
# .captialize()
# 첫글자 대문자
# .title()
# 항상 첫글자 대문자
# .upper()
# 모두 대문자
# .lower()
# 모두 소문자
# .swapcase()
# 대소문자 반대로
#
# # alginmnent
# () 총 몇칸
# .center()
# 가운데정렬
# .ljust()
# 좌측정렬
# .rjust()
# 우측정렬

# Formating
# old style %

# print('%s' % 42)
# # '42'
# 문자열 string
#
# print('%d' % 42)
# # '42'
# 10진수 decimal
#
# print('%x' % 42)
# # '2a'
# 16진수 hexadecimal
#
# print('%o' % 42)
# # '52'
# 8진수 octal
#
# -좌측정렬
# +우측정렬
# .최소너비


# new style

# {} .format(a,b)
# d={'a','b','c'} 딕셔너리

# subjects = {'python' : 'kim', 'c++' : 'sung', 'datastructure' : 'kim', 'database' : 'kang'}
# print("{0[python]}, {0[datastructure]}".format(subjects))
# 0은 딕셔너리 d에서 첫번째 인수
#
# ''채우기
# :< 좌측정렬
# :> 우측정렬
# :^ 중앙정렬
# :.^ 중앙정렬중 .으로 채우기

# f-stringss

#prime number
# number = int(input("input number : "))
# cnt = 0
# i = 1
# while i <= number:
#     if number%i == 0:
#         cnt=cnt+1
#     i = i+1
# if cnt == 2:
#     print(f'{number} is prime number')
# else :
#     print(f'{number} is not prime number')



# number = int(input("input number : "))
# cnt = 0
# i = 2
# while i < number:
#     if number%i == 0:
#         cnt=cnt+1
#         break
#     print(i, end=' ')
#     i = i+1
# if cnt == 0:
#     print(f'{number} is prime number')
# else :
#     print(f'{number} is not prime number')

# number = int(input("input number : "))
# is_prime = True #int->bool
# if number<2 :
#     print(f'{number} is not prime number')
# else :
#     i = 2
#     while i < number:
#         if number%i == 0:
#             is_prime = False # remove +
#             break
#         print(i, end=' ')
#         i = i+1
#     #if cnt==0:
#     if is_prime:
#         print(f'{number} is prime number')
#     else :
#         print(f'{number} is not prime number')

# word = 'thud'
# offset = 0
# while offset < len(word):
#     print(word[offset], end= ' ')
#     offset +=1
# # end= ' ' 가로로 배열
# print()
# #list tuple dic
# for letter in word:
#     print(letter)


word = 'thud'
for k in range (0, len(word), 1):
    print(word[k], end= ' ')

print()

for i in range(5):
    print(i)
