# TODO решите задачу
import json

# Имя файла с данными
INPUT_FILENAME = "input.json"

def task() -> float:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Загружаем данные из файла в формате списка словарей

 # Переменную для суммы произведений
    total_sum = 0.0

    # Проходим по каждому словарю в списке
    for item in data:
        # Извлекаем значения "score" и "weight"
        score = item.get("score", 0.0)  # Если ключа нет, используем 0.0
        weight = item.get("weight", 0.0)  # Если ключа нет, используем 0.0
        # Вычисляем произведение и добавляем к общей сумме
        total_sum += score * weight

    # Округляем результат до 3 знаков после запятой
    return round(total_sum, 3)

print(task())
