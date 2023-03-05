input_line_number = int(input())

test_case = {}
for i in range(input_line_number):
    line = {}
    input_line1 = input().split()
    input_line2 = input().split()
    line['len'] = input_line1[0]
    line['condition'] = input_line1[1]
    line['plan'] = input_line2[0]
    test_case[i] = line
# print(products)



def maxZeros(N):

	maxm = -1

	cnt = 0
	while(N):
		if(not(N & 1)):
			cnt += 1
			N >>= 1
			maxm = max(maxm,cnt)
		else:
			maxm = max(maxm,cnt)
			cnt = 0
			N >>= 1

	return maxm


# N =  int(plan, 2)


for i in range(input_line_number):
	plan = test_case[i]['plan']
	condition = int(test_case[i]['condition'])
    # N =  int(plan, 2)
    # print(maxZeros(N))
	n= int(plan , 2)
	print(maxZeros(n) + condition)