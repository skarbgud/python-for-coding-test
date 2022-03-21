# 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1] # 두번째 키워드에 대하여 정렬


result = sorted(array, key=setting)
print(result)
