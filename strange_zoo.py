
meerkat = []
for _ in range(3):
    data = input()
    meerkat.append(data)
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)