# # print(0.1)
# # print(1e-1)
# univ = "Inha university"
# print (univ)
# print(univ[5])
#
#
# subjects =['py','c+','li','ab']
# print (subjects)
# subjects[3] = 'linux'
# print (subjects[3])
#
#
# # 99 = 71
#
# abc = 7
# Abc = 9
# ABC = 6
# print (abc, Abc, ABC)
#
# test9=87
# # 9test=98
# _9test=40
# print(test9, _9test)
#
# # y=x+5 NameError: name 'x' is not defined
# # x=1
# # Print(y)
#
# print (type(3.14))
# print(type(3.14) == float)
# print(isinstance(3.14, float))
# print(isinstance("a", float))

# while True :
#     Menu = input("1) Celsius to Fahrenheit 2)Fahrenheit to Celsius 3) Quit : ")
#     print()
#     if Menu not in ['1', '2', '3'] :
#         print("Please choose from the menu.")
#     if Menu == '1' :
#             Celsius = (float(input('Input Celsius : ')))
#             if (isinstance(Celsius,int) or isinstance(Celsius, float)):
#                 Celsius=(float(input('Input Celsius : ')))
#                 print(f'{Celsius}C, {(Celsius * 9 / 5) + 32:.4f}F')
#             else :
#                 print("Invalid input. Please enter the number.")
#     elif Menu == '2' :
#         try :
#             Fahrenheit = float(input('Input Fahrenheit : '))
#             print(f'{Fahrenheit}F, {(Fahrenheit-32)*5/9:.4f}C')
#         except ValueError :
#             print("Invalid input. Please enter the number.")
#     elif Menu == '3' :
#         print('Terminating the program.')
#         break
#     print()

# artists = ['BTS','Newjeans','a','b','c']
# groups = artists
# print(artists)
# artists[2] ='z'
# print(artists, groups)
#
# money = (5,000,000)
# print (money)
# print (type(money))
# cash = (5_000_000)
# print (cash)
# print (type(cash))

# base_number = int(input('Input base nubmer : '))
# exponent_number = int(input('Input base nubmer : '))
# # f-string
# print(f'밑 {base_number}, 지수 {exponent_number}, 결과 {base_number**exponent_number}')
#
# # format function
# print('밑 {0}, 지수 {1}, 결과 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
# print('밑 {}, 지수 {}, 결과 {}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
#
# # c like
# print('밑 %d, 지수 %d, 결과 %d' % (base_number, exponent_number, pow(base_number, exponent_number)))

# First_number = int(input("First number : "))
# Second_number = int(input("Second Number : "))
#
# quotient = First_number // Second_number
# remainder = First_number % Second_number
# print (f'몫{quotient}, 나머지{remainder}')
#
#
# quotient = First_number // Second_number
# remainder = First_number % Second_number
# print(f'몫{divmod(First_number, Second_number)[0]} 나머지{divmod(First_number, Second_number)[1]}')

# dec = 65
# octal = 0o101
# hexadecimal = 0x41
# binary = 0b01000001
#
# print(dec, octal, hexadecimal, binary)
#
# print(chr(binary))
#
# print(ord('0'))
#
# # (32°F − 32) × 5/9 = 0°C
# fahrenheit = float(input('Input Fahrenheit : '))
# print(f'Fahrenheit: {fahrenheit}F, Celsius : {((fahrenheit-32.0) * 5/9):.4f}C')

#(0°C × 9/5) + 32 = 32°F
# menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Quit : ")
# if menu == '1':
#     fahrenheit = float(input('Input Fahrenheit : '))
#     print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit-32.0) * 5/9):.4f}C')
# elif menu == '2':
#     celsius = float(input('Input Celsius : '))
#     print(f'Celsius: {celsius}C, Fahrenheit: {((celsius*9/5)+32):.4f}F ')
# else :
#     print('Terminate Program.')

# print(int('11', 16))
# print(int('1A', 16))
# # print(int('A')+ int('B')) = x
#
# print(10**100)

# temp = []
# if temp :
#     print("존재")
# else :
#     print("공백")

# letter = input('Input alphabet : ')
# vowels = {'a', 'e', 'i', 'o', 'u'}
# if letter in vowels:
#     print(f'{letter} is a vowel')
# else:
#     print(f'{letter} is a consonant')

# menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Quit : ")
# if menu == '1':
#     fahrenheit = float(input('Input Fahrenheit : '))
#     print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit-32.0) * 5/9):.4f}C')
# elif menu == '2':
#     celsius = float(input('Input Celsius : '))
#     print(f'Celsius: {celsius}C, Fahrenheit: {((celsius*9/5)+32):.4f}F ')
# else :
#     print('Terminate Program.')



menu = input("1, 2, 3")
if menu == '1' :
    화씨 = float(input('화씨 넣어'))
    print((화씨-32)*5/9)
















