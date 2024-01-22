# # def remove_duplicates(a):
# #     a
# #     pass
# #     result = []
# #     seen_chars =set
# #
# # result = remove_duplicates("programming")
# # print(result)
# #
# #
# #
# #
# # result = [] 중복문자를 제거하고 남은 결과
# # seen_chars = set() 이미 등장한 문자 set
# #
#
# abccc
#
# a결과
# b결과
# c결과
# c seen_chars
# c seen_chars
#
# for char in input_str: 입력글자 하나씩 순회
#     if char not in seen_chars: 한번도 등장한적 없다면
#         result.append(char) 결과에 추가해야되고
#         seen_chars.add(char) 이미 등장한 문자에도 추가해서 겹치는거 제거해야지
# #
# # return ''.join(result)
#
# my_string = "Hello, World!"
#
# for char in my_string:
#     print(char)


# def calculate_average(nums):
#     return sum(nums)/len(nums)
#
# numbers = [2, 5, 8, 10, 6]
# result = calculate_average(numbers)
# print(result)

# def calculate_difference(nums):
#     big_number = max(nums)
#     small_number = min(nums)
#     return big_number-small_number
#
# numbers = [3, 9, 2, 1, 7, 5]
# result = calculate_difference(numbers)
# print(result)


# def reverse_string(input_str):
#     string = list(input_str)
#     string.reverse()
#     a=''.join(string)
#     return a
#
# result = reverse_string("Hello, World!")
# print(result)
#
# def reverse_string(input_str):
#     return input_str[::-1]
# result = reverse_string("Hello, World!")
# print(result)

# def is_leap_year(year):
#     if (int(year)%4==0 and int(year)%100!=0) or (int(year)%400==0) :
#        return 1
#     else :
#         return 0

try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    result = num1 / num2

    print("나눗셈 결과:", result)

except ZeroDivisionError:
    print("Error: 0으로 나눌 수 없습니다.")

except ValueError:
    print("Error: 올바른 숫자를 입력하세요.")

except Exception as e:
    print(f"Error: 예외가 발생했습니다 - {e}")