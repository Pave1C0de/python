"""
3. Реализовать базовый класс Worker (работник).

    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
    например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
    и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position,
    передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
class Worker:
    def __init__(self, name, surname, position, income = {"wage": 0, "bonus": 0}):
        try:
            if type(income) == dict and type(name) == str and type(surname) == str and type(position) == str:
                self._income = income
                self.name = name
                self.surname = surname
                self.position = position
        except: TypeError('bad type Worker class init')


class Position(Worker):
    def get_full_name(self):
        return self.name + " " +self.surname

    def get_total_income(self):
        try:
            return self._income["wage"] + self._income["bonus"]
        except:
            return -1


seller_1 = Position("Jon", "Doe", "main seller", {"wage": 100, "bonus": 200})
print(seller_1.position)
print(f"full name: {seller_1.get_full_name()}")
print(f"total imcome: {seller_1.get_total_income()}")
print()
seller_2 = Position("Борис", "Бритва", "best seller", {"wage": 100, "bonus": 150})
print(seller_2.position)
print(f"full name: {seller_2.get_full_name()}")
print(f"total imcome: {seller_2.get_total_income()}")