

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

    if last_lesson is None:
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



