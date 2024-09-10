
for n in range(3,21):
    pairs = []
    for i in range(1,21):
        for j in range(1+i,21):
            if n % (i + j) == 0:
                pairs.append(f'{i}{j}')
            else:
                continue
    result = ''.join(pairs)
    print(f'{n} - {result}')