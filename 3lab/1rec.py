def unpack_recursive(iterable):
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple, set)):
            result.extend(unpack_recursive(item))
        elif isinstance(item, dict):
            result.extend(unpack_recursive(item.items()))
        else:
            result.append(item)
    return result
if __name__ == "__main__":
    test_data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
    print("Оригинальные данные:")
    print(test_data)
    
    print("\nРезультат распаковки:")
    unpacked = unpack_recursive(test_data)
    print(unpacked)