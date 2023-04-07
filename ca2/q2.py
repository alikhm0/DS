def main():
    n ,k = (str(input())).split()
    n ,k = int(n) , int(k)
    array_list = (input()).split()
    for i in range(len(array_list)):
        array_list[i] = int(array_list[i])
    num_of_question = int(input())
    right_of_range = []
    for i in range(num_of_question):
        number = int(input())
        right_of_range.append(number)
  
    for i in right_of_range:
        calc(array_list , i , k)

def calc(list , value,k):
    check_lst = []
    bigest = 0
    for i in range(k):
        check_lst.append(list[value-(i+1)])
        if check_lst[i] > bigest:
            bigest = check_lst[i]
    print(bigest)

if __name__=="__main__":
    main()
