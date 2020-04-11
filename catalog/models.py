from django.db import models

TRANSMISSION_CHOICE = [
    (1, "механика"),
    (2, "автомат"),
    (3, "робот"),
]

class Producer(models.Model):
    name = models.CharField('Производитель', max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 

class Color(models.Model):
    name = models.CharField('Производитель', max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 

class Car(models.Model):
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True)
    model_of_car = models.CharField('Модель', max_length=150, null=True)
    year = models.IntegerField('Год выпуска', null=True)
    transmission = models.SmallIntegerField('Коробка передач', choices=TRANSMISSION_CHOICE, null=True)
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['producer']

    def __str__(self):
        return self.producer.name + ' ' + self.model_of_car + ' ' + self.color.name + ' ('+str(self.year)+')'

    @classmethod
    def transmission_choice(cls, transmission_str):
        return {b: a for a, b in cls._meta.get_field('transmission').choices}.get(
            transmission_str, 'NULL')