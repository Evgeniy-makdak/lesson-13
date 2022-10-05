# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:

    def get_name(self):
        return Room().get_name()


class City:
    def __init__(self):
        self.street = Street()

    def population(self):
        return 100500

    def get_name(self):
        return self.street.get_name()


class Country:
    def __init__(self):
        self.city = City()

    def get_name(self):
        return self.city.get_name()

    def get_population(self):
        return self.city.population()


class Planet:
    def __init__(self):
        self.Country = Country()

    def get_name(self):
        return self.Country.get_name()

    def get_population(self):
        return self.Country.get_population()


class Person:
    def __init__(self):
        self.planet = Planet()

    def get_person_room(self):
        # return self.planet.get_contry().get_city().get_street().get_room().get_name()
        return self.planet.get_name()

    def get_city_population(self):
        # return self.planet.get_contry().get_city().population()
        return self.planet.get_population()


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person()
s1 = person.get_person_room()
s2 = person.get_city_population()
print(s1)
print(s2)
