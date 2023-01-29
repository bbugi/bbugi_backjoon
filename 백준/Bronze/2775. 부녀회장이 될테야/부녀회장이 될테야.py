import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case): # 테스트 케이스만큼 입력 반복
    k = int(input()) # 층
    n = int(input()) # 호수
    

    apt = [[1] * n for _ in range(k+1)]
    # print(apt)

    # 아파트 0층의 거주민 수
    apt[0] = [i for i in range(1, n+1)]
    # print(apt)

    # 아파트 층별 1호 거주민 수 = 항상 1명

    def sum_kn(floor, ho):
        sum_ho = 0
        for i in range(ho+1):
            sum_ho += apt[floor-1][i]
        # print(sum_ho)
        return sum_ho
            
    # # 아파트 k층 n호 거주민 수 = k-1층의 1호~n호 까지의 거주민 수 합
    for i in range(1, k+1):
        for j in range(1,n):
            apt[i][j] = sum_kn(i,j)
    # print(apt)

    print(apt[k][n-1])