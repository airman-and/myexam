orders = [ ["1", "재킷", 5, 120000], 
["2", "셔츠", 6, 24000], 
["3", "바지", 3, 50000],
["4", "코트", 6, 300000] ]
result = list(map(lambda x: (x[0], x[2] * x[3]), orders))
print(result)
