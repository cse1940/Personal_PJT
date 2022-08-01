## CHAPTER 1. ★

## 1-1. 파이썬과 Visual Studio Code 설치하기

- 파이썬 설치 완료했습니다.

![Visual Studio Code 설치 화면](README.assets/image-20220801005203631.png)



```python
 우리가 파이썬을 왜 배워야 하는지에 대해, 파이썬은 왜 파이썬인지 간략하게 정리한 후에 Python을 설치해보았습니다.
설치부터 어려워 못하면 어떡하지 우려함과는 달리 Visual Studio Code라는 코드 에디터가 있어 손쉽게 할 수 있었습니다.
Python을 설치 후, 책에 있는 예제 문장을 실행해보며 맛을 보았습니다.
앞으로 어떤 것을 배울지 걱정 반, 기대 반 입니다.
```

### 1-2. 출력 프로그램 만들기

```python
print("2022", "07", "31", sep="-") # 2022-07-31
print("PM 23", "58", sep=":") # PM 23:58
print("------------") # ------------
print("내 이름은 최승은이고,", end=" ") # 내 이름은 최승은이고, 24살이다.
print("24살이다.")
print("MBTI는", "ISTP이다.") # MBTI는 ISTP이다.
```

### 1-3. 자료형 마스터!

```python
name = "최승은"
age = 24
MBTI = "ISTP"
height = 159.9
have_boyfriend = True
print(type(name)) # <class "str">
print(type(age)) # <class "int">
print(type(MBTI)) # <class "str">
print(height) # <class "float">
print(have_boyfriend) # <class "bool">
```

### 1-4. 어떻게 돈을 내야 할까?

```python
price = 5670
thousand = 5
hundred = 6
ten = 7
print(f"""{price}원을 계산하려면 # 5670원을 계산하려면
1000원 지폐 {thousand}장 # 1000원 지폐 5장
100원 동전 {hundred}개 # 100원 동전 6개
10원 동전 {ten}개가 필요합니다.""") # 10원 동전 7개가 필요합니다.
```

### 1-5. 생년원일로 연도, 월, 일 출력하기

```python
birth = int(input("생년월일을 입력해 주세요. : ")) # 19991006
year = birth // 10000
month = (birth % 10000) // 100
day = (birth % 10000) % 100
print(f"{year}년 {month}월 {day}일 생이네요!") # 1999년 10월 6일 생이네요!
```

