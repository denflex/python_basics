"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""

class Worker:
    name = "Роман"
    surname = "Петров"
    position = "Сантехник"
    wage = 100000
    bonus = 50000
    _income = {"Оклад": wage, "Премия": bonus}
    profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_total_income(self):
        self.profit = self.wage + self.bonus
        return "Оклад плюс премия: {}".format(self.profit)


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.wage)

p = Position()
print(str(p.get_total_income()) + " " + str(w._income))
