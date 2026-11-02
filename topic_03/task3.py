my_dict = {"ім'я": "Олег", "вік": 25}

print("Початковий словник:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("-" * 25)

my_dict.update({'місто': 'Київ', 'вік': 26})
print("Після update():")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("-" * 25)

print("Ключі (keys):")
for k in my_dict.keys():
    print(k)
print("-" * 25)

print("Значення (values):")
for v in my_dict.values():
    print(v)
print("-" * 25)

print("Елементи (items):")
for key, value in my_dict.items():
    print(f"Ключ: {key} | Значення: {value}")
print("-" * 25)

del my_dict["ім'я"]
print("Після видалення ключа \"ім'я\":")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("-" * 25)

my_dict.clear()
print("Після clear():")
if not my_dict:
    print("Словник порожній")