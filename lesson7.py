# LESSON #7. Кортежи (tuple)

data = (True, tuple("Tuple"), tuple([0, 2, 4.0, 6, 8.0, 10, 0]))

if data[0]:
    print(f"\n{data[1]}[{len(data[-1])}]: {data[-1]}")

    print(f"\ndata[-1].count(0): {data[-1].count(0)}")
