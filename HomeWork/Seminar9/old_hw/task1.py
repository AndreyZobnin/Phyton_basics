import csv
import json
from random import randint as r
from random import uniform as u
from typing import Callable
from os.path import exists


def found_roots_from_csv(file_name: str = 'file.csv'):
    if not exists(file_name):
        scv_generator('params_list.csv')

    def deco(func: Callable):
        with open(file_name, encoding='utf-8') as f_csv:
            csv_reader = csv.DictReader(f_csv, dialect='excel-tab', lineterminator='\n')
            data = list(csv_reader.reader)[1:]
            results = []

        def wrapper(*args, **kwargs):
            for line in data:
                results.append(func(float(line[0]), float(line[1]), float(line[2])))

            return results

        return wrapper

    return deco


def save_roots_to_json(file_name: str = 'file.json'):
    def decorator(func: Callable):
        data = []

        def wrapp(*args, **kwargs):
            with open(file_name, 'w', encoding='utf-8') as f_json:
                json_dict = {'params': args, **kwargs}
                result = func(*args, **kwargs)
                json_dict['roots'] = f'{result}'
                data.append(json_dict)
                json.dump(data, f_json)

            return result

        return wrapp

    return decorator


def scv_generator(file_name: str) -> None:
    min_gen = -100
    max_gen = 100
    min_lines = 100
    max_lines = 1000
    gen_numbers = [{'Num a': round(u(min_gen, max_gen), 3),
                    'Num b': round(u(min_gen, max_gen), 3),
                    'Num c': round(u(min_gen, max_gen), 3)}
                   for _ in range(r(min_lines, max_lines))]

    with open(file_name, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, dialect='excel-tab',
                                    fieldnames=('Num a', 'Num b', 'Num c'),
                                    lineterminator='\n')
        csv_writer.writeheader()
        csv_writer.writerows(gen_numbers)


@found_roots_from_csv('params_list.csv')
@save_roots_to_json('roots.json')
def quadratic_equation(a: float, b: float, c: float) -> float | tuple[float, float] | tuple[complex, complex]:
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        result = x1, x2

    elif d == 0:
        x = -b / (2 * a)
        result = x

    else:
        d = complex(d, 0)
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        result = x1, x2

    return result


if __name__ == '__main__':
    res = quadratic_equation()