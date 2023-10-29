def find_common_participants(str_1, str_2, sep_=","):
    set_1 = set(str_1.split(sep_))
    set_2 = set(str_2.split(sep_))

    set_3 = list(set_1.intersection(set_2))

    return sorted(set_3)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, sep_ = "|")
