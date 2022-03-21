n, k = map(int, input().split())  # N과 K를 입력받기
a = list(map(int, input().split()))  # 배열 A의 모든 원소 입력받기
b = list(map(int, input().split()))  # 배열 A의 모든 원소 입력받기

a.sort() # 배열 a는 오름차순 정렬
b.sort(reverse=True) # 배열 b는 내림차순 정렬

# 첫번쨰 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:  # a의 원소가 b의 원소보다 크거나 같은때, 반복문 탈출
        break

print(sum(a)) # 배열 a의 모든 원소의 합을 출력
