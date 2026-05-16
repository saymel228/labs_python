def unpack(iterable):
    result = []
    stack = [iter(iterable)]
    
    while stack:
        current = stack[-1]
        try:
            item = next(current)
            if isinstance(item, (list, tuple, set)):
                stack.append(iter(item))
            elif isinstance(item, dict):
                stack.append(iter(item.items()))
            else:
                result.append(item)
        except StopIteration:
            stack.pop()
    
    return result
if __name__ == "__main__":
    test_data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
    print("Итеративная распаковка:")
    print("Оригинальные данные:")
    print(test_data)
    
    print("\nРезультат распаковки:")
    unpacked = unpack(test_data)
    print(unpacked)