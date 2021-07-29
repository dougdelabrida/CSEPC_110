number_of_rows_columns = int(input("How many columns and rows do you want in your multiplication table? "))

for column in range(1, number_of_rows_columns + 1):
    print()
    for row in range(1, number_of_rows_columns + 1):
        number = column * row
        if ((number_of_rows_columns * number_of_rows_columns) > 1000):
            print(f"{number:5}", end = "")
        else:
            print(f"{number:4}", end = "")
