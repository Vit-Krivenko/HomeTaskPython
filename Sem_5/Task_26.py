
def degree_of_number(num_1, num_2):
    if num_2 == 0:
        return 1
    else:
        return num_1 * degree_of_number(num_1,num_2-1)
    
a = int(input("Введите число которое будем возводить в степень "))
b = int(input("Введите степень в которую будем возводить число "))    
print(degree_of_number(a,b))
