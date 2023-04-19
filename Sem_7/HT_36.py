def print_operation_table(operation, num_rows = 6 , num_columns = 6 ):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            if i == 1 or j == 1:
                print(i*j, end=" ")
            if i > 1 and j > 1:
                print(operation(i,j), end = " ")
        print()

print_operation_table(lambda x , y : x * y)