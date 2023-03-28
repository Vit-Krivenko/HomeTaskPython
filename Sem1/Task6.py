lukkyTicket = int(input("Введите шестизначный номер билета "))
sum1 = 0
sum2 = 0
if 99999 < lukkyTicket < 1000000:
    for i in range(3):
        sum1 = sum1 + lukkyTicket%10
        lukkyTicket = lukkyTicket//10
    for i in range(3):
        sum2 = sum2 + lukkyTicket%10
        lukkyTicket = lukkyTicket//10
    if sum1 == sum2:
        print("Билет счастливый!!!")
    else:
        print("Билет обычный")
else:
    print("Это не шестизначный номер!!!")