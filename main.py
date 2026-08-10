import array
import re
import json
import time

EPSILON = 1e-9
def only_normal(label_raw: str) -> str:
        if not label_raw:
            return "UNKNOWN"

        clean = str(label_raw).strip().lower()

        if clean in ["+","cross"]:
            return "Cross"
        elif clean in ["x"]:
            return "X"
        else:
            return "UNKNOWN"


class Matrix:
    def __init__(self, size : int, data:list=None):
        self.n=size
        self.data = data if data is not None else []
          # 이중 for문(리스트 컴프리헨션)을 이용한 N * N 배열 초기화a
        """ self.matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)
            self.matrix.append(row)    
        print(self.matrix)
        
        print(self.n)"""
    def time_ch(self, start_time : int):
        self.start_time = time.time()

        self.end_time = time.time()

        # 연산 함수 호출하고 연산 수행 시 동시에 { start_time = time.time() 시간 측정시작! 하고 연산 끝나면 
        #  end_time = time.time()후} result_time =end_time - start_time 
        # 근데 sum_time+=reuslt_time / average_time= sum_time/10

        """크기별 MAC 연산 시간을 ms 단위로 측정해야 한다.
        최소 기준: 각 크기별로 MAC 연산을 10회 반복 측정 후 평균 시간을 출력한다.
        시간 측정은 I/O(입력/출력/파일 읽기) 시간을 제외하고 “연산 함수 호출 구간” 중심으로 수행하는 것을 권장한다.
        """
    def mac(self, pathern: 'Matrix') -> tuple[float,float]  | None:  
            #튜플 사용 이유 새롭게 알게 된 점: 한 번 생성되면 내부 값을 변경할 수 없다! => 즉 고정데이터로 활용 가능
            if self.n != pathern.n:
                print(f" 오류 : 행렬 크기가 맞지 않습니다. ({self.n}*{self.n}) VS ({pathern.n}*{pathern.n})")
                return None
            if not self.data or not pathern.data:
                print("오류 : 행렬 데이터가 없습니다. ")
                return None
    

            num_runs = 10
            full_time = 0.0
            total_sum=0.0
            #제너레이터를 쓰면 0부터 더해서 초기화 필요 X
            for __ in range(num_runs):
                start_time = time.perf_counter() # time.time()대신 사용 이유: 마이크로처 단위의 매우 높은 정밀도
                total_sum = sum(              
                    self.data[r][c] * pathern.data[r][c]
                    for r in range(self.n)
                    for c in range(self.n)
                )
                end_time = time.perf_counter()
                full_time += end_time - start_time
            avg_time = (full_time / num_runs) * 1000.0 #밀리 초는 1초의 1천분의 1

            """total_sum= sum(self.data[r][c] * pathern.data[r][c]for r in range(self.n)for c in range(self.n))"""
            """
            total_sum = 0.0
            
            for r in range(self.n):
                for c in range(self.n):
                    total_sum += self.data[r][c] * pathern.data[r][c]"""
            return total_sum, avg_time

    """  
    def get_val(self, r: int, c: int) -> float:
        return self.data[r][c] #(r,c) 위치 반환

    def set_val(self, r:int, c:int, val : float):
        self.data[r][c] = val# (r,c)위치에 값 저장
    """

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
                    rows = [float(x) for x in row]
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
            print("\n [1]필터 입력")
            print("\n ---------------------------------------")
            filter_a = self.user_input("필터 A (Cross)", n_size)
            filter_b = self.user_input("필터 B (X)", n_size)

            print("\n [2]패턴 입력")
            print("\n ---------------------------------------")
            input_pattern = self.user_input("검사할 패턴", n_size)

            a_mac = input_pattern.mac(filter_a)
            b_mac = input_pattern.mac(filter_b)


            if not a_mac or not b_mac:
                print("연산 실패로 진행을 중단합니다.")
                return
            score_a, a_time = a_mac # 튜플 언패킹 활용!  tuple=(3, 5) "반환 값 가정 /
            # a,b = tuple 할 경우 왼쪽부터 a=3 ,b=5의 값이 들어간다!
            score_b, b_time =b_mac
            avg_time= (a_time + b_time)/2

            if abs(score_b -score_a) <EPSILON:
                win_score="판정불가 (|A-B| < 1e-9)"
            elif score_a > score_b:
                win_score="A"
            else :
                win_score="B"
            

            print("\n [3]MAC 결과")
            print("\n ---------------------------------------")
            print("\n" + "="*40)
            print(f"필터 A(Cross)와의 Mac 점수 : {score_a}")
            print(f"필터 B(X)와의 Mac 점수 : {score_b}")
            print(f"연산 시간(평균/10회): {avg_time:.3f}")
            print(f"판정: {win_score}")
            print("=" * 40 + "\n")

        except ValueError:
            print("올바른 정수를 입력하세요.")


        
class Mode_2():
    """[모드 2] JSON 기반 데이터 일괄 검수 및 분석 실행기"""
    def __init__(self, json_path: str = "data.json"):
        self.json_path = json_path
        self.filters = {}
        self.patterns = {}

    def load_data(self) -> bool:
        try:
            with open(self.json_path,"r",encoding="utf-8") as f:
                read_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[오류] 파일 로드 실패 : {e}")
            return False

        raw_filters = read_data.get("filters",{})
        raw_patterns = read_data.get("patterns",{})
        self.filters = {}
        self.patterns = {}

        for f_key, f_value in raw_filters.items():
            try:
                n_size = int(f_key.split('_')[1])
            except(IndexError,ValueError) as e:
                print("[오류]")
                n_size = None

            self.filters[f_key] = {
                "n_size" : n_size,
                "cross" : f_value.get("cross",[]),
                "x" : f_value.get("x",[])
            }
            
        for p_key, p_value in raw_patterns.items():
            try:
                n_size = int(p_key.split('_')[1])
            except(IndexError,ValueError):
                print("[오류]")
                n_size = None

            self.patterns[p_key] = {
                "n_size" : n_size,
                "input" : p_value.get("input",[]),
                "expected" : p_value.get("expected","UNKNOWN")
            }

        return True
 
    def check_filter_pattern(self, p_key : str) -> tuple[bool,str]:
        p_data = self.patterns.get(p_key,{})
        n_size = p_data.get("n_size",0)
        input_data = p_data.get("input",[])

        if n_size is None or n_size <=0:
            return False, "N 크기 파싱 실패"

        f_key = f"size_{n_size}"
        f_data = self.filters.get(f_key, {})
        cross_filter = f_data.get("cross",{})
        x_filter = f_data.get("x",{})
        targets = [
            ("입력 패턴 ", input_data),
            ("Cross 필터", cross_filter),
            ("X 필터", x_filter)
        ]

        for name, input in targets:
            if len(input) != n_size or any(len(row) != n_size for row in input):
                return False, f"{name} 크기 불일치 (N={n_size})"# input, Cross, X필터 중 에러뜨면 에러 뜬 곳과 이유 반환!
        return True, "정상"
    """1. N 크기가 올바른 숫자인지 검사 (n_size > 0)
            2. input 데이터가 N개 행 & 각 행이 N개 열인지 검사
            3. Cross 필터 데이터가 N x N 인지 검사
            4. X 필터 데이터가 N x N 인지 검사
            => 하나라도 틀리면 (False, "에러 이유") 반환!"""
    
    def analyze_pattern(self, p_key: str)->dict:

        p_data = self.patterns.get(p_key, {}) 
        n_size = p_data.get("n_size",0)
        input_data = p_data.get("input",[])
        f_expected = p_data.get("expected","UNKNOWN")

        #정규화 하려면 패턴 값에 따른 필터 필요!
        f_key = f"size_{n_size}"
        f_data = self.filters.get(f_key,{})
        cross_data = f_data.get("cross",[])
        x_data = f_data.get("x",[])

        input_mat = Matrix(n_size, input_data) # 크기 정보와 데이터 묶어서 객체로 만듬.(바로 mac함수 사용)
        cross_mat = Matrix(n_size, cross_data)
        x_mat = Matrix(n_size, x_data)

        score_cross, time_cross=input_mat.mac(cross_mat)
        score_x, time_x = input_mat.mac(x_mat)

        #함수 호출을 어떻게 할건지? 과정부터 정하자!
        
        expected = only_normal(f_expected)#라벨까지 해주고 
        avg_time = (time_cross + time_x)/2.0 #각각 10회면 총 20회이니 2로 나눔

        
       
        """
        run() -> mode2_flow() -> load_data()호출 -> [1]필터로드 화면 출력 -> 패턴 수 만큼 반복문 실행(for p_key in self.pattern.key()) 
        -> check_filter_pattern()호출 -> analyze_pattern(p_key) 호출 ->dict형태로 반환 ->  [2]패턴 분석 결과 화면 출력
        """

        if abs(score_cross - score_x) < EPSILON:
            result =  "UNDECIDED"
            status = "FAIL"
            reason = "(동점(UNDECIDED)처리 규칙에 따른 FAIL)"
        
        elif score_x < score_cross:
            result = "Cross"
             
            if expected == "Cross" :
                status = "PASS"
                reason = "정상" 
            else:
                status = "FAIL"
                reason = f"불일치(예측: {expected} / 결과: Cross)에 따른 FAIL"
            
        else :
            result = "X"
            if expected == "X": 
                status = "PASS" 
                reason= "정상"
            else :
                status  ="FAIL"
                reason = f"불일치(예측: {expected} / 결과: X)에 따른 FAIL"

        return {
            "score_cross" : score_cross,
            "score_x" : score_x,
            "expected" : expected,
            "result" : result,
            "status" : status,
            "reason" : reason,
            "avg_time" : avg_time
        }
        """ [2-1단계] Matrix 객체 생성      ──> 2D 데이터 리스트를 Matrix 클래스로 변환
        [2-2단계] MAC 점수 연산         ──> input_mat.mac()으로 Cross, X 점수 계산
        [2-3단계] 라벨 정규화          ──> only_normal()로 expected 라벨 정리
        [2-4단계] 점수 비교 및 판정/리턴 ──> 크기 비교, 동점 처리(UNDECIDED), dict 반환"""

        """input_mat = Matrix(n_size, input_data)
            cross_mat = Matrix(n_size, cross_data)
            x_mat     = Matrix(n_size, x_data)"""

# 핵심 동작 흐름


    def mode2_flow(self) -> None:
        print(f"\n -------[모드 2] {self.json_path} 자동 일괄 분석 ---------------")
        if not self.load_data():
            print("[오류] 데이터를 불러오지 못해 분석을 중단합니다.")
            return
        """
        run() -> mode2_flow() -> load_data()호출 -> [1]필터로드 화면 출력 -> 패턴 수 만큼 반복문 실행(for p_key in self.pattern.key()) 
        -> check_filter_pattern()호출 -> analyze_pattern(p_key) 호출 ->dict형태로 반환 ->  [2]패턴 분석 결과 화면 출력
        """
        print("\n#---------------------------------------")
        print("# [1] 필터 로드")
        print("#---------------------------------------")
        for f_key in self.filters.keys(): #딕셔너리의 key만 모을 수 있는 함수!
            print(f"✓ {f_key:<10} 필터 로드 완료 (Cross, X)")

        valid_result = {} #성능분석시에 사용할 패턴별 연산 결과를 담아둘 딕셔너리
        print("\n#---------------------------------------")
        print("# [2] 패턴 분석(라벨 정규화 적용)")
        print("#---------------------------------------")

        total_count= 0
        pass_count =0
        fail_case = []

        
        for p_key in self.patterns.keys():
            print(f"- --{p_key} ---")
            total_count +=1

            is_size_valid, size_error_reason = self.check_filter_pattern(p_key)
            if not is_size_valid:
                print(f"판정 : ERROR | FAIL ({size_error_reason})\n")
                fail_case.append((p_key,size_error_reason))
                continue

            analyze_result = self.analyze_pattern(p_key)
            valid_result[p_key] = analyze_result

            
            print(f"Cross 점수: {analyze_result['score_cross']:.16f}")
            print(f"X점수 : {analyze_result['score_x']:.16f}")
            print(f"판정: {analyze_result['result']} | expected: {analyze_result['expected']} | {analyze_result['status']} {analyze_result['reason']} ")

            if analyze_result["status"]=="PASS":
                pass_count+=1
            else:
                fail_case.append((p_key,analyze_result["reason"]))
        print("\n#---------------------------------------")
        print("# [3] 성능 분석 (평균/10회)")
        print("#---------------------------------------")
        print(f"{'크기':<12}{'평균 시간(ms)':<16}{'연산 횟수':<12}")
        print("#---------------------------------------")



        for p_key, p_value in valid_result.items():
            n_size= self.patterns[p_key].get("n_size",0)
            #흠..평균 시간 어떻게 불러오지? mac()함수를 또 불러오는건 로직 낭비.. 이미 불러왔던것 사용 
            # 근데 analyze_pattern()에서는 mac함수를 사용!
            size=f"{n_size}x{n_size}"
            avg_time = p_value['avg_time']
            count = n_size * n_size

            print(f"{size:<12}{avg_time:<12.4f}{count:<12}")

        print("#---------------------------------------")
        print("# [4] 결과 요약") 
        print("#---------------------------------------")

        fail_count = len(fail_case)

       

        print(f"총 테스트: {total_count}개")
        print(f"통과: {pass_count}개")
        print(f"실패: {fail_count}개\n")

        if  fail_case:
            print("실패 케이스")
            for p_key, reason in fail_case:
                print(f"- {p_key}: {reason}")
        print("\n")



class Manager:
    def __init__(self):
        #__init__ 에서 인스턴스를 만들어 이전 실행결과를 기억!
        self.mode1_run = Mode_1()
        self.mode2_run = Mode_2("data.json")

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
                self.mode2_run.mode2_flow()
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