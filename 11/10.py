class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def __add__(self, other):
        # + 연산자 오버로딩: 두 원의 반지름을 더한 새로운 원 반환
        return Circle(self.__radius + other.__radius)
    
    def __gt__(self, other):
        # > 연산자 오버로딩: 반지름 비교
        return self.__radius > other.__radius
    
    def __lt__(self, other):
        # < 연산자 오버로딩: 반지름 비교
        return self.__radius < other.__radius
