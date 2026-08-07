# MinNPU
외부 라이브러리 없이 MiniNPU 시뮬레이터 개발

#  트러블슈팅

## self.mode1_run() 에러 (type error)
이 에러는 self.mode1_run()처럼 클래스 인스턴스 뒤에 소괄호 ()를 붙여 함수처럼 호출하려고 했지만, 정작 Mode_1 클래스 안에 __call__ 메서드가 정의되어 있지 않아서 발생한 오류!

파이썬에서 객체를 함수처럼 인스턴스() 형식으로 실행하려면, 해당 클래스 내부에 반드시 def __call__(self): 메서드가 작성되거나 self.model_run.execute()와 같은 방식을 사용 가능

### 방법 1.  Mode_1 클래스의 메인 실행 함수 이름을 __call__로 변경
객체를 바로 self.mode1_run() 형태로 호출하고 싶다면, Mode_1 클래스의 메인 실행 함수 이름을 __call__로 변경

### 방법 2. 일반 메서드 이름 사용 후, 그 메서드를 호출
self.mode1_run.mode1_flow()



## 1. `Matrix` 클래스 인스턴스 생성 시 `TypeError` 발생 문제

###  문제 상황 (Issue)
모드 1(사용자 입력 모드)과 모드 2(자동 분석 모드) 실행 중 `Matrix` 객체를 생성하는 방식의 차이로 인해 `TypeError`가 발생함.

* **사례 1:** `Matrix`가 데이터(`data`)만 받도록 작성된 상태에서 크기(`size`)와 데이터를 함께 넘길 때 발생
이미지: selftypeerror1

```text
  TypeError: Matrix.__init__() takes 2 positional arguments but 3 were given
```

* **사례 2**: Matrix가 크기(size)와 데이터(data)를 모두 필수 인자로 요구하는 상태에서 크기만 넘길 때 발생
이미지 : selftypeerror2

```text
TypeError: Matrix.__init__() missing 1 required positional argument: 'data'
```

**원인 분석 (Root Cause)**
파이썬 클래스의 __init__ 메서드는 첫 번째 인자로 인스턴스 자신(self)을 자동으로 전달받음.

* 모드 1에서는 행렬 크기(size)만 지정하여 빈 행렬을 생성하는 방식(Matrix(n_size))을 사용함.

* 모드 2에서는 크기와 기존 데이터(data)를 동시에 전달하는 방식(Matrix(n_size, data))을 사용함.

**모드에 따라 넘겨주는 인자 개수**가 달랐으나, Matrix.__init__의 매개변수가 이를 유연하게 처리하지 못해 충돌이 발생함.

### 해결 방법 
Matrix 클래스의 __init__ 메서드 매개변수에 **기본값(data: list = None)을 적용**하여, **1개의 인자(크기만 전달)와 2개의 인자(크기+데이터 전달)를 모두 수용**할 수 있도록 수정함.


```python
class Matrix:
    def __init__(self, size: int, data: list = None):
        self.size = size
```