# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_num(num: int, mode: str) -> str:
    result = ''
    convert: int = 1
    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8
        case "hex":
            convert = 16
    while num >= 1:
        res = num % convert
        result += str(res)
        num = num // convert
    return result[::-1]


print(convert_num(88, mode="bin"), f"assert: {bin(88)}")
print(convert_num(88, mode="oct"), f"assert: {oct(88)}")
print(convert_num(88, mode="hex"), f"assert: {hex(88)}")
