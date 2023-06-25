import fractions

first: str = str(input("Введите числитель первой дроби "))
second: str = str(input("Введите знаменатель первой дроби "))
third: str = str(input("Введите числитель второй дроби "))
fourth: str = str(input("Введите знаменатель второй дроби "))
number1: int = int(first)
number2: int = int(second)
number3: int = int(third)
number4: int = int(fourth)


result1 = (number1 / number2 ) + (number3 / number4)
result2 = (number1 / number2 ) * (number3 / number4)
print(result1)
print(result2)
firstfraction = fractions.Fraction(number1, number2)
secondfraction = fractions.Fraction(number3, number4)
result3 = firstfraction + secondfraction
result4 = firstfraction * secondfraction
print(result3)
print(result4)