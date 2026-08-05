import array

class Matrix:
    def __init__(self, n : int):
        self.n=n
        self.matrix = [[0 for _ in range(n)]for _ in range(n)]
          # 이중 for문(리스트 컴프리헨션)을 이용한 N * N 배열 초기화
        """ self.matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)
            self.matrix.append(row)    
        print(self.matrix)
        
        print(self.n)"""
    

    def get_val(self, r: int, c: int) -> float:
        return self.matrix[r][c] #(r,c) 위치 반환

    def set_val(self, r:int, c:int, val : float):
        self.matrix[r][c] = val# (r,c)위치에 값 저장

    def display(self):
        print(f"[{self.n}x{self.n}  Matrix]")
        for row in self.matrix:
            print(row)

    def user_input(self, name:str = "패턴"):
        print(f"\n[{name} 입력 ({self.n}x{self.n})]")
        print(f"아래에 {self.n}줄의 데이터를 한 번에 입력(또는 붙여넣기) 후, 엔터를 한 번 더 눌러주세요:")
                
        lines = []
        while True :
            try:
                line = input().strip()#공백 포함 해서 받음
                if not line:
                    break
                lines.append(line) #1줄 입력시 바로 lines에 저장
            except EOFError:
                break

        if len(lines) != self.n : # 열이 맞지 않으면 다시
            print(f"\n 오류 : 입력된 줄 수 ({len(lines)})가 N({self.n})과 맞지 않습니다.")
            return False

        temp_matrix = []
        for i, line in enumerate(lines,1): #각 줄의 '오'가 맞지 않으면 다시
            tokens = line.split()
            if len(tokens) != self.n:
                print(f"\n 오류 : {i}번째 줄의 숫자 개수({len(tokens)}개)가 N({self.n})과 맞지 않습니다.")
                return False

            try:
                row_vals = [int(x) for x in tokens]
                temp_matrix.append(row_vals)
            except ValueError:
                print(f"\n오류: {i+1}번째 숫자가 아닌값이 포함되어 있습니다.")
                return False

        for r in range(self.n):
            for c in range(self.n):
                self.set_val(r,c,temp_matrix)

        print("\n 성공적으로 입력을 완료했습니다!")
        return True




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
    def decide_pattern(self, score_cross, score_x):
        return


if __name__ == "__main__":
    try:
        n_size = int(input("만들고 싶은 N x N 배열의 크기(N)를 입력하세요:  "))

        pattern=Matrix(n_size)
        while True:
            if pattern.user_input(name="사용자 패턴"):
                break
            print("다시 시도해 주세요.\n")

        # 결과 확인
        pattern.display()

    except ValueError:
        print("N은 정수여야 합니다.")
        """ my_matrix = Matrix(n_size)
        print("--기본 생성된 배열")
        my_matrix.display()

        for i in range(n_size):
            my_matrix.set_val(i,i,1.0)
        print("\n--대각선 값을 1로 변경한 후 배열")
        my_matrix.display()"""

    except ValueError:
        print("올바른 정수를 입력해주세요.")