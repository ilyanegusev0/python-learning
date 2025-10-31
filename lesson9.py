# LESSON #9. Множества (set и frozenset)

# set

set_data = {True, 'python', 1, 1.0, 2, 2.5, 3, 3.0, 4, 4.05, 5, 5.0}

print(f"\nset_data: {set_data}")

set_data.add(6)
print(f"\nset_data.add(6): {set_data}")

set_data.update([True, False, 'python', 'c#', 7, 7.0, 8, 8.5])
print(f"\nset_data.update([True, False, 'python' , 'c#', 7, 7.0, 8, 8.5]): {set_data}")

set_data.remove('c#')
print(f"\nset_data.remove('c#'): {set_data}")

set_data.clear()
print(f"\nset_data.clear(): {set_data.clear()}")

nums = [0, 10, 10.0, 20, 20.5, 30, 40, 50, 0]
print(f"\nnums: {nums}")

nums = set(nums)
print(f"\nnums = set(nums): {nums}")

# frozenset
print("\n" + '-' * 50)

fset_data = frozenset([True, 'python', 1, 1.0, 2, 2.5, 3, 3.0, 4, 4.05, 5, 5.0])
print(f"\nfset_data: {fset_data}")
