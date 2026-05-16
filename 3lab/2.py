def calculate_w(n):
    if n == 1:
        return 0.3
    elif n == 2:
        return -1.5
    
    w_prev_prev = 0.3  # w1
    w_prev = -1.5       # w2
    
    for i in range(3, n + 1):
        numerator = (i - 1) ** 2
        denominator = (i + 1) ** 3
        w_current = w_prev * w_prev_prev * numerator / denominator
        w_prev_prev, w_prev = w_prev, w_current
    
    return w_prev
if __name__ == "__main__":
    print("Результаты вычислений:")
    for n in range(1, 6):  # Вычисляем w1-w5
        result = calculate_w(n)
        print(f"w_{n} = {result:.8f}")  # :.8f - вывод с 8 знаками после запятой
    try:
        user_n = int(input("\nВведите номер элемента (n) для вычисления w_n: "))
        if user_n >= 1:
            user_result = calculate_w(user_n)
            print(f"w_{user_n} = {user_result:.10f}")
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Ошибка: нужно ввести целое число!")
    
    input("\nНажмите Enter для выхода")  # Чтобы окно не закрылось сразу