class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = (self.index, self.data[self.index])
        self.index += 1
        return result

# 테스트
data = ['a', 'b', 'c']
for index, value in MyEnumerate(data):
    print(f"{index} : {value}")
