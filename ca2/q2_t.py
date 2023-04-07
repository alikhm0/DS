def main():
    n, k = map(int, input().split())
    array_list = list(map(int, input().split()))
    num_of_question = int(input())
    right_of_range = []
    for i in range(num_of_question):
        number = int(input())
        right_of_range.append(number)

    max_values = []
    max_value = max(array_list[:k])
    max_values.append(max_value)
    for i in range(1, n-k+1):
        new_value = array_list[i+k-1]
        if new_value > max_value:
            max_value = new_value
        elif array_list[i-1] == max_value:
            max_value = max(array_list[i:i+k])
        max_values.append(max_value)

    for i in right_of_range:
        print(max_values[i - k])

if __name__ == "__main__":
    main()
