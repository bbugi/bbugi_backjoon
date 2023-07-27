def solution(arr):
    cnt = 0
    while True:
        tmp = [0]*len(arr)
        cnt += 1
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                tmp[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                tmp[i] = arr[i] * 2 + 1
            else:
                tmp[i] = arr[i]
        
        if arr == tmp :
            return cnt - 1
            break
        else:
            arr = tmp
            continue
                