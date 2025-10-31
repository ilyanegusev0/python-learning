# LESSON #10. Функции (def, lambda)

# def

def pass_func():
    pass


get_sum = lambda x, y: x + y


def get_min(l):
    min_value = l[0]
    for el in l:
        if el < min_value:
            min_value = el

    return min_value


# --------------------------------------------------

pass_func()

print(f"\nget_sum(256, 512): {get_sum(256, 512)}")

print(f"\nget_sum(\"Hello \", \"world!\"): {get_sum("Hello ", "world!")}")

nums1 = [5, -5, 10, -10, 15, -15]
print(f"\nnums: {nums1}")
print(f"get_min(nums1): {get_min(nums1)}")
