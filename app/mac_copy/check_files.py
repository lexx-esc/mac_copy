import os
from shutil import copy as shcopy
from datetime import datetime


def check_source(source, destination, up_level=False, log_clear=False):
    lst = os.listdir(source)
    for i in lst:
        if is_exclude(i):
            continue
        path = os.path.join(source, i)
        if not os.path.exists(path):
            log(path, not up_level)
            continue
        if os.path.isdir(path):
            up_level = path if not up_level else up_level
            d_path = destination_mkdir(destination, i)
            check_source(path, d_path, up_level)
        if os.path.isfile(path):
            copyfile(path, destination)


def is_exclude(value):
    ex = ['.DocumentRevisions-V100'
          , '.DS_Store'
          , '.Spotlight-V100'
          , 'fb2.Flibusta.Net']
    return value in ex


def log(log_data, clear):
    if clear:
        attribute = 'w'
    else:
        attribute = 'a'

    time = str(datetime.now())
    mes = ': ' + log_data + ' - не существует' + '\n'
    string = time + mes
    print(string)
    with open('./copy.log', attribute) as file:
        file.write(string)


def destination_mkdir(destination, dir_name):
    path = jot_test(os.path.join(destination, dir_name))
    os.mkdir(path)
    return path


def copyfile(filepath, topath):
    f_name = jot_test(os.path.basename(filepath))
    shcopy(filepath, os.path.join(topath, f_name))


def jot_test(string):
    if 'й' in string:
        return string.replace('й', 'й')
    return string
