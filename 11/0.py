class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"<이름:{self.name}, 나이:{self.age}>"
    
def keyAge(person):
    return person.age

people = [Person("홍길동",20), Person("김철수", 35),Person("최자영",38)]
print(sorted(people, key = keyAge))
