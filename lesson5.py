# LESSON #5. Списки (list). Функции и их методы

# list

nums = [True, 'Numbers', []]

nums[-1].append(10)
nums[-1].append(20.0)
nums[-1].extend([3, 4.0])
nums[-1].extend([0, 100.0, 200])
nums[-1].extend([0, 1000.0, 2000, 3000.0, 4000])
nums[-1].insert(0, 0)

if nums[0]:
    print(f"\n{nums[1]}[{len(nums[-1])}]: {nums[-1]}")

    nums[-1].reverse()
    print(f"\nreverse(): {nums[-1]}")

    nums[-1].sort()
    print(f"\nsort(): {nums[-1]}")

    nums[-1].pop()
    print(f"\npop(): {nums[-1]}")

    nums[-1].pop(-2)
    print(f"\npop(-2): {nums[-1]}")

    nums[-1].remove(0)
    print(f"\nremove(0): {nums[-1]}")

    print(f"\nCountable elements (with for):")
    for el in range(len(nums[-1])):
        print(f"{el}) {nums[-1][el]}")

    value = input("\nВведіть значення для підрахунку кількості збігів: ")

    count = 0
    count += nums[-1].count(float(value))
    count += nums[-1].count(str(value))
    count += nums[-1].count(bool(value))

    print(f"Знайдено збігів: {count}")

nums[-1].clear()
print(f"\nclear(): {nums[1]}[{len(nums[-1])}]: {nums[-1]}")
