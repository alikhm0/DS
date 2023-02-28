numbers_str = str(input())
numbers_str_sep = numbers_str.split(' ')
num_of_pesones = int(numbers_str_sep[0])
percent = int(numbers_str_sep[1])

names_str = str(input())
names_str_sep = names_str.split(',')

score_str = str(input())
score_int_sep = list(map(int, score_str.split(','))) 

data = [list(a) for a in zip(names_str_sep, score_int_sep)]

sort_baseon_score  = sorted(data,key=lambda l:l[1], reverse=True)
sort_baseon_name  = sorted(data,key=lambda l:l[0], reverse=False)

num_of_baseon_score = int(num_of_pesones * percent / 100)

res_list = []
for i in range(num_of_baseon_score):
    res_list.append(sort_baseon_score[i][0])

for i in range(num_of_pesones):
    if not sort_baseon_name[i][0] in res_list:
        res_list.append(sort_baseon_name[i][0])
# res_list = sort_baseon_score[0:4]
# for i in range(num_of_pesones):
#     if not sort_baseon_name[i] in res_list:
#         res_list.append(sort_baseon_name[i])
    

res_str = ""
for i in res_list:
    res_str = res_str + i + " "
print(res_str[:-1])