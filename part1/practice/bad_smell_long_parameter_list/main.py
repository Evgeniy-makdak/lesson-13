# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __int__(self):
        pass

    def get_speed(self):
        if self.state == "fly":
            return self.speed * 1.2
        elif self.state == "crawl":
            return self.speed * 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    def set_unit(self, ):
        pass

    def move(self, direction):

        speed = self.get_speed()
        if direction == 'UP':
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)

#     ...
