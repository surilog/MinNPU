import array

class Matrix:
    def __init__(self, size : int):
        self.n=size
        self.data = []
          # 이중 for문(리스트 컴프리헨션)을 이용한 N * N 배열 초기화a
        """ self.matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)
            self.matrix.append(row)    
        print(self.matrix)
        
        print(self.n)"""
    

    def get_val(self, r: int, c: int) -> float:
        return self.data[r][c] #(r,c) 위치 반환

    def set_val(self, r:int, c:int, val : float):
        self.data[r][c] = val# (r,c)위치에 값 저장

    def display(self):
        print(f"[{self.n}x{self.n}  Matrix]")
        for row in self.data:
            print(row)

    def user_input(self, name:str = "패턴") -> bool:
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

        if len(lines) != self.n : # 줄 수 검사!
            print(f"\n 오류 : 입력된 줄 수 ({len(lines)})가 N({self.n})과 맞지 않습니다.")
            return False

        final_arr = []
        for i, line in enumerate(lines,1): #각 줄의 '행'가 맞지 않으면 다시
            row = line.split()
            if len(row) != self.n:
                print(f"\n 오류 : {i}번째 줄의 숫자 개수({len(row)}개)가 N({self.n})과 맞지 않습니다.")
                return False

            try:
                rows = [int(x) for x in row]
                final_arr.append(rows)
            except ValueError:
                print(f"\n오류: {i+1}번째 숫자가 아닌값이 포함되어 있습니다.")
                return False

        self.data = final_arr
        print(" 성공적으로 입력을 완료했습니다!")
        return True

        print("\n 성공적으로 입력을 완료했습니다!")
        return True




    


if __name__ == "__main__":
    try:
        n_size = int(input("만들고 싶은 N x N 배열의 크기(N)를 입력하세요:  "))

        if n_size <= 0:
            print("크기는 1 이상의 양수여야 합니다! ")
        else:
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