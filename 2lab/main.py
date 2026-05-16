# 1 задание
import itertools

def count_codes():
    letters = ['А', 'Н', 'Д', 'Р', 'Е', 'Й']
    count = 0
    
    for code in itertools.product(letters, repeat=6):
        if code[0] == 'Й' or code[-1] == 'Й':
            continue
        if code.count('Й') > 1:
            continue
        has_invalid_ye = False
        for i in range(len(code) - 1):
            if (code[i] == 'Й' and code[i+1] == 'Е') or (code[i] == 'Е' and code[i+1] == 'Й'):
                has_invalid_ye = True
                break
        if has_invalid_ye:
            continue
        count += 1
    
    return count

print(f'1 задание: {count_codes()}')


# 2 задание
n = 8**2020 + 4**2017 + 25
print(f'2 задание: {bin(n).count("1")}')


# 3 задание
print('3 задание:')
count = 1
for num in range(245690, 245757):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(count, num)
            count += 1