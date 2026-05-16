def calculate_w_recursive(n):
    if n == 1:
        return 0.3
    elif n == 2:
        return -1.5
    else:
        w_prev_1 = calculate_w_recursive(n - 1)
        w_prev_2 = calculate_w_recursive(n - 2)
        numerator = (n - 1) ** 2
        denominator = (n + 1) ** 3
        return w_prev_1 * w_prev_2 * numerator / denominator
if __name__ == "__main__":
    print("Результаты вычислений (рекурсивная версия):")
    for n in range(1, 6):  # Вычисляем w1-w5
        result = calculate_w_recursive(n)
        print(f"w_{n} = {result:.8f}")  # :.8f - вывод с 8 знаками после запятой
    try:
        user_n = int(input("\nВведите номер элемента (n) для вычисления w_n: "))
        if user_n >= 1:
            user_result = calculate_w_recursive(user_n)
            print(f"w_{user_n} = {user_result:.10f}")
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Ошибка: нужно ввести целое число!")
    
    input("\nНажмите Enter для выхода")  # Чтобы окно не закрылось сразу