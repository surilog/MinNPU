import json

class data_json:

    def json_load(self, file_path:str) -> Dict[str, Any] | None:
        #함수가 실행을 마치고 반환할 값 / Dict의 키는 항상 str, 값은 리스트 , 상수등 모두 올 수 있음.
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[오류] {file_path} 파일을 찾을 수 없습니다!")
        except json.JSONDecodeError:
            print(f"[오류] {file_path} 파일이 올바른 JSON형식 데이터가 아닙니다.")
            return None


    """patherns에서 key를 추출 """
    def extract_size_key(self, pattern_key : str ) -> int | None:
        # 정규표현식: "size_" 다음에 나오는 숫자를 그룹(\d+)으로 추출
        match = re.match(r"^size_(\d+)_", pattern_key)
        #(\d+) 이렇게 괄호로 감싸면 파이썬 정규표현식 엔진이 "이 부분은 나중에 따로 꺼낼 수 있게" '1번 그룹'으로 저장하여 기억!
        #re.match() : 문자열 처음부터 정규표현식과 맞는지 확인 후 반환
        if match:
            return int(match.group(1))
        #match.group(1)은 정규표현식에서 "첫 번째 괄호 ()로 묶은 부분만 쏙 빼오는 기능
        return

        # 1. 키 이름에서 크기 N 추출
        """해당 size_N 필터를 선택!"""
    

    """필터와 패턴의 크기가 일치하는지검증"""

    def schema_check(self, pattern_key: str, pattern_data: dict, fliters: dict) -> dict:
        expected = pattern_data.get("expected","UNKNOWN")

        n_size = self.extract_size_key(pattern_key)

        if n_size is None:
            return{
                "status": "FAIL",
                "reason": f"패턴 키 명명 규칙 위반 ('size_N_idx' 형식이 아닙니다: '{pattern_key}')"
            }
    
        # 2. 'size_N'필터가 filters 항목에 존재하는지 확인
        filter_key = f"size_{n_size}"
        if filter_key not in filters:
            return{
                "status": "FAIL",
                "reason": f"대응하는 필터 '{filter_key}'가 filters에 존재하지 않습니다."
            }

        filter_raw = filters[filter_key]
        input_raw = pattern_data.get("input", [])
        
    