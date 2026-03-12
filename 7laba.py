"""
Лабораторная работа по АСД
Тема: Динамическое программирование - Задача о максимальном подмассиве
"""


def max_subarray_sum(arr):
    """

    мы ищем самые выгодные позиции подмассива для суммы 6

    Находит максимальную сумму непрерывного подмассива.

    Суть алгоритма:
    Проходим по массиву и на каждом шаге решаем:
    - взять текущий элемент и добавить к предыдущей сумме
    - или начать новый подмассив с текущего элемента

    Пример:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    Шаг 1: берем -2
    Шаг 2: 1 лучше, чем -2+1 = -1 → берем 1
    Шаг 3: -3 лучше, чем 1-3 = -2 → берем -2
    Шаг 4: 4 лучше, чем -2+4 = 2 → берем 4
    и так далее...
    """
    if not arr:
        return 0

    # Текущая сумма (заканчивается на текущем элементе)
    current_sum = arr[0]
    # Максимальная сумма за все время
    max_sum = arr[0]

    for i in range(1, len(arr)):
        # Что выгоднее: начать новый подмассив или продолжить старый?
        current_sum = max(arr[i], current_sum + arr[i])
        # Обновляем максимум!
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_elements(arr):
    """
    Возвращает не только сумму, но и сам подмассив.
    """
    if not arr:
        return 0, []

    current_sum = arr[0]
    max_sum = arr[0]

    # Индексы начала и конца текущего подмассива
    start = 0
    end = 0
    # Временное начало для нового подмассива
    temp_start = 0

    for i in range(1, len(arr)):
        # Если начать новый подмассив выгоднее
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum = current_sum + arr[i]

        # Если нашли новую максимальную сумму
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start : end + 1]


if __name__ == '__main__':
    # Пример 1: смешанные числа
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f'Массив: {arr1}')
    sum1, sub1 = max_subarray_with_elements(arr1)
    print(f'Максимальная сумма: {sum1}')
    print(f'Подмассив: {sub1}')
    print()
