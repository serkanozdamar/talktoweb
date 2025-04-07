my_list = [1,2,3,4,5,6]

"""
int ali[3][5] = {
                {1,2,3,4,5},
                {11,21,31,41,51},
                {12,23,33,43,53}
                }
                
 ali[1][1] ~ali[6]
 ali[1][4] ~ali[9]
 ali[0]
 ali[1]
 ali[2][4]
 for(int row=0;row<3;row++)
    for(int column=0;column<5;column++){
            printf(column[row][column]);
    }
   
"""
x = my_list[0]

"""
6 X 2
"""
my_list2 = [[1, "a"],
            [2, "a"],
            [3, "a"],
            [4, "a"],
            [5, "a"],
            [6, "a"]
            ]
y = my_list2[0][0]
print(my_list2[0][1])

row = len(my_list2)
column = len(my_list2[0])

my_list3 = [[1, "a", 5,6],
            [2, "a", "ali"],
            [3, "a"],
            [4, "a", "veli", (2,3), {}],
            [5, "a"],
            [6, "a"]
            ]
my_list3[3][3][0] = "ali"
for i in range(len(my_list3)):
    for j in range(len(my_list3[i])):
        print(f"my_list3[{i}][{j}]: {my_list3[i][j]}")