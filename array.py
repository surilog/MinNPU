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

    def mac(self, pathern: 'Matrix') -> float | None:
            if self.n != pathern.n:
                print(f" 오류 : 행렬 크기가 맞지 않습니다. ({self.n}*{self.n}) VS ({pathern.n}*{pathern.n})")
                return None
            if not self.data or not pathern.data:
                print("오류 : 행렬 데이터가 없습니다. ")
                return None
    
            #제너레이터를 쓰면 0부터 더해서 초기화 필요 X
            total_sum = sum(
                self.data[r][c] * pathern.data[r][c]
                for r in range(self.n)
                for c in range(self.n)
            )
            """total_sum= sum(self.data[r][c] * pathern.data[r][c]for r in range(self.n)for c in range(self.n))"""
            """
            total_sum = 0.0
            
            for r in range(self.n):
                for c in range(self.n):
                    total_sum += self.data[r][c] * pathern.data[r][c]"""
            return float(total_sum)

    """  
    def get_val(self, r: int, c: int) -> float:
        return self.data[r][c] #(r,c) 위치 반환

    def set_val(self, r:int, c:int, val : float):
        self.data[r][c] = val# (r,c)위치에 값 저장
        """

    def display(self):
        print(f"[{self.n}x{self.n}  ")
        for row in self.data:
            print(row)

class Mode_1:

    def user_input(self, name:str, n_size: int) -> Matrix:
        mat=Matrix(n_size)
        print(f"\n[{name} 입력 ({n_size}x{n_size})]")
        print(f"아래에 {n_size}줄의 데이터를 한 번에 입력(또는 붙여넣기) 후, 엔터를 한 번 더 눌러주세요:")
                
        
        while True :
            lines = []
            while True:
                try:
                    line = input().strip()#공백 포함 해서 받음
                    if not line:
                        break
                    lines.append(line) #1줄 입력시 바로 lines에 저장
                except EOFError:
                    break

            if len(lines) != n_size : # 줄 수 검사!
                print(f"\n 오류 : 입력된 줄 수 ({len(lines)})가 N({n_size})과 맞지 않습니다.")
                continue

            final_arr = []
            valied = True
            for i, line in enumerate(lines,1): #각 줄의 '행'가 맞지 않으면 다시
                row = line.split()

                if len(row) != n_size:
                    print(f"\n 오류 : {i}번째 줄의 숫자 개수({len(row)}개)가 N({n_size})과 맞지 않습니다.")
                    valied =  False
                    break

                try:
                    rows = [int(x) for x in row]
                    final_arr.append(rows)

                except ValueError:
                    print(f"\n오류: {i}번째 숫자가 아닌값이 포함되어 있습니다.")
                    valied = False
                    break

            if valied:
                mat.data = final_arr
                print(" 성공적으로 입력을 완료했습니다!")
                return mat
            print("다시 입력해주세요! ")

    def mode1_flow(self) -> None:
        print("\n -----------------[모드 1] 사용자 직접 입력---------------")
        try:
            n_size = int(input("행렬 크기(N)를 입력하세요 (예: 3): "))
            if n_size<=0:
                print("크기는 1 이상의 양수여야 합니다.")
                return
            filter_a = self.user_input("필터 A (Cross)", n_size)
            filter_b = self.user_input("필터 B (X)", n_size)
            input_pattern = self.user_input("검사할 패턴", n_size)

            score_a = input_pattern.mac(filter_a)
            score_b = input_pattern.mac(filter_b)

            print("\n" + "="*40)
            print(f"필터 A(Cross)와의 Mac 점수 : {score_a}")
            print(f"필터 B(X)와의 Mac 점수 : {score_b}")
            print("=" * 40 + "\n")

        except ValueError:
            print("올바른 정수를 입려하세요.")


        
class Mode_2():
    def __init__(self):
        return 0



class Manager:
    def __init__(self):
        #__init__ 에서 인스턴스를 만들어 이전 실행결과를 기억!
        self.mode1_run = Mode_1()
        """self.mode2_run = Mode_2("data.json")"""

    def menu(self) -> None:
        print("1. 사용자 직접 입력 모드 (Mode1)")
        print("2. data.json 자동 일괄 분석 모드 (Mode2)")
        print("3. 프로그램 종료")

    def run(self) -> None:
        while True:
            self.menu()
            choice = input("원하는 모드를 선택하세요 : ").strip()

            if choice == "1":
                self.mode1_run.mode1_flow()
            elif choice == "2":
                self.mode2_run()
            elif choice == "3":
                print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
                break
            else:
                print("\n 올바른 번호를 입력해 주세요 (1, 2, 3).")


if __name__ == "__main__":
    manager = Manager()
    manager.run()

   
    """ try:
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
         my_matrix = Matrix(n_size)
        print("--기본 생성된 배열")
        my_matrix.display()

        for i in range(n_size):
            my_matrix.set_val(i,i,1.0)
        print("\n--대각선 값을 1로 변경한 후 배열")
        my_matrix.display()

    except ValueError:
        print("올바른 정수를 입력해주세요.")"""