# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    happiness = 0
    inp = input().split(" ")
    array = list(map(int, input().split()))
    good = set(map(int, input().split()))
    bad = set(map(int, input().split()))
    for i in array:
        if i in good:
            happiness += 1
        if i in bad:
            happiness-= 1
    print(happiness)