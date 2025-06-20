class Function:
    def value(self, x):
        """Return f(x). 서브클래스에서 반드시 오버라이딩해야 함."""
        raise NotImplementedError("Subclass must implement value()")


class Quadratic(Function):
    def __init__(self, a, b, c):
        # 2차 방정식의 계수 저장
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        # f(x) = a·x² + b·x + c
        return self.a * x**2 + self.b * x + self.c

    def get_roots(self):
        """
        방정식 a·x² + b·x + c = 0 의 두 근을 반환.
        판별식(discriminant) D = b² - 4ac
        D ≥ 0 이면 실수 근, D < 0 이면 복소수 근.
        """
        disc = self.b**2 - 4 * self.a * self.c

        # 실수/복소수 구분하여 제곱근 계산
        if disc >= 0:
            from math import sqrt
            sqrt_disc = sqrt(disc)
        else:
            from cmath import sqrt
            sqrt_disc = sqrt(disc)

        root1 = (-self.b + sqrt_disc) / (2 * self.a)
        root2 = (-self.b - sqrt_disc) / (2 * self.a)
        return root1, root2


# 사용 예
if __name__ == "__main__":
    q = Quadratic(1, -3, 2)
    print("f(5) =", q.value(5))           # f(5) = 1·25 -3·5 +2 = 12
    roots = q.get_roots()                 
    print("roots =", roots)               # roots = (2.0, 1.0)
