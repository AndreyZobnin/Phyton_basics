#Прочитайте созданный в прошлом задании csv файл без
#использования csv.DictReader.
#Дополните id до 10 цифр незначащими нулями.
#В именах первую букву сделайте прописной.
#Добавьте поле хеш на основе имени и идентификатора.
#Получившиеся записи сохраните в json файл, где каждая строка
#csv файла представлена как отдельный json словарь.
#Имя исходного и конечного файлов передавайте как аргументы
#функции.

import csv
import json
from pathlib import Path


def csv_v_json(file_out: Path, file_in: Path) -> None:
    json_list = []
    with open(file_out, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            json_dict = {}
            level, user_id, name = row
            json_dict['level'] = int(level)
            json_dict['id'] = user_id.zfill(10)
            json_dict['name'] = name.title()
            json_dict['hash'] = hash(f'{user_id}{name}')
            json_list.append(json_dict)

    with open(file_in, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


if __name__ == '__main__':
    csv_v_json(Path('out.csv'), Path('json_in.json'))