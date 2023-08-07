""" ---Задача 6 семинара №15---.
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога
- расширение, если это файл
- флаг каталога
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование"""

import argparse
import logging
import os
from os import walk
from collections import namedtuple

FILE = 'Task.log'

logging.basicConfig(filename=FILE, filemode='w', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='files', field_names='name, ext, is_folder, parent_folder')


def pars():
    parser = argparse.ArgumentParser(prog='Задача №6 семинара 15',
                                     epilog='name - имя файла без расширения или название каталога | '
                                            'ext - расширение, если это файл | '
                                            'is_folder - флаг каталога | '
                                            'parent_folder - название родительского каталога',
                                     description='Данный модуль осуществляет запись информации '
                                                 'о содержимом каталога в файл Task.log')

    parser.add_argument('-p', '--path', default=os.curdir, help='путь до директории на компе')
    arg = parser.parse_args()
    return directory_info(arg.path)


def directory_info(file_p: str) -> None:
    files_list = walk(file_p)
    for catalog in files_list:
        objects_path, folders, files = catalog
        if len(folders) != 0:
            for folder in folders:
                obj = file(folder, '', True, objects_path.split('\\')[-1])
                logger.info(obj)
        if len(files) != 0:
            for f in files:
                f_name, f_ext = f.split('.')
                obj = file(f_name, f_ext, False, objects_path.split('\\')[-1])
                logger.info(obj)
    print(f'> Информация о содержимом каталога успешно записана в файл {FILE}')


if __name__ == '__main__':
    pars()