# TODO Напишите функцию find_common_participants
def find_common_participants(spisok1, spisok2, otdel=','):
    participants_first_group = spisok1.split(otdel)
    participants_second_group = spisok2.split(otdel)
    spisok = list(set(participants_first_group).intersection(set(participants_second_group)))
    spisok.sort()
    return spisok


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
spisok_gotov = find_common_participants(participants_first_group, participants_second_group, otdel='|')
print(spisok_gotov)