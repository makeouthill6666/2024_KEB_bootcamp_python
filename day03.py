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
numpy 행렬에서 slicing 활용
[:] 전부
[start:] start부터 끝까지
[:end] 처음부터 end-1까지
[start:end] start부터 end-1까지
[::숫자] 숫자마다 건너뛰면서
[start:end:숫자] start부터 end-1까지 숫자마다 건너뛰면서
[start::숫자]start부터 끝까지 숫자마다 건너뛰면서
[:end:숫자]처음부터 end까지 숫자마다 건너뛰면서

slicing
print(university[:4])
print(university[:-11])
print(len(university))
print(university[0:len(university)])
print(university[:15])
print(university[::1])
print(university[::2])