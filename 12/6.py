class Point:
    def __init__(self, x, y):
        # 2D 좌표를 멤버 변수에 저장
        self.x = x
        self.y = y

    def __str__(self):
        # "(x, y)" 형태의 문자열 반환
        return f"({self.x}, {self.y})"


class Point3D(Point):
    def __init__(self, x, y, z):
        # 부모(Point) 초기화
        super().__init__(x, y)
        # 3D 좌표 z 추가
        self.z = z

    def __str__(self):
        # "(x, y, z)" 형태의 문자열 반환
        return f"({self.x}, {self.y}, {self.z})"


# 사용 예
if __name__ == "__main__":
    p2 = Point(3, 4)
    p3 = Point3D(1, 2, 5)
    print(p2)  # 출력: (3, 4)
    print(p3)  # 출력: (1, 2, 5)
