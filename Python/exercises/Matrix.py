row_1 = ["_","_","_"]
row_2 = ["_","_","_"]
row_3 = ["_","_","_"]
matrix = [row_1,row_2,row_3]

for i in matrix:
    print (i)

print
row = int(input("Type a row: "))
column = int(input ("Type a column: "))
matrix[row-1][column-1] = "x"

for i in matrix:
    print (i)
