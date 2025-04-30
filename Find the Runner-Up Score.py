#Run with scoreInput.txt
#python -u "Find the Runner-Up Score\!" < scoreInput.txt
#use \ because Python gets confused by the "!"

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    if len(set(arr)) > 1:
        print(sorted(set(arr))[-2])
    else:
        print(sorted(set(arr))[-1])
