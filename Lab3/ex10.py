def loop(mapping):
    current_key = 'start'
    visited = set()
    result = []
    while current_key not in visited and current_key in mapping:
        result.append(mapping[current_key])
        visited.add(current_key)
        current_key = mapping[current_key]

    return result


map = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(map))
