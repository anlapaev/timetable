import datetime

from django.db import models

# Группы
class Group(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Название группы')
    Letter_Class = (
        ('1 Курс', '1 Курс'), ('2 Курс', '2 Курс'), ('3 Курс', '3 Курс'), ('4 Курс', '4 Курс'), ('5 Курс', '5 Курс'),
        ('6 Курс', '6 Курс')
    )
    letter = models.CharField(max_length=40, choices=Letter_Class, default="", verbose_name='Курс')
    count = models.CharField(max_length=10, null=True, verbose_name='Кол-во студентов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

# Дисциплина
class Discipline(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


# Преподаватели
class Teacher(models.Model):
    name = models.CharField(max_length=150, null=True, verbose_name='ФИО преподавателя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

# Аудитория
class Audience(models.Model):
    name = models.CharField(max_length=150, null=True, verbose_name='Аудитория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


# Пара
class Lesson(models.Model):
    date = models.DateField(verbose_name='Дата проведения пары', null=True)
    Letter_Class = (
        ('Лекция', 'Лекция'), ('Семинар', 'Семинар'), ('Экзамен', 'Экзамен')
    )
    Date_Para = (
        ('8:00-9:30', '8:00-9:30'), ('9:40-11:10', '9:40-11:10'), ('11:20-12:50', '11:20-12:50'),
        ('13:00-14:30', '13:00-14:30'),
        ('14:40-16:10', '14:40-16:10'), ('16:20-17:50', '16:20-17:50'),
    )
    letter = models.CharField(max_length=40, choices=Letter_Class, default="", verbose_name='Вид пары')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа', null=True)
    category = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплина', null=True,)
    name = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='ФИО преподавателя', null=True)
    para = models.CharField(max_length=50, choices=Date_Para, default="А", verbose_name='Время')
    office = models.ForeignKey(Audience, on_delete=models.CASCADE, verbose_name='Аудитория', null=True, )

    def __str__(self):
        return self.para

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'
