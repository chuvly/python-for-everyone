 ## P4.1 루프를 이용하여 다음을 계산하는 프로그램을 작성하라.

# a. 2와 100 사이 (경계 포함)에 있는 모든 짝수들의 합

a = 0
for value in range(2, 101, 2) :
    a += value

print("연습문제 P4.1 a :", a)


# b. 1과 100 사이 (경계 포함)에 있는 모든 제곱수의 합

b = 0
for value in range(1, 100) :
    num = value ** value
    b += num

print("연습문제 P4.1 b :", b)


# c. 2^0 부터 2^20까지 모든 2의 거듭제곱 수

print("연습문제 P4.1 c")
for num in range(21) :
    c = 2 ** num
    print("2의", num,"제곱 =", c) 


# d. a와 b 사이(경계 포함)의 모든 홀수의 합 a,b는 입력으로 받는다.

d = 0
a = int(input("a ="))
b = int(input("b ="))
for value in range(a,b + 1) :
    if value % 2 != 0 :
        d += value

print("연습문제 P4.1 d :", d)


# e. 입력받은 수에서 홀수 숫자의 합 (ex. input = 32677 sum = 3 + 7 + 7 = 17)

e = 0
num = input("num =")
for value in num :          # 각 자릿수를 분리하여 정수 시퀀스로 만듬
    number = int(value)     # 분리한 자릿수를 정수형으로 초기화
    if number % 2 != 0 :
        e += number

print("연습문제 P4.1 e :", e)
