# [D3] 2805. 농작물 수확하기

- 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=
- 분류: 구현, 2차원 배열
- 풀이 날짜: 2026-11-20

## 접근 방법

- 가운데 열 `center = N // 2`를 기준으로 행마다 마름모 범위를 슬라이싱해서 합산
  - 위쪽 절반 (`y < center`): `maps[y][center-y : center+y+1]`
  - 가운데 행: 전체
  - 아래쪽 절반: `maps[y][y-center : N-y+center]`

## 시간 복잡도

O(N²)

## 회고 / 막혔던 점

- 한 줄이 공백 없이 붙어서 들어오므로 `split()` 말고 `strip()` 후 한 글자씩 `map(int, ...)`
- 마름모 범위(슬라이싱 시작/끝)를 정확히 지정하는 게 핵심
- 세 경우를 하나로 합칠 수도 있음: 가운데에서 떨어진 거리 `d = abs(y - center)`라 하면 범위는 `maps[y][d : N-d]`
- PyCharm에서 풀고 저장소로 옮김
