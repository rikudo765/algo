#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних двбічнооднозв'язний список з поточним елементом.
"""

def init():
    """ Викликається один раз на початку виконання програми. """
    pass


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return True


def set_first():
    """ Зробити поточний елемент першим.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    pass


def set_last():
    """ Зробити поточними останній елемент списку

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    pass


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    pass


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    pass


def current():
    """ Повертає навантаження поточного елементу.

    :return: Навантаження поточного елементу
    """
    return None


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    pass


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    pass


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    """
    pass


def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return []


def len():
    """ Повертає кількість елементів у списку

    :return: кількість елементів у списку
    """
    return 0


def swap_prev():
    """ Міняє місцями поточний елемент списку з попереднім
    Гарантується, що виклик функції здійснюється лише, якщо поточний елемент не перший у списку
    Поточний елемент лишається не змінним
    """
    pass


def swap_next():
    """ Міняє місцями поточний елемент списку з наступним
    Гарантується, що виклик функції здійснюється лише, якщо поточний елемент не останній у списку
    Поточний елемент лишається не змінним
    """
    pass
