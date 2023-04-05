n = (int(input("Введите количество элементов массива: ")))
a =[]
a = [int(input("Введите элемент массива:")) for i in range(n)]
k = (int(input("Введите искомое число: ")))
p = abs(abs(a[0])-abs(k))
x = a[0]
for i in range (n-1):
    if abs(abs(a[i+1])-abs(k)) < p:
        p = abs(abs(a[i+1])-abs(k))
        x = a[i+1]
print(f"Самый близкий по величине элемент к искомому: {x}")
