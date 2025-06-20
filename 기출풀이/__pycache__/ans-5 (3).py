# 학번: 2024315312   이름: 조현영

print("--- 1 ----")
# 음이 아닌 정수를 리스트로 나타낸다. 예: 1234는  [4, 3, 2, 1], 0은 [0]
# 이런 리스트 형태의 수로 변환하여 반환하는 함수 f를 
# 결과가 모두 True가 나오도록 '''''' 위치에 완성하시오.

def f(n):
    '''''' 
    nist =list(map(int, list(str(n))))
    nist.reverse()
    return nist

print(f(0) == [0])
print(f(45) == [5, 4])
print(f(12345) == [5, 4, 3, 2, 1])
print(f(123) == [3, 2, 1])



print("--- 2 ----")
# m부터 n까지의 덧셈식과 합을 문자열로 반환하는 함수 sum(m, n)을
# 결과가 모두 True로  나오도록 '''''' 위치에 작성하시오.
# 항의 수가 5 이상이면 중간에 ... 을 넣는다
# 예: 2+3+4+5=14,     2+3+...+7=27

def Sum(m, n):
    ''''''
    hap = 0
    List = list(range(m,n+1))
    hap = sum(List)
    List = list(map(str,List))
  

     
    if len(List) >= 5:
        return f'{List[0]}+{List[1]}+...+{List[-1]}={hap}'
    if len(List) < 5:
        result = "+".join(List)
        return f'{result}={hap}'


print(Sum(2,5) == "2+3+4+5=14")
print(Sum(2,7) == "2+3+...+7=27")
print(Sum(5,100) == "5+6+...+100=5040")          


print("--- 3 ----")
# 함수 change(m, n500, n100)는 거스름 돈을 동전으로 지불한다.
# 동전으로는 500원, 100원이 있고 n500, n100은 각 동전이 있는 갯수이다.
# 500원 동전이 부족하면 100원 동전으로 지불해야 하고,
# 100원 동전이 있으면 최소한 하나는 지불해야 한다.
# 지불할 수 없으면 함수는 "NG"를 반환한다.
# 결과가 모두 True로  나오도록 '''''' 위치에 함수를 작성하시오.

def change(m, n500, n100):
    ''''''
    # 500원으로 뺸다. 이후 500원보다 작아지거나 500원의 개수가 0보다 작아지면, 
    # 100원으로 뺀다. 이후 0원이되면 사용 개수와 함께 출력, 
    # 100원보다 작은 수가 되거나, 100원을 다 사용해버리면 NG 출력
    List = [0,0]
    if m >= 100 and n100 > 0:
        m -= 100
        n100 -= 1
        List[1] += 1

    while m >= 500 and n500 > 0:
        m -= 500
        n500 -= 1
        List[0] += 1
    while m >= 100 and n100 > 0:
        m -= 100
        n100 -= 1
        List[1] += 1
    if m == 0:
        return (List[0],List[1])
    else:
        return 'NG'


    

print(change(500, 0, 10) == (0, 5))
print(change(500, 2, 10) == (0, 5))
print(change(500, 2, 0) == (1, 0))
print(change(1000, 2, 10) == (1, 5))
print(change(90, 1, 10) == "NG")
print(change(1000, 2, 4) == "NG")


print("--- 4 ----")
# 함수 exp(s)은 실수 형태인 문자열 "0.xxxx"을
# 매개변수 s로 받아 정수부분이 한자리인 지수 형태인 문자열로 반환한다.
# 결과가 모두 True 가 나오도록 '''''' 위치에 함수를 작성하시오..
# 참고로 문자열을 실수로 변환한 처리하면, 소숫점 이하가 일치하지 않을 수 있다.
# 따라서 처음부터 끝까지 문자열로 처리해야 한다.
# 힌트: 문자열에서 0이 아닌 숫자의 위치를 파악하여 지수를 결정해야한다.
#         "0.00123."은 소숫점을 3자리 옮겨야 되기때문에 지수가 -3이된다.

def exp(s):
    if float(s) == 0:
        return s + 'e0'
    if s[0] != '0':
        return f'bad: {s}'
    else:
        S = list(s)
        S.remove('.')
        i = 0
        while S[i] == '0':
            i += 1
        news = S[i:]
        news.insert(1,'.')
        return "".join(news) + f'e-{i}'

print(exp("0.001230") == "1.230e-3")
print(exp("0.10000") == "1.0000e-1")
print(exp("0.000") == "0.000e0")
print(exp("1234.") == "bad: 1234.")






