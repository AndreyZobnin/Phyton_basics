#Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from pathlib import Path
from number import number
from generation import generation
from two_files import two_files
from files_make import files_make
from new_file import new_file
from renames import renames

if __name__ == '__main__':
    number(20, 'numbers.txt')

    generation(10, 4, 7, Path('names.txt'))

    two_files(Path('numbers.txt'), Path('names.txt'), Path('result.txt'))

    files_make('bin', count=10)

    data = {
        'txt': 4,
        'zip': 3,
    }

    new_file(data)

    renames(4, 'bin', 'zip', [2, 4], "new")