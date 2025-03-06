from collections import deque

def main():
    N,M=map(int,input().split())

    Q=deque([[a] for a in range(1,M+1)])
    result = []
    count = 0
    
    while Q:
        A=Q.popleft()
        print(Q.popleft())
        if len(A)==N:
            result.append(A)
            count += 1
        else:
            for b in range(A[-1]+10, M+1-(N-len(A)-1)*10):
                Q.append(A+[b])

    print(count)
if __name__ == "__main__":
    main()

