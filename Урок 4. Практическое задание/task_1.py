"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv
script_name, workday, perhour, bonus = argv
def sal(argv):
    sal1 = int(workday) * int(perhour) + int(bonus)
    return sal1
print("Имя скрипта: ", script_name)
print("Ваша зарплата: ", sal(argv))

