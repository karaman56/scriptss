# Скрипт для работы с учениками

## Удаление плохих комментариев

Этот скрипт удаляет все плохие комментарии (наказания) для указанного ученика.
```
Bash
from datacenter.models import Schoolkid, Chastisement

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
Bash
chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
chastisements.delete()
print(f"Все наказания для ученика '{schoolkid.full_name}' были удалены.")
```
# Пример использования
```
Bash
remove_chastisements("Голубев Феофан")
from datacenter.models import Schoolkid, Lesson, Commendation

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
Bash
last_lesson = Lesson.objects.filter(
year_of_study=schoolkid.year_of_study,
group_letter=schoolkid.group_letter,
subject__title=subject_title
).order_by('-date').first()

if last_lesson is None:
print(f"У ученика '{schoolkid.full_name}' нет уроков по предмету '{subject_title}'.")
return
```

# Создаем похвалу
```
Bash
Commendation.objects.create(
text="Молодец! Отлично справился с заданием.",
created=last_lesson.date,
schoolkid=schoolkid,
subject=last_lesson.subject,
teacher=last_lesson.teacher
)
print(f"Похвала для ученика '{schoolkid.full_name}' успешно создана.")
```

# Пример использования 
```
create_commendation("Фролов Иван", "Музыка")
```


## Заключение

Эти скрипты позволяют управлять комментариями и похвалами для учеников в системе. Убедитесь, что вы правильно указываете имена учеников, чтобы избежать ошибок.


### Запуск скриптов

Вы можете запускать скрипты, копируя их в shell, или импортируя их из файла `scripts.py`, что является более надежным способом.

