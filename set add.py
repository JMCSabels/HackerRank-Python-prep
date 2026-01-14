# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    num = int(input())
    s = set()

    for i in range(num):
        country = input()
        s.add(country)
        
    print(len(s))