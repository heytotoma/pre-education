'''
3.
앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
'''
# <입력>
ls=[4,3,2,1,8,7,5,10,11,16,21,6] # 12개

def bubble_sort(ls):
    for i in range(len(ls) - 1, 0, -1): # range(11,0,-1), 역순
        for j in range(0, i): # i : 11~0
            if ls[j] > ls[j + 1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]  # 자리 바꿈
    return ls

print(bubble_sort(ls))

# <출력>
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21]