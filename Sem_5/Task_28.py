def sum(num_1, num_2):
    if num_1 == 0:
        return num_2
    else:
        return sum(num_1-1,num_2+1)
    
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))    
print(f"Сумма чисел a и b будет {sum(a,b)}")