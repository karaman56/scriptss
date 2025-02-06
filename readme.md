# Скрипт для работы с учениками

Этот проект содержит скрипты для управления данными учеников в системе. Вы можете создавать похвалы, изменять оценки и удалять плохие комментарии для учеников.

## Удаление плохих комментариев

Этот скрипт удаляет все плохие комментарии  для указанного ученика.
```
python
from datacenter.models import Schoolkid, Chastisement, Mark, Commendation, Lesson

def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'. Пожалуйста, уточните запрос.")
        return
```

# Получаем все наказания для ученика и удаляем их
```
chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
chastisements.delete()
print(f"Все наказания для ученика '{schoolkid.full_name}' были удалены.")
remove_chastisements("Голубев Феофан")


def create_commendation(schoolkid_name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'. Пожалуйста, уточните запрос.")
        return
```

# Получаем последний урок по предмету
```
last_lesson = Lesson.objects.filter(
year_of_study=schoolkid.year_of_study,
group_letter=schoolkid.group_letter,
subject__title=subject_title
).order_by('-date').first()

if not last_lesson:
    print(f"У ученика '{schoolkid.full_name}' нет уроков по предмету '{subject_title}'.")
    return
```

# Создаем похвалу
```
Commendation.objects.create(
text="Молодец! Отлично справился с заданием.",
created=last_lesson.date,
schoolkid=schoolkid,
subject=last_lesson.subject,
teacher=last_lesson.teacher
)
print(f"Похвала для ученика '{schoolkid.full_name}' успешно создана.")
create_commendation("Фролов Иван", "Музыка")
```
# Меняем оценку
```
def change_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'. Пожалуйста, уточните запрос.")
        return

    updated_count = Mark.objects.filter(schoolkid=schoolkid, value__in=[2, 3]).update(value=5)

    if updated_count:
        print(f"Оценки ученика '{schoolkid.full_name}' изменены на пятерки.")
    else:
        print(f"У ученика '{schoolkid.full_name}' нет оценок, которые можно было бы изменить.")
change_marks('Фролов Иван')
```

## Заключение

Эти скрипты позволяют управлять комментариями и похвалами для учеников в системе. Убедитесь, что вы правильно указываете имена учеников, чтобы избежать ошибок.

## Запуск скриптов

Вы можете запускать скрипты, копируя их в shell, или импортируя их из файла `scripts.py`, что является более надежным способом.

## Примечания

- Убедитесь, что вы используете актуальные имена учеников.
- Все функции написаны на Python и используют Django ORM для работы с базой данных.


