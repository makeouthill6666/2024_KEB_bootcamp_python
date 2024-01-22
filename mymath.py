def isprime(n) -> bool:
    """
    매개변수로 넘겨받은 수가 소수인지 여부를 boolean으로 리턴
    : param n: 판정할 매개변수
    : return: 소수면 True 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
print(isprime.__doc__)

def c_to_f(Celsius):
    if Celsius < -273.15:
        print("Invalid input. Temperature cannot be below absolute zero.")
        return None
    return (Celsius * 9/5) + 32

def f_to_c(Fahrenheit):
    if Fahrenheit < -459.67:
        print("Invalid input. Temperature cannot be below absolute zero.")
        return None
    return (Fahrenheit - 32) * 5/9