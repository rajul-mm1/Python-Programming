def count_grt_no(arr):
    max_so_far = float('-inf')
    count = 0
    for num in arr:
        if num > max_so_far:
            count+=1
            max_so_far = num
    return count

n = int(input())
arr = list(map(int, input().split()))
print(count_grt_no(arr))