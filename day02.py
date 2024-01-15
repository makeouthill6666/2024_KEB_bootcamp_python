# print(0.1)
# print(1e-1)
univ = "Inha university"
print (univ)
print(univ[5])


subjects =['py','c+','li','ab']
print (subjects)
subjects[3] = 'linux'
print (subjects[3])


# 99 = 71

abc = 7
Abc = 9
ABC = 6
print (abc, Abc, ABC)

test9=87
# 9test=98
_9test=40
print(test9, _9test)

# y=x+5 NameError: name 'x' is not defined
# x=1
# Print(y)

print (type(3.14))
print(type(3.14) == float)
# print(ininstance(3.14, float))
# print(ininstance("a", float))

artists = ['BTS','Newjeans','a','b','c']
groups = artists
print(artists)
artists[2] ='z'
print(artists, groups)

money = (5,000,000)
print (money)
print (type(money))
cash = (5_000_000)
print (cash)
print (type(cash))

base_number = int(input('Input base nubmer : '))
exponent_number = int(input('Input base nubmer : '))
# f-string
print(f'밑 {base_number}, 지수 {exponent_number}, 결과 {base_number**exponent_number}')

# format function
print('밑 {0}, 지수 {1}, 결과 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
print('밑 {}, 지수 {}, 결과 {}'.format(base_number, exponent_number, pow(base_number, exponent_number)))

# c like
print('밑 %d, 지수 %d, 결과 %d' % (base_number, exponent_number, pow(base_number, exponent_number)))

