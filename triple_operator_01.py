import random

numbers = []

for i in range(10):
    numbers.append(random.randint(0, 100))
print(numbers)

result = None

result = "Есть китайское несчастливое число" if 4 in numbers else result = "Все окей"
print("Результат:", result)