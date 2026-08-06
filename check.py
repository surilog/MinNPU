def mac_operation_flow( pattern, filter_matrix):
        """
        2차원 패턴 배열과 필터 배열의 같은 위치 요소끼리 곱한 후 
        모든 값을 더한 '유사도 점수'를 반환합니다.
        """

        total_score = 0
        rows = len(pattern)
        cols= len(pattern)
        """total_score=[[0 for _ in range(rows)] for _ in range(cols)]"""
        for r in range(rows):
            for c in range(cols):
                total_score += pattern[r][c] * filter_matrix[r][c]

        return total_score



    # -----------------------------------------------------------
    # 데이터 정의 (0: 빈 공간, 1: 채워진 공간)
    # -----------------------------------------------------------

    # 입력 데이터: 십자가 모양
cross_input = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

# 필터 1: 십자가 필터
cross_filter = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

# 필터 2: X 필터
x_filter = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# -----------------------------------------------------------
# 실행 및 결과 확인
# -----------------------------------------------------------


score_case1 = mac_operation_flow(cross_input, cross_filter)
print(f"Case 1 (십자가 입력 × 십자가 필터) 점수: {score_case1}")  # 출력: 5 (일치)

score_case2 = mac_operation_flow(cross_input, x_filter)
print(f"Case 2 (십자가 입력 × X 필터) 점수: {score_case2}")  
