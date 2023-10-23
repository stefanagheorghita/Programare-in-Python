def compare(dict1, dict2):
    if type(dict1) != dict or type(dict2) != dict:
        return dict1 == dict2
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    for key in dict1:
        if not compare(dict1[key], dict2[key]):
            return False
    return True


dict1 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 3]}}
dict2 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 3]}}
print(compare(dict1, dict2))
dict3 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 4]}}
print(compare(dict1, dict3))
