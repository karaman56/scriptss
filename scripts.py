from datacenter.models import Schoolkid, Chastisement, Mark, Commendation, Lesson


def get_schoolkid(schoolkid_name):
    """Получает объект Schoolkid по имени ученика."""
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'. Пожалуйста, уточните запрос.")
        return


def create_commendation(schoolkid_name, subject_title):
    """Создает похвалу для ученика по указанному предмету."""
    schoolkid = get_schoolkid(schoolkid_name)
    last_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title).order_by('-date').first()
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
    """Изменяет оценки ученика с двойками и тройками на пятерки."""
    schoolkid = get_schoolkid(schoolkid_name)
    updated_count = Mark.objects.filter(schoolkid=schoolkid, value__in=[2, 3]).update(value=5)
    if updated_count:
        print(f"Оценки ученика '{schoolkid.full_name}' изменены на пятерки.")
    else:
        print(f"У ученика '{schoolkid.full_name}' нет оценок, которые можно было бы изменить.")


def remove_chastisements(schoolkid_name):
    """Удаляет все плохие комментарии для указанного ученика."""
    schoolkid = get_schoolkid(schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    """Получаем все замечания для ученика."""
    deleted_count, _ = chastisements.delete()
    """Удаляем все найденные замечания."""
    if deleted_count:
        print(f"Удалено {deleted_count} наказаний для ученика '{schoolkid.full_name}'.")
    else:
        print(f"У ученика '{schoolkid.full_name}' нет замечаний  для удаления.")

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Изменить оценки")
        print("2. Создать похвалу")
        print("3. Удалить замчание")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            name = input("Введите имя ученика: ")
            change_marks(name)
        elif choice == '2':
            name = input("Введите имя ученика: ")
            subject = input("Введите название предмета: ")
            create_commendation(name, subject)
        elif choice == '3':
            name = input("Введите имя ученика: ")
            remove_chastisements(name)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


