numberOfCranes = int(input("Введите общее количество сделанных журавликов "))
eachChild = int(numberOfCranes/6)
if numberOfCranes%6 == 0:
    print (f"Петя и Сережа сделали по  {eachChild} журавликов, а Катя - {eachChild*4}")
else:
     print (" Задача не имеет натурального решения")