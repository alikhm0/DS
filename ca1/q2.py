fist_line = str(input())
fist_line_sep = fist_line.split()
num_of_number = int(fist_line_sep[0])
num_of_try = int(fist_line_sep[1])

num_of_rock = str(input())
lst_rocks = []
for letter in num_of_rock:
    lst_rocks.append(int(letter))

trys = []
for i in range(num_of_try):
    trys.append(int(input()))

res = ""
for i in trys:
    temp_lst = lst_rocks[:i]
    temp = 0
    for j in temp_lst:
        temp = abs(i - j) + temp
        
    print(int(temp))

# print(res[:-1])
