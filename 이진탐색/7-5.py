def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# N(가계의 부품 수) 입력
n = int(input())
# 가계에 있는 전체 부품의 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()  # 이진 탐색 수행하기 위해 사전에 정렬
# M(손님이 확인 요청한 부품의 개수) 입력
m = int(input())
# 손님이 확인 욫ㅇ한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
