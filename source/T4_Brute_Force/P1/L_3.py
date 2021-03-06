"""
Перестановки.
За заданим натуральним числом n вивести усі перестановки з цілих чисел від 1 до n.
"""

def sequences(lst : list, k, n):
    """
    :param lst: підсписок перестановок
    :param k:   елемент для вставки
    :param n:   найбільший елемент послідовності
    :return:    None
    """
    if k > n:  # Якщо всі елементи вже вичерпано
        print(*lst)
        return

    # Вставляємо елемент k у всі можливі позиції списку
    # отриманого на попередніх ітераціях
    for pos in range(k):
        lst_next = lst[:]              # Копіюємо список
        lst_next.insert(pos, k)        # вставляємо елемент
        sequences(lst_next, k + 1, n)  # Запускаємо рекурсивно додавання наступного члена послідовності.

# Головна програма
if __name__ == "__main__":
    n = int(input())
    lst = []
    sequences(lst, 1, n)

