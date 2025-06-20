f = lambda x:x**3
snl = [1, 2, 3, 4, 5, 6, 7]
print(f'원래 리스트:\n{snl}')
nd = list(map(f,snl))
print(f'세제곱된 값:\n{nd}')