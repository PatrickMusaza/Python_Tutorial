dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
print(merged)
