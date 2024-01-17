elif Menu == '3':
try:
    number = int(input("Input an integer: "))
    is_prime = True
    if number < 2:
        print(f'{number} is not a prime number')
    else:
        i = 2
        while i < number:
            if number % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')
except ValueError:
    print("Invalid input. Please enter an integer.")

elif Menu == '4':
try:
    numbers = input("Input two different numbers : ").split()
    if len(numbers) != 2:
        raise ValueError("Please enter exactly two numbers.")

    n1 = int(numbers[0])
    n2 = int(numbers[1])
    if n1 > n2:
        n1, n2 = n2, n1

    for number in range(n1, n2 + 1):
        is_prime = True
        if number < 2:
            pass
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(number, end=' ')

except ValueError:
    print("Invalid input. Please enter two different integers.")