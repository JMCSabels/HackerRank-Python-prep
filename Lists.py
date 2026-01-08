if __name__ == '__main__':
    N = int(input())
    eList = []
    
    for _ in range(N):
        command = input().split()
        #split the input
        #have a function for each type of input and what it's supposed to do
        match command[0]:
            case "append":
                eList.append(int(command[1]))
            case "insert":
                eList.insert(int(command[1]), int(command[2]))
            case "print":
                print(eList)
            case "remove":
                eList.remove(int(command[1]))
            case "sort":
                eList.sort()
            case "pop":
                eList.pop()
            case "reverse":
                eList.reverse()