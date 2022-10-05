# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_read(csv_data) -> list:
    # Чтение данных из строки
    return [line.split(';') for line in csv_data.split('\n')]


def get_sort(data: list):
    # Сортировка по возрасту по возрастанию
    return sorted(data, key=lambda x: int(x[1]))


def get_filter(data):
    # Фильтрация
    return [x for x in data if int(x[1]) > 10]


def get_users_list():
    data = get_read(csv)
    data = get_sort(data)
    return get_filter(data)


if __name__ == '__main__':
    print(get_users_list())
