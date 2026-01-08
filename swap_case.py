def swap_case(s):
    new_S = ""
    
    for letter in s:
        if letter.islower():
            new_S += letter.upper()
        else:
            new_S += letter.lower()

    
    return new_S

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)