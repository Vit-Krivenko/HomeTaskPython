number = 0
while 99 > number or number>1000:
    number = int(input("Введите трехзначное число "))
sum = 0
for i in range(3):
    sum = sum + number%10
    number = number//10
print("Сумма цифр числа =", sum)
