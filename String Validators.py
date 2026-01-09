if __name__ == '__main__':
    s = input()
    #1 alnum
    hasAlnum = any(x.isalnum() for x in s)
    #2 alpha
    hasAlpha = any(x.isalpha() for x in s)
    #3 digits
    hasDigits = any(x.isnumeric() for x in s)    
    #4 lowercase
    hasLower = any(x.islower() for x in s)
    #5 uppercase
    hasUpper = any(x.isupper() for x in s)
    print(hasAlnum, hasAlpha, hasDigits, hasLower, hasUpper, sep="\n")