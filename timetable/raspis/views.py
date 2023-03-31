import datetime

from django.utils import timezone
from datetime import datetime, date
from django.shortcuts import render, redirect
from django.db.models.functions import Lower

from .models import Group, Discipline, Teacher, Audience, Lesson

today = timezone.now().date()
midnight = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc)
Lesson.objects.filter(date__lt=midnight).delete() # фильтруем объекты по дате и удаляем все записи, которые меньше текущей даты

def index(request):
    field_course_name = request.GET.get("field_name")  # получаем выбранное значение поля из GET-параметра
    unic_courses = Group.objects.distinct().values_list('name', flat=True)  # уникальные курсы
    id_group_course = Group.objects.distinct().filter(name=field_course_name).values_list('id', flat=True).first()  # id групп выбранного пользователем курса
    if field_course_name in unic_courses:  # если выбранное значение есть в поле group
        group = Lesson.objects.filter(group_id=id_group_course).order_by(Lower('date').asc())  # отбираем из таблицы данные по id группы
        return render(request, "raspis/index-3.html", {"items": group})

    ######################################################
    field_teacher_name = request.GET.get("field_teach_name")  # получаем выбранное значение поля из GET-параметра
    unic_teachers = Teacher.objects.distinct().values_list('name', flat=True)  # отбираем только уникальных преподавателей
    id_teacher = Teacher.objects.filter(name=field_teacher_name).values_list('id', flat=True).first() # получаем по полю name id преподавателя

    if field_teacher_name in unic_teachers: # если выбранное значение есть в поле teacher
        teacher = Lesson.objects.filter(name_id=id_teacher).order_by(Lower('date').asc()) # отбираем из таблицы данные по id преподавателя
        return render(request, "raspis/index-3.html", {"items": teacher})

    group = Group.objects.values('name')
    discipline = Discipline.objects.filter(pk=1)
    teacher = Teacher.objects.values('name')
    auditorium = Audience.objects.all()
    lesson = Lesson.objects.all()

    context = {
        'groups': group,
        'disciplines': discipline,
        'teachers': teacher,
        'audiences': auditorium,
        'lessons': lesson,
    }

    return render(request, 'raspis/index-2.html', context=context)


def main(request):
    return render(request, 'raspis/index-1.html')