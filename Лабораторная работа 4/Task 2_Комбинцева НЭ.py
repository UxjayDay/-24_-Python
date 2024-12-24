# TODO импортировать необходимые молули
import csv  # Для работы с CSV файлами
import json  # Для работы с JSON файлами

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:    # TODO считать содержимое csv файла

        # Создаем объект CSV reader с разделителем ","
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        # Создаем список для хранения данных в формате JSON
        json_data = []

        # Проходим по каждой строке CSV файла
        for row in csv_reader:
            # Добавляем словарь в список
            json_data.append(row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Для проверки
    task()

    # Открываем и выводим содержимое JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
