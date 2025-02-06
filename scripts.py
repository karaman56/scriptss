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

    last_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title
    ).order_by('-date').first()

    if not last_lesson:
        print(f"У ученика '{schoolkid.full_name}' нет уроков по предмету '{subject_title}'.")
        return

    Commendation.objects.create(
        text="Молодец! Отлично справился с заданием.",
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )
    print(f"Похвала для ученика '{schoolkid.full_name}' успешно создана.")


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




