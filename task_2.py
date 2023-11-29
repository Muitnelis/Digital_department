import csv, json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открытие файла для чтения сsv строк
    with open(INPUT_FILENAME) as file:
        reader = list(csv.reader(file, delimiter=',', quotechar='\n'))
        # Чтение данных
        header = reader[0]

    json_ans = []
    for i in range(1, len(reader)):
        tmp = {}
        for j in range(len(header)):
            tmp[header[j]] = reader[i][j]
        json_ans.append(tmp)

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(json_ans, file, indent=4)

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
