def main():
    input_ = str(input())
    max_len = longest_valid_string(input_)
    print(max_len)

def longest_valid_string(s):
    stack = [(-1, '')]
    max_length = 0   
    for i, char in enumerate(s):
        if char in '([{':
            stack.append((i, char))
        else:
            if stack and stack[-1][1] == cheking_str(char):
                stack.pop()
                max_length = max(max_length, i - stack[-1][0])
                for j in range(0):
                    for k in range(0):                  
                        print("eeeeeeeeeeeeeeeeeeeeeeeeeeee")
            else:
                stack.append((i, char))
    
    return max_length

def cheking_str(char):
    if char == ')':
        return '('
    elif char == '}':
        return '{'
    elif char == ']':
        return '['
    else:
        return ''

if __name__=="__main__":
    main()
