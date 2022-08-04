## CHAPTER 1. ★

### 1-1. 파이썬과 Visual Studio Code 설치하기

- 파이썬과 Visual Studio Code를 설치하고 실행한 과정을 나만의 글로 기록하기

![Visual Studio Code 설치 화면](README.assets/image-20220801005203631.png)



```python
 우리가 파이썬을 왜 배워야 하는지에 대해, 파이썬은 왜 파이썬인지 간략하게 정리한 후에 Python을 설치해보았습니다.
설치부터 어려워 못하면 어떡하지 우려함과는 달리 Visual Studio Code라는 코드 에디터가 있어 손쉽게 할 수 있었습니다.
Python을 설치 후, 책에 있는 예제 문장을 실행해보며 맛을 보았습니다.
앞으로 어떤 것을 배울지 걱정 반, 기대 반 입니다.
```

### 1-2. 출력 프로그램 만들기

- 양식은 자유, 배운 내용을 최대한 활용하여 나를 소개하기

```python
print("2022", "07", "31", sep="-") # 2022-07-31
print("PM 23", "58", sep=":") # PM 23:58
print("------------") # ------------
print("내 이름은 최승은이고,", end=" ") # 내 이름은 최승은이고, 24살이다.
print("24살이다.")
print("MBTI는", "ISTP이다.") # MBTI는 ISTP이다.
```

### 1-3. 자료형 마스터!

- 문자열, 정수, 실수, 불 자료형 변수를 하나씩 만들고 type() 함수를 이용해 자료형으로 출력해 보기

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

- 언제나 딱 알맞은 금액으로 물건금액을 내고 싶은 승은이를 위해 1,000원 지폐, 100원 동전, 10원 동전이 최소한 몇 개씩 필요한지 계산하는 

  프로그램 만들어 보기

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

- 생년월일은 YYYYMMDD 형식의 숫자로 입력받은 뒤 연도, 월, 일을 계산해서 출력하는 프로그램 만들어 보기

```python
birth = int(input("생년월일을 입력해 주세요. : ")) # 19991006
year = birth // 10000
month = (birth % 10000) // 100
day = (birth % 10000) % 100

print(f"{year}년 {month}월 {day}일 생이네요!") # 1999년 10월 6일 생이네요!
```

### 1-6. 합격과 불합격 통보하기

- 사용자로부터 세 과목의 점수를 입력받아 평균 점수가 50점 이상이면 '합격', 50점 미만이면 '불합격'을 출력하는 프로그램 만들어 보기

```PYTHON
score1 = int(input("국어 점수를 입력하세요. : ")) # 80
score2 = int(input("수학 점수를 입력하세요. : ")) # 70
score3 = int(input("영어 점수를 입력하세요. : ")) # 60
score4 = (score1 + score2 + score3) / 3

if score4 >= 50:
    print(f"평균 점수는 {score4}점으로 합격입니다.") # 평균 점수는 70점으로 합격입니다.
else:
    print(f"평균 점수는 {score4}점으로 불합격입니다.")
```

### 1-7. BMI 결과보기

- BMI = 몸무게(kg) / (키(m) * 키(m))

- 사용자로부터 키와 몸무게를 입력받아 BMI 지수가 25 이상일 경우 '비만', 23 이상 25 미만일 경우 '과체중', 18.5 이상 23 미만일 경우 '정상 체중',

  18.5 미만일 경우에는 '저체중'이라는 메세지를 BMI 지수와 함께 출력하는 프로그램 만들어 보기

```PYTHON
height = int(input("키를 입력하세요. : ")) # 160
weight = int(input("몸무게를 입력하세요. : ")) # 60
bmi = weight / (height * 0.01 * height * 0.01)

if bmi >= 25:
    print(f"BMI 지수가 {bmi}이므로 비만입니다.")
elif bmi >= 23:
    print(f"BMI 지수가 {bmi}이므로 과체중입니다.") # BMI 지수가 23.4375이므로 과체중입니다.
elif bmi >= 18.5:
    print(f"BMI 지수가 {bmi}이므로 정상 체중입니다.")
else:
    print(f"BMI 지수가 {bmi}이므로 저체중입니다.")
```

### 1-8. 짝수이면서 7의 배수는 아닌 수 찾기

- 1 ~ 100 짝수들 중 7의 배수가 아닌 수가 몇 개인지 출력하는 프로그램 만들어 보기

```python
count = 0

for i in range(2, 101, 2):
    if i % 7 != 0:
        count += 1
print(f"짝수이면서 7의 배수가 아닌 수의 갯수는 {count}") # 43
```

### 1-9.  정수 n까지의 합을 구하는 함수 만들기

- 사용자로부터 정수를 하나 입력받아 0부터 정수 n까지의 합계를 구하는 프로그램 만들어 보기

```python
number = int(input("정수를 입력하세요. : ")) # 11

def getSum(num):
    count = 0
    for i in range(num + 1):
        count += i
    return count
sum = getSum(number)
print(f"0부터 {number}까지의 합계는 {sum}입니다.") # 60
```

### 1-10. 이름 출력하기

- "제 이름은 000입니다."라는 문자열 변수를 만들고 문자열 슬라이싱으로 000만 출력해 보기

```python
name = "제 이름은 최승은입니다."
print(name[6:9]) # 최승은
print(name[-7:-4]) # 최승은
```

### 1-11. 입력받은 수의 평균 구하기

- 숫자 7개를 입력받아 리스트에 저장하고 그 수들의 평균을 구해서 출력하는 프로그램 만들어 보기

```python
ls = []
for i in range(7):
    number = int(input("정수를 입력하세요. : ")) # 정수를 입력하세요. : 
    ls.append(number)

count = 0
for l in ls:
    count += l
print(f"평균 : {count / 7}")
```



## CHAPTER 2. ★★

### 2-1. 윤년 판단하기

- 사용자가 입력한 연도가 윤년인지 아닌지 판단하는 프로그램 만들어 보기

```PYTHON
year = int(input("연도를 입력하세요. : ")) # 1999

if year % 4 == 0 and year % 100 != 0:
    print(f"{year}은 윤년입니다.")
elif year % 400 == 0:
    print(f"{year}은 윤년입니다.")
else:
    print(f"{year}은 윤년이 아닙니다.") # 1999은 윤년이 아닙니다.
```

### 2-3. 반올림 계산기 만들기

- 반올림 계산을 하는 프로그램 만들어 보기(단, 아래 2가지 조건을 만족해야 함)
  1. 소수점 첫째 자리에서 반올림합니다.
  2. 사용자에게 실수를 입력받지만 결과는 정수를 반환해야 합니다.

```python
number = float(input("숫자를 입력해 주세요. : ")) # 10.5
number_ = int(number + 0.5)
print(f"{number}를 반올림하면 {number_}입니다.") # 10.5를 반올림하면 11입니다.
```

### 2-4. 높이가 n인 직각이등변삼각형 만들기

- 사용자에게 삼각형의 높이를 입력받아 * 문자로 직각이등변삼각형 모양을 만드는 프로그램 만들어 보기

```python
# 왼쪽으로 별 정렬
n = int(input("삼각형의 높이를 입력해 주세요. : ")) # 4
for i in range(1, n + 1):
    print("*" * i) # *
                     **
                     ***
                     ****

# 오른쪽으로 별 정렬
n = int(input("삼각형의 높이를 입력해 주세요. : ")) # 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i ) # *
                                     **
                                    ***
                                   ****
```

### 2-5. 팩토리얼 계산하기

- n!은 1부터 n까지의 모든 정수를 곱한 것
- 팩토리얼을 계산하는 코드를 만들어 보기

```python
number = int(input("숫자를 입력해 주세요. : ")) # 4
count = 1

for i in range(1, number + 1):
    count *= i
print(f"{number}!은 {count}입니다.") # 4!은 24입니다.
```

### 2-6. 퀴즈 점수 계산하기

- 퀴즈 결과에 따라 점수를 계산하는 프로그램 만들어 보기(단, 아래 조건을 만족해야 함)
  1. O는 퀴즈를 맞힌 경우입니다. O의 점수는 1점부터 시작되며, 연속해서 맞힐수록 배당된 점수가 하나씩 더 커집니다. (예: O → 1점, OOO → 1 + 2 + 3 = 6점)
  2.  X는 퀴즈를 틀린 경우입니다. X의 점수는 0점입니다.

```python
answer = input("퀴즈 결과를 입력해 주세요.(예: OOXOXXO): ").split("X") # OOOOX
score = 0

for i in answer:
    for j in range(0, len(i) + 1):
        score += j
print(score) # 10
```

### 2-7. 도형별 넓이 계산기

- 선택한 도형별로 길이를 입력받아 넓이를 출력하는 프로그램 만들어 보기
  1. 도형 목록에는 원, 삼각형, 직사각형, 정사각형이 존재합니다.
  2. 도형의 넓이 계산은 함수로 정의되어야 합니다.
  3. 도형별로 필요한 길이를 입력받아야 합니다.
     - 원 → 반지름
     - 삼각형 → 밑변, 높이
     - 직사각형 → 가로, 세로 
     - 정사각형 → 한 변의 길이

```python
def circle(x):
    return x * x * 3.14

def triangle(x, y):
    return x * y / 2

def rectangle(x, y):
    return x * y

def square(x):
    return x * x

print("""
=======도형 목록=======
1. 원
2. 삼각혐
3. 직사각형
4. 정사각형
=======================
""")

number = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해 주세요. : ")) # 4

if number == 1:
    a = int(input("원의 반지름 길이를 입력해 주세요. : "))
    print(f"반지름이 {a}인 원의 넓이는 약 {circle(a)}입니다.")
elif number == 2:
    a = int(input("삼각형의 밑변의 길이를 입력해 주세요. : "))
    b = int(input("삼각형의 높이의 길이를 입력해 주세요. : "))
    print(f"밑변이 {a}이고 높이가 {b}인 삼각형의 넓이는 {triangle(a, b)}입니다.")
elif number == 3:
    a = int(input("직사각형의 가로의 길이를 입력해 주세요. : "))
    b = int(input("직사각형의 세로의 길이를 입력해 주세요. : "))
    print(f"가로가 {a}이고 세로가 {b}인 직사각형의 넓이는 {rectangle(a,b)}입니다.")
elif number == 4:
    a = int(input("정사각형의 한 변의 길이를 입력해 주세요. : ")) # 5
    print(f"한 변이 {a}인 정사각형의 넓이는 {square(a)}입니다.") # 한 변이 5인 정사각형의 넓이는 25입니다.
else:
    print("다시 입력해 주세요.")
```

### 2-10. 숫자 n의 k번째 약수

- 숫자 n과 k를 입력받아, n의 k번째 약수를 구하는 프로그램 만들어 보기(단, 아래 조건을 만족해야 함)
  1. 숫자 k는 n이 가진 약수의 총 개수보다 작거나 같아야 합니다. 만일 k가 n이 가진 약수의 개수보다 크다면 입력한 숫자만큼의 약수가 존재하지 않는다는 메세지를 출력합니다.

```python
ls = [] 
n = int(input("숫자를 입력해 주세요. : ")) # 10
k = int(input("몇 번째 약수를 알고 싶나요? : ")) # 2

for i in range(1, n):
    if n % i == 0:
        ls.append(i)
if k > len(ls):
    print("입력한 숫자만큼의 약수가 존재하지 않습니다.")
else:
    print(f"{n}의 {k}번째 약수는 {ls[k-1]}입니다.") # 10의 2번째 약수는 2입니다.
```



### 2-11. 함수를 활용한 구구단

- 숫자를 입력받아 해당 숫자의 구구단을 출력하는 프로그램 만들어 보기(단, 아래 조건을 만족해야 함)
  1. 함수를 하나 이상 만들어 사용해야 합니다.
  2. 입력받는 숫자의 범위는 2~9이며, 범위 이외의 숫자를 입력하면 오류 메세지가 출력됩니다.
  3. 사용자가 프로그램을 종료하기 전까지 계속 반복되어야 합니다.

```python
def multiplication(x):
    for i in range(1, 10):
        print(f"{x} * {i} = {x*i}")


while True:
    number = int(input("2~9 사이의 숫자를 입력해 주세요. (1을 누르면 프로그램이 종료됩니다.) ")) # 10
    if number == 1:
        print("프로그램이 종료합니다.")
        break
    elif 2 <= number <= 9:
        multiplication(number)
    else:
        print("범위 외의 숫자입니다. 다시 시도하세요.") # 범위 외의 숫자입니다. 다시 시도하세요.
                                                  # 2~9 사이의 숫자를 입력해 주세요. (1을 누르면 프로그램이 종료됩니다.)
```

