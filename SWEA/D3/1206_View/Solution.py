#import sys
#sys.stdin = open(r"C:\Users\joohy\PycharmProjects\ssafy\View\input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        max_value = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])

        if max_value<arr[i]:
            building = arr[i]-max_value
            count += building

    print(f"#{test_case} {count}")