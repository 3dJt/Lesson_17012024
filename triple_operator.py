import random

numbers = []

for i in range(10):
    numbers.append(random.randint(0, 100))
print(numbers)

print("Число 13 есть в списке.") if 13 in numbers else print("Числа 13 нет в списке.")

