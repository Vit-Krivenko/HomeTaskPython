n = (int(input("Введите количество элементов массива: ")))
a =[]
count = 0
a = [int(input("Введите элемент массива:")) for i in range(n)]
k = (int(input("Введите искомое число: ")))

for i in range (n):
    if a[i]==k:
        count+=1
print(f"Количество искомых элементов в массиве: {count}")