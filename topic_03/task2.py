my_list = [5, 2, 8]

my_list.append(4)
print(f"Після append: {my_list}")

my_list.extend([1,9])
print(f"Після extend: {my_list}")

my_list.insert(2,7)
print(f"Після insert: {my_list}")

my_list.remove(8)
print(f"Після remove: {my_list}")

copied_list = my_list.copy()
print(f"Результат copy у новий список: {copied_list}")

my_list.sort()
print(f"Після sort(): {my_list}")

my_list.reverse()
print(f"Після reverse: {my_list}")

my_list.clear()
print(f"Після clear: {my_list}")
