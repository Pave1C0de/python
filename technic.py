"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
import datetime

class St_a(): #Storage_area
    def __init__(self, max_place=30):
        self.equipments = []
        self.places = []
        self.max_place = max_place
        self.classes_num = []
        self.equipment_counter = {}

    def __counter(self, some, equipment, do):
        #print(equipment.__class__.__name__, do, some.__class__.__name__)
        if do == "add":
            if equipment.__class__.__name__ in self.equipment_counter.keys():
                self.equipment_counter[equipment.__class__.__name__] += 1
            else:
                self.equipment_counter.update({equipment.__class__.__name__ : 1})
        elif do == "remove":
            if (equipment.__class__.__name__ in self.equipment_counter.keys()) and self.equipment_counter[equipment.__class__.__name__] > 0:
                self.equipment_counter[equipment.__class__.__name__] -= 1
            else:
                print("No item in store area")



    def add_equipment(self, equipment, place):
        if not(equipment in self.equipments) and not(place in self.places) and (place <= self.max_place):
            self.equipments.append(equipment)
            equipment.in_time = datetime.datetime.today()
            self.places.append(place)
            self.__counter(self, equipment, "add")

    def del_equipment(self, equipment):
        if (equipment in self.equipments):
            self.places.remove(self.places[self.equipments.index(equipment)])
            self.equipments.remove(equipment)
            equipment.out_time = datetime.datetime.today()
            self.__counter(self, equipment, "remove")

    def add_places(self, add_place):
        self.max_place += add_place

    def set_place_get_eq(self, place):
        if place in self.places:
            i = self.places.index(place)
            return self.equipments[i]

    def set_eq_get_place(self, equipment):
        if equipment in self.equipments:
            i = self.equipments.index(equipment)
            return self.places[i]



class Of_eq(): #Office_equipment
    def __init__(self, brand ="Noname", sn="0000-0000-0000", dimensions=[0,0,0], in_time="00.00.0000"):
        self.brand = brand
        self.type_of_eq = self.__class__.__name__
        self.sn =sn
        self.dimensions = dimensions
        self.in_time = in_time
        self.out_time = None


    def get_info(self):
        l = 22
        print(f"Office_equipment type:{' '*(l - len('Office_equipment type'))}{self.type_of_eq}\nbrand:{' '*(l - len('brand'))}{self.brand}\nSerial number:{' '*(l - len('Serial number'))}{self.sn}\nDimensions:{' '*(l - len('Dimensions'))}{self.dimensions}\nregistration time:{' '*(l - len('registration time'))}{self.in_time}")

class printer(Of_eq):
    def __init__(self, type, brand ="Noname", sn="0000-0000-0000", dimensions=[0,0,0], in_time="00.00.0000"):
        super().__init__(brand, sn, dimensions, in_time)
        self.type = type

    def get_info(self):
        l = 22
        print(f"Office_equipment type:{' '*(l - len('Office_equipment type'))}{self.type_of_eq}\nbrand:{' '*(l - len('brand'))}{self.brand}\nSerial number:{' '*(l - len('Serial number'))}{self.sn}\nDimensions:{' '*(l - len('Dimensions'))}{self.dimensions}\nregistration time:{' '*(l - len('registration time'))}{self.in_time}\ntype:{' '*(l - len('type'))}{self.type}")

class scanner(Of_eq):
    def __init__(self, format, brand="Noname", sn="0000-0000-0000", dimensions=[0, 0, 0], in_time="00.00.0000"):
        super().__init__(brand, sn, dimensions, in_time)
        self.type = format

    def get_info(self):
        l = 22
        print(f"Office_equipment type:{' ' * (l - len('Office_equipment type'))}{self.type_of_eq}\nbrand:{' ' * (l - len('brand'))}{self.brand}\nSerial number:{' ' * (l - len('Serial number'))}{self.sn}\nDimensions:{' ' * (l - len('Dimensions'))}{self.dimensions}\nregistration time:{' ' * (l - len('registration time'))}{self.in_time}\nformat:{' ' * (l - len('format'))}{self.format}")

class xerox(Of_eq):
    def __init__(self, speed, brand="Noname", sn="0000-0000-0000", dimensions=[0, 0, 0], in_time="00.00.0000"):
        super().__init__(brand, sn, dimensions, in_time)
        self.type = speed

    def get_info(self):
        l = 22
        print(f"Office_equipment type:{' ' * (l - len('Office_equipment type'))}{self.type_of_eq}\nbrand:{' ' * (l - len('brand'))}{self.brand}\nSerial number:{' ' * (l - len('Serial number'))}{self.sn}\nDimensions:{' ' * (l - len('Dimensions'))}{self.dimensions}\nregistration time:{' ' * (l - len('registration time'))}{self.in_time}\nspeed:{' ' * (l - len('speed'))}{self.speed}")


coffee_machine2000_1 = Of_eq(brand="Bosh", sn = "2123-3333-9002", dimensions=[30, 30, 50] )
coffee_machine2000_2 = Of_eq(brand="Bosh", sn = "2123-3373-9112", dimensions=[30, 30, 50] )

work_station2307 = printer("lazer", brand="Brother", sn="353FN30002", dimensions=[40, 40, 20])
laser_jet3010 = printer("color", brand="Samsung", sn="47328164739hjd", dimensions=[30, 40, 20])

same_name_1 = scanner("A4", brand="Scan", sn="333200jkfd3999", dimensions=[35, 35, 25])
same_name_2 = scanner("A3", brand="Scan", sn="333233jkfd3933", dimensions=[35, 35, 25])

xerox_fast23 = xerox("80 p/min", brand="Xerox", sn="33323", dimensions=[50, 35, 25])
xerox_best3 = xerox("100 p/min", brand="Xerox", sn="33332f", dimensions=[45, 30, 25])




t = St_a(5)
t.add_equipment(coffee_machine2000_1, 2)
t.add_equipment(work_station2307, 1)
t.add_equipment(laser_jet3010, 3)
print(t.equipment_counter)
t.del_equipment(laser_jet3010)
print(t.equipment_counter)
t.add_equipment(coffee_machine2000_2, 4)
t.add_equipment(laser_jet3010, 5)
t.add_places(3)
t.add_equipment(same_name_1, 6)
t.add_equipment(same_name_2, 7)
t.add_equipment(xerox_fast23, 8)
print(t.equipment_counter)
print(t.set_eq_get_place(laser_jet3010))
t.set_place_get_eq(2).get_info()


#t.equipments[0].get_info()
#print(t.places)

#t.add_places(4)
#print(t.max_place)

#print(t.set_eq_get_place(d))
#t.set_place_get_eq(1).get_info()
#print("#"*10)
#t.set_place_get_eq(3).get_info()
